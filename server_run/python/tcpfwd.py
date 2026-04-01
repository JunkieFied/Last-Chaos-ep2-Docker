#!/usr/bin/env python
"""TCP forwarder using select() for proper concurrent connection handling.
Usage: python tcpfwd.py <target_port>:<proxy_port> [...]
"""
import socket, select, sys, time, os

def wait_for_port(port):
    while True:
        try:
            s = socket.socket()
            s.connect(('127.0.0.1', port))
            s.close()
            return
        except:
            time.sleep(1)

def run_proxy(target_port, proxy_port):
    wait_for_port(target_port)
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.setblocking(False)
    srv.bind(('0.0.0.0', proxy_port))
    srv.listen(128)
    sys.stdout.write("tcpfwd: 0.0.0.0:%d -> 127.0.0.1:%d\n" % (proxy_port, target_port))
    sys.stdout.flush()

    pairs = {}  # socket -> partner socket
    inputs = [srv]

    while True:
        readable, _, exceptional = select.select(inputs, [], inputs, 1.0)
        for s in readable:
            if s is srv:
                try:
                    client, addr = s.accept()
                    client.setblocking(False)
                    backend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    backend.connect(('127.0.0.1', target_port))
                    backend.setblocking(False)
                    pairs[client] = backend
                    pairs[backend] = client
                    inputs.append(client)
                    inputs.append(backend)
                except Exception as e:
                    sys.stderr.write("tcpfwd %d: accept/connect error: %s\n" % (proxy_port, str(e)))
                    sys.stderr.flush()
            else:
                partner = pairs.get(s)
                if partner:
                    try:
                        data = s.recv(65536)
                        if data:
                            partner.sendall(data)
                        else:
                            # Connection closed
                            for sock in (s, partner):
                                if sock in inputs:
                                    inputs.remove(sock)
                                pairs.pop(sock, None)
                                try: sock.close()
                                except: pass
                    except Exception:
                        for sock in (s, partner):
                            if sock in inputs:
                                inputs.remove(sock)
                            pairs.pop(sock, None)
                            try: sock.close()
                            except: pass

        for s in exceptional:
            partner = pairs.get(s)
            for sock in (s, partner):
                if sock and sock in inputs:
                    inputs.remove(sock)
                pairs.pop(sock, None)
                try: sock.close()
                except: pass

if len(sys.argv) < 2:
    print("Usage: %s target:proxy [target:proxy ...]" % sys.argv[0])
    sys.exit(1)

children = []
for arg in sys.argv[1:]:
    target, proxy = arg.split(':')
    pid = os.fork()
    if pid == 0:
        run_proxy(int(target), int(proxy))
        sys.exit(0)
    children.append(pid)

for pid in children:
    os.waitpid(pid, 0)

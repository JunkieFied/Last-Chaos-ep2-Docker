#define _GNU_SOURCE
#include <dlfcn.h>
#include <sys/socket.h>
#include <netinet/in.h>

/* Intercept bind() to change any specific IP to 0.0.0.0 (INADDR_ANY).
 * This allows servers to advertise 127.0.0.1 in their config (for clients)
 * while actually binding to all interfaces (for Docker port forwarding).
 */
int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen) {
    int (*original_bind)(int, const struct sockaddr *, socklen_t);
    original_bind = dlsym(RTLD_NEXT, "bind");

    if (addr->sa_family == AF_INET) {
        struct sockaddr_in *addr_in = (struct sockaddr_in *)addr;
        unsigned long ip = ntohl(addr_in->sin_addr.s_addr);
        /* Change any non-zero, non-INADDR_ANY bind to 0.0.0.0 */
        if (ip != 0 && ip != 0x7F00000B) { /* skip Docker DNS 127.0.0.11 */
            struct sockaddr_in modified = *addr_in;
            modified.sin_addr.s_addr = htonl(INADDR_ANY);
            return original_bind(sockfd, (struct sockaddr *)&modified, addrlen);
        }
    }
    return original_bind(sockfd, addr, addrlen);
}

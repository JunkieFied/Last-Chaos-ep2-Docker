import os

# bindfix.so intercepts bind() calls: changes 127.0.0.1 -> 0.0.0.0
# This lets Docker port forwarding work while configs advertise 127.0.0.1 to clients
PRELOAD = "LD_PRELOAD=/usr/lib/bindfix.so"

os.system("setenforce 0")
print("-------------------------------------------------------------------")
print("Starting Connectorserver screen                                [OK]")
os.system("cd server/Connector/Connector/ && screen -d -m -S connectorserver bash -c '%s ./run'" % PRELOAD)
print("Starting Helperserver screen                                   [OK]")
os.system("cd server/Helper/Helper/ && screen -d -m -S helperserver bash -c '%s ./run'" % PRELOAD)
print("Starting Sub-Helperserver screen                               [OK]")
os.system("cd server/SubHelper/SubHelper/ && screen -d -m -S subhelperserver bash -c '%s ./run'" % PRELOAD)
print("Starting Messengerserver screen                                [OK]")
os.system("cd server/Messenger/Messenger/ && screen -d -m -S messengerserver bash -c '%s ./run'" % PRELOAD)
print("Starting Loginserver screen                                    [OK]")
os.system("cd server/LoginServer/LoginServer/ && screen -d -m -S loginserver bash -c '%s ./run'" % PRELOAD)
print("Starting Gameserver1 screen                                    [OK]")
os.system("cd server/GameServer/GameServer1/ && screen -d -m -S gameserver1 bash -c '%s ./run2'" % PRELOAD)
print("Starting Billingserver (cash) screen                           [OK]")
os.system("cp -r server/CashServer/CashServer /tmp/CashServer && mkdir -p /tmp/CashServer/Log && cd /tmp/CashServer && screen -d -m -S cashserver bash -c 'MONO_IOMAP=all mono ./cash.exe'")
os.system("screen -ls")
print("-------------------------------------------------------------------")
print("--------------------------STARTUP DONE!----------------------------")
print("")

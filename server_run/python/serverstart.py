import os




os.system("setenforce 0")
print("-------------------------------------------------------------------")
print("Starting Connectorserver screen                                [OK]")
os.system("cd server/Connector/Connector/ && screen -d -m -S connectorserver ./run")
print("Starting Helperserver screen                                   [OK]")
os.system("cd server/Helper/Helper/ && screen -d -m -S helperserver ./run")
print("Starting Sub-Helperserver screen                               [OK]")
os.system("cd server/SubHelper/SubHelper/ && screen -d -m -S subhelperserver ./run")
print("Starting Messengerserver screen                                [OK]")
os.system("cd server/Messenger/Messenger/ && screen -d -m -S messengerserver ./run")
print("Starting Loginserver screen                                    [OK]")
os.system("cd server/LoginServer/LoginServer/ && screen -d -m -S loginserver ./run")
print("Starting Gameserver1 screen                                    [OK]")
os.system("cd server/GameServer/GameServer1/ && screen -d -m -S gameserver1 ./run2")
print("Starting Billingserver (cash) screen                           [OK]")
os.system("cd server/CashServer/CashServer/ && screen -d -m -S cashserver ./run")
os.system("screen -ls")
print("-------------------------------------------------------------------")
print("--------------------------STARTUP DONE!----------------------------")
print("")

# os.system("screen -ls")
# os.system("cd /home/lastchaos/server/Connector/Connector/ && screen -d -m -S connectorserver ./run")



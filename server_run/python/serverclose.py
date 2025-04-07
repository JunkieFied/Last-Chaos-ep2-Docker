#!/usr/bin/python

# PYTHON CODE BY PONYCHAOS (C) 2013

import os
import time

print("LastChaos EP2/EP3 Automated Private Server Tool")
print("")
print("")
print("-------------------------------------------------------------------")
print("|                                                                 |")
print("|  Please make sure first to PROPERLY shutdown the gameserver by  |")
print("|  entering the /shutdown command as GameMaster/Administrator!    |")
print("|                                                                 |")
print("|     !!! OTHERWISE THERE WILL BE RISKS OF DATA LOSS !!!          |")
print("|                                                                 |")
print("-------------------------------------------------------------------")
print("")
print("")
print("")
print("If you didn't shutdown the gameserver properly, now is your chance!")
print("Cancel this script by pressing CTRL+C or STRG+C")
print("Waiting 10 seconds...")
time.sleep(10)
print("")
print("")
print("Begin shutdown... (no screen session found means the server is already closed)")
time.sleep(3)
print("")
print("Stopping Billingserver (cash) screen                           [OK]")
os.system("screen -r cashserver -X quit")

print("Stopping Messengerserver screen                                [OK]")
os.system("screen -r messengerserver -X quit")

print("Stopping Helperserver screen                                   [OK]")
os.system("screen -r helperserver -X quit")

print("Stopping Sub-Helperserver screen                               [OK]")
os.system("screen -r subhelperserver -X quit")

print("Stopping Loginserver screen                                    [OK]")
os.system("screen -r loginserver -X quit")

print("Stopping GameServer1 screen                                    [OK]")
os.system("screen -r gameserver1 -X quit")

print("Stopping Connectorserver screen                                [OK]")
os.system("screen -r connectorserver -X quit")

print("")
os.system("screen -ls")
print("")

print("-------------------------------------------------------------------")
print("--------------------------SHUTDOWN DONE!---------------------------")
print("")



import os 
import sys
from colorama import Fore, Back, Style
os.system("sudo git clone https://github.com/Mange/rtl8192eu-linux-driver")
os.system("cd rtl8192eu-linux-driver; make; sudo make install")   
os.system("sudo echo blacklist rtl8192cu > /etc/modprobe.d/blacklist.conf")
i = str(input("Do you want to reboot y/n?:\n"))

if  i == "y":
    print(Fore.YELLOW)
    print("-" * 50)
    print(Fore.CYAN)
    print("Rebooting")
    print(Fore.YELLOW)
    print("-" * 50)
    os.system("sudo reboot")

if i == "Y":
    print(Fore.YELLOW)
    print("-" * 50)
    print(Fore.CYAN)
    print("Rebooting")
    print(Fore.YELLOW)
    print("-" * 50)

elif i == "n": 
    print(Fore.RED)
    print("\nExiting")
    sys.exit

elif i == "N": 
    print(Fore.RED)
    print("\nExiting")
    print(Fore.RESET)
    sys.exit

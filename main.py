import os
import discord
import psutil
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

def check_server_status(server_name):
    for process in psutil.process_iter(attrs=['pid','name']):
        if(server_name.lower() in (process.info['name']).lower()):
        # if(process.info['name'] == server_name):
            return True
    return False

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.command()
async def listservers(ctx):
     await ctx.send("The currently available serversare: Moria, Enshrouded")

@client.command()
@commands.has_role(1319646693838557264)
async def startserver(ctx, server):
    if check_server_status(server):
        await ctx.send(server + " server is already running")
        return
    else:
        if(server.lower() == 'moria'):
            os.startfile("C:\gameservers\moriaserver\startMoriaServer.bat")
            await ctx.send(server + " server started.")
            return
        if(server.lower() == 'valheim'):
            # os.startfile("C:/Users/Kevin/Desktop/commando.bat")
            await ctx.send(server + " server started.")
            return
        if(server.lower() == 'enshrouded'):
            os.startfile("C:\gameservers\enshroudedserver\StartEnshroudedServer.bat")
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
            os.startfile("C:\gameservers\enshroudedserver\CloseEnshroudedServer.bat")
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
import os
import discord
import random
# from dotenv import load_dotenv
from discord.ext import commands
# from webserver import keep_alive

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.command()
async def listservers(ctx):
     await ctx.send("The currently available serversare: Moria, Valheim, Enshrouded")

@client.command()
async def startserver(ctx, server: str):
    if(server.lower() == 'moria'):
        os.startfile("moriatest.bat")
        await ctx.send(server + " server started.")
        return
    if(server.lower() == 'valheim'):
        # os.startfile("C:/Users/Kevin/Desktop/commando.bat")
        await ctx.send(server + " server started.")
        return
    if(server.lower() == 'enshrouded'):
        # os.startfile("C:/Users/Kevin/Desktop/commando.bat")
        await ctx.send(server + " server started.")
        return
    else:
        await ctx.send(server + " is not an option on !listservers.")
        return

with open('ServerBotToken.txt', 'r') as file: 
    TOKEN = file.read().rstrip()
client.run(TOKEN)
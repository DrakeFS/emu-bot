import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
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
@commands.has_role(1319646693838557264)
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
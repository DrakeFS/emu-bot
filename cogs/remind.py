import discord
from discord.ext import commands
import asyncio

class Remind(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("remind cog loaded")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command()
    async def remind(self, ctx, time, *, task):
        def convert(time):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600*24}

            unit = time[-1]

            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2
            return val * time_dict[unit]
        converted_time = convert(time)
        if converted_time == -1:
            await ctx.send("You didn't enter the time correctly.")
            return
        if converted_time == -2:
            await ctx.send("Time must be an integer.")
            return
        await ctx.send(f"Started reminder for **{task}** and will last {time}")

        await asyncio.sleep(converted_time)
        await ctx.send(f"{ctx.author.mention} your reminder for **{task}** has expired.")

def setup(client):
    client.add_cog(Remind(client))
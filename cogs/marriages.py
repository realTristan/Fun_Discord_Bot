import discord, os, os.path, json, asyncio, random
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *


class Marriages(commands.Cog):
    def __init__(self, client):
        self.client = client

    def write(self, file, data, f):
        with open(os.path.dirname(__file__) + f'\\..\\json\\{file}.json', 'w') as x:
            json.dump(data, x, indent=4)
            f.close(); x.close()



    @commands.command()
    async def marry(self, ctx, user : discord.Member):
        marriages = ["'s hound", "", "'s tiger", "'s gremlin", "'s eagle", "'s aunt", "'s troll"]
        await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} has proposed to **{user.mention}{random.choice(marriages)}**", color=16739560))
        await ctx.send(embed=discord.Embed(description=f"{user.mention} do you accept, their proposal?", color=16739560))
        msg = await self.client.wait_for("message", check=lambda m: m.author == user and m.channel == ctx.message.channel, timeout=10)
        
        if 'yes' in msg.content:
            await ctx.send(embed=discord.Embed(description=f"Hooray! {user.mention} has accepted {ctx.author.mention}'s proposal", color=16739560))
            with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
                data=json.load(f)
                data[str(ctx.message.guild.id)][str(ctx.author.id)]["marriages"].append(int(user.id))
                data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] += 10
                self.write('data', data, f)

        elif 'no' in msg.content:
            await ctx.send(embed=discord.Embed(description=f"Awwww! {ctx.author.mention} better luck next time!", color=16739560))



    @commands.command()
    async def divorce(self, ctx, user : discord.Member):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            if int(user.id) in data[str(ctx.message.guild.id)][str(ctx.author.id)]["marriages"]:
                await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} has embarked a lonely journey without {user.mention}', color=16739560))
                data[str(ctx.message.guild.id)][str(ctx.author.id)]["marriages"].remove(int(user.id))
                data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] -= 10
                self.write('data', data, f)
    


    @commands.command()
    async def marriages(self, ctx):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f); marriages_arr = []
            for married in data[str(ctx.message.guild.id)][str(ctx.author.id)]["marriages"]:
                marriages_arr.append(f"<@{married}>")

            marriages = ' '.join(str(enum) for enum in marriages_arr)
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} is intimately married to {marriages}', color=16739560))






def setup(client):
    client.add_cog(Marriages(client))

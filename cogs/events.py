import discord, os, os.path, json, asyncio, random, string
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    def write(self, file, data, f):
        with open(os.path.dirname(__file__) + f'\\..\\json\\{file}.json', 'w') as x:
            json.dump(data, x, indent=4)
            x.close()




    @commands.command()
    @has_permissions(administrator=True)
    async def addQAevent(self, ctx, *args):
        string = ' '.join(str(enum) for enum in list(args))
        qa = string.split(">")
        print(qa)
        with open(os.path.dirname(__file__) + '\\..\\json\\events.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["qa_event"].update({qa[0]: qa[1]})
            self.write("events", data, f)

        await ctx.send(embed=discord.Embed(title='Q&A Added', description=f'**Question:** {qa[0]}\n**Answer:** {qa[1]}', color=65535))



    @commands.command()
    @has_permissions(administrator=True)
    async def delQAevent(self, ctx, event: str):
        with open(os.path.dirname(__file__) + '\\..\\json\\events.json','r+') as f:
            data=json.load(f)
            for line in list(data[str(ctx.message.guild.id)]["qa_event"]):
                    if event in line:
                        del data[str(ctx.message.guild.id)]["qa_event"][str(line)]
            self.write("events", data, f)
        await ctx.send(embed=discord.Embed(title='Q&A Removed', description=f'**Question:** {event}\n**Answer:** {data[str(ctx.message.guild.id)]["qa_event"][str(event)]}', color=65535))



    @commands.command()
    async def showQAevents(self, ctx):
        with open(os.path.dirname(__file__) + '\\..\\json\\events.json','r+') as f:
            data=json.load(f)
            embed=discord.Embed(title='Q&A Events', color=65535)
            for line in data[str(ctx.message.guild.id)]["qa_event"]:
                embed.add_field(name=f'{line}', value=f'{data[str(ctx.message.guild.id)]["qa_event"][line]}')
            await ctx.send(embed=embed)



    @commands.command()
    @has_permissions(manage_messages=True)
    async def startQAevent(self, ctx):
        id = ''.join(random.choice(string.digits) for _ in range(3))
        with open(os.path.dirname(__file__) + '\\..\\json\\events.json','r+') as f:
            data=json.load(f)
            events = list(data[str(ctx.message.guild.id)]["qa_event"])
            q = random.choice(events)
            await ctx.send(embed=discord.Embed(title=f'Q&A Event #{id}', description=f'{q}', color=65535))
        try:
            msg = await self.client.wait_for("message", check=lambda m: m.channel == ctx.message.channel, timeout=300)
            if data[str(ctx.message.guild.id)]["qa_event"][str(q)] in msg.content:
                await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} was correct! +20 points', color=65535))
                with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
                    data=json.load(f)
                    data[str(msg.guild.id)]["users"][str(msg.author.id)]["points"] += 20
                    self.write("data", data, f)

        except asyncio.TimeoutError:
            await ctx.send(embed=discord.Embed(title=f'Q&A Event #{id}', description=f'**Correct answer:** {data[str(ctx.message.guild.id)]["qa_event"][str(q)]}', color=65535))









def setup(client):
    client.add_cog(Events(client))

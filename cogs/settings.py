import discord, os, os.path, json, asyncio, random
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *


class Settings(commands.Cog):
    def __init__(self, client):
        self.client = client


    def write(self, file, data, f):
        with open(os.path.dirname(__file__) + f'\\..\\json\\{file}.json', 'w') as x:
            json.dump(data, x, indent=4)
            x.close()



    @commands.command()
    async def setup(self, ctx):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            if str(ctx.message.guild.id) not in data:
                data.update({
                    str(ctx.message.guild.id): {
                        "commands" : {
                            "kill_command": {
                                "kill_timer": 0
                            }
                        },
                        "users" : {

                        }
                    }
                })

        self.write('data', data, f)



    @commands.command(aliases=['lb'])
    async def leaderboard(self, ctx):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json', "r+") as f:
            data=json.load(f); lb_dict = {}

            for user in data[str(ctx.message.guild.id)]["users"]:
                lb_dict.update({f"<@{user}>": data[str(ctx.message.guild.id)]["users"][user]["points"]})
            top_users = {k: v for k, v in sorted(lb_dict.items(), key=lambda item: item[1], reverse=True)}; names = ''

            for postion, user in enumerate(top_users):
                names += f'**{postion+1}:** {user} [{top_users[user]}]\n'
                if postion+1 > 19:
                    break
            await ctx.send(embed=discord.Embed(title='Points Leaderboard', description=names, color=65535)); f.close()


    @commands.command()
    async def points(self, ctx, *args):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json', "r+") as f:
            data=json.load(f)
            if not args:
                await ctx.send(embed=discord.Embed(title=f'Points', description=f'**User:** {ctx.author.mention}\n**Amount:** {data[str(ctx.message.guild.id)]["users"][str(ctx.author.id)]["points"]}', color=65535))
            else:
                user_id = str(list(args)[0]).strip('<').strip('>').strip('@').replace('!', '')
                await ctx.send(embed=discord.Embed(title=f'Points', description=f'**User:** {list(args)[0]}\n**Amount:** {data[str(ctx.message.guild.id)]["users"][user_id]["points"]}', color=65535))
            




    # Giving points for every message / image they send
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
                data=json.load(f)

                if not message.attachments:
                    data[str(message.guild.id)]["users"][str(message.author.id)]["points"] += 0.25
                    
                elif message.attachments:
                    data[str(message.guild.id)]["users"][str(message.author.id)]["points"] += 0.5

                self.write('data', data, f)





def setup(client):
    client.add_cog(Settings(client))

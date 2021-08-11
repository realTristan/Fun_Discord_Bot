import discord, os, os.path, json, asyncio, random, time
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
    @has_permissions(administrator=True)
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

                        },
                        "settings": {
                            "mod_role": 0,
                            "prefix": "=",

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


    # checks yours or another users points
    @commands.command()
    async def points(self, ctx, *args):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json', "r+") as f:
            data=json.load(f)
            if not args:
                await ctx.send(embed=discord.Embed(title=f'Points', description=f'**User:** {ctx.author.mention}\n**Amount:** {data[str(ctx.message.guild.id)]["users"][str(ctx.author.id)]["points"]}', color=65535))
            else:
                user_id = str(list(args)[0]).strip('<').strip('>').strip('@').replace('!', '')
                await ctx.send(embed=discord.Embed(title=f'Points', description=f'**User:** {list(args)[0]}\n**Amount:** {data[str(ctx.message.guild.id)]["users"][user_id]["points"]}', color=65535))
            

    # send your points to another user
    @commands.command()
    async def give(self, ctx, user : discord.Member, amount: int):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json', "r+") as f:
            data=json.load(f)
            if data[str(ctx.message.guild.id)]["users"][str(ctx.author.id)]["points"] - int(amount) >= 0:
                data[str(ctx.message.guild.id)]["users"][str(ctx.author.id)]["points"] -= int(amount)
                data[str(ctx.message.guild.id)]["users"][str(user.id)]["points"] += int(amount)
                self.write("data", data, f); f.close()
                await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} gave **{amount} points** to {user.mention}', color=65535))




    @commands.command()
    @has_permissions(administrator=True)
    async def setpoints(self, ctx, user : discord.User, amount : int):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json', "r+") as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(user.id)]["points"] = int(amount)
            self.write("data", data, f); f.close()
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} set {user.mention}'s points to **{amount}**", color=65535))



    @commands.command()
    @has_permissions(administrator=True)
    async def modrole(self, ctx, role: discord.Role):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json', "r+") as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["settings"]["mod_role"] = int(role.id)
            self.write("data", data, f); f.close()
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} set {role.mention} as the mod role', color=65535))

    

    @commands.command()
    @has_permissions(administrator=True)
    async def addmod(self, ctx, user : discord.Member):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json', "r+") as f:
            data=json.load(f)
            role = ctx.message.guild.get_role(int(data[str(ctx.message.guild.id)]["settings"]["mod_role"]))
            await user.add_roles(role)
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} added {user.mention} as a moderator', color=65535))




    @commands.command()
    @has_permissions(administrator=True)
    async def delmod(self, ctx, user : discord.Member):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json', "r+") as f:
            data=json.load(f)
            role = ctx.message.guild.get_role(int(data[str(ctx.message.guild.id)]["settings"]["mod_role"]))
            await user.remove_roles(role)
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} removed {user.mention} from being a moderator', color=65535))




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




    #tracking how long an users in the vc for
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        with open(os.path.dirname(__file__) + '\\..\\json\\vc.json','r+') as f:
            data=json.load(f)
            if not before.channel and after.channel: # when they join the channel
                data[str(member.guild.id)].update({str(member.id): {"joined": time.time()}})
                self.write("vc", data, f)

            elif before.channel and not after.channel: #when they leave the channel
                timeLeft = time.time() - data[str(member.guild.id)][str(member.id)]["joined"]
                with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
                    data=json.load(f)
                    data[str(member.guild.id)]["users"][str(member.id)]["points"] += round(timeLeft / 60)
                    self.write("data", data, f)








def setup(client):
    client.add_cog(Settings(client))

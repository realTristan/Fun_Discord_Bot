import discord, os, os.path, json, asyncio, random
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    def write(self, file, data, f):
        with open(os.path.dirname(__file__) + f'\\..\\json\\{file}.json', 'w') as x:
            json.dump(data, x, indent=4)
            f.close(); x.close()



    # bite commands doesn't change any points
    @commands.command()
    async def bite(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} has viciously devoured {random.choice(ctx.message.guild.members).mention}'s flesh!‏‏‎ ‎‏‏‎ ‎👹", color=12517376))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} has viciously devoured {list(args)[0]}'s flesh!‏‏‎ ‎‏‏‎ ‎👹", color=12517376))

    # bonk command doesn't change any points
    @commands.command()
    async def bonk(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} bonk {random.choice(ctx.message.guild.members).mention}", color=65450))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} bonk {list(args)[0]}", color=65450))


    # barf command doesn't change any points
    @commands.command()
    async def barf(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} spew last nights dinner all over {random.choice(ctx.message.guild.members).mention}!‏‏‎ ‎‏‏‎ ‎🤮", color=2883328))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} spew last nights dinner all over {list(args)[0]}!‏‏‎ ‎‏‏‎ ‎🤮", color=2883328))


    # barf command doesn't change any points
    @commands.command()
    async def thumbsup(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} gently raised his thumb towards {random.choice(ctx.message.guild.members).mention}!‏‏‎ ‎‏‏‎ ‎👍", color=2883328))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} gently raised his thumb towards {list(args)[0]}!‏‏‎ ‎‏‏‎ ‎👍", color=2883328))


    # pout command doesn't change any points
    @commands.command()
    async def pout(self, ctx):
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} pouts their lips.', color=2883328))


    # sleepy command doesn't change any points
    @commands.command()
    async def sleepy(self, ctx):
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} is getting verryyyy sleepy...', color=37338))


    # stab command removes 1 point
    @commands.command()
    async def stab(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} just stabbed {random.choice(ctx.message.guild.members).mention}!! Everyone... **RUN!!**', color=12517376))
        else:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} just stabbed {list(args)[0]}!! Everyone... **RUN!!**', color=12517376))

        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] -= 1
            self.write('data', data, f)


    # wink command doesn't change any points
    @commands.command()
    async def wink(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} 😉 {random.choice(ctx.message.guild.members).mention}', color=16739560))
        else:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} 😉 {list(args)[0]}', color=16739560))


    # stop command doesn't change any points
    @commands.command()
    async def stop(self, ctx):
        await ctx.send(embed=discord.Embed(description=f'**STOP!!!**', color=16711680))


    # wag command doesn't change any points
    @commands.command()
    async def wag(self, ctx):
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} wags their tail.', color=2883328))


    # dance command rewards 1 point
    @commands.command()
    async def dance(self, ctx, *args):
        if not args:
            embed=discord.Embed(description=f'{ctx.author.mention} is bouta groove over to your significant other! Join the dance to stop them!‏‏‎ ‎‏‏‎ ‎💃', color=14287066)
            embed.set_footer(text=f'=dance @ {ctx.author}')
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=discord.Embed(description=f"Whew! That was a close one! Don't stop groooooooving though!", color=14287066))

        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] += 1
            self.write('data', data, f)


    # spit command doesn't change any points
    @commands.command()
    async def spit(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} hatefully spat on {random.choice(ctx.message.guild.members).mention}!‏‏‎ ‎‏‏‎ ‎😬", color=2883328))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} hatefully spat on {list(args)[0]}!‏‏‎ ‎‏‏‎ ‎😬", color=2883328))


    # poke command doesn't change any points
    @commands.command()
    async def poke(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} poked {random.choice(ctx.message.guild.members).mention}... Are they flirting?‏‏‎ ‎‏‏‎ ‎🧐", color=16776960))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} poked {list(args)[0]}... Are they flirting?‏‏‎ ‎‏‏‎ ‎🧐", color=16776960))



    # stare command doesn't change any points
    @commands.command()
    async def stare(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} is staring into {random.choice(ctx.message.guild.members).mention}'s dark soul...‏‏‎ ‎‏‏‎ ‎〰️", color=0))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} is staring into {list(args)[0]}'s dark soul...‏‏‎ ‎‏‏‎ ‎〰️", color=0))


    # pat command doesn't change any points
    @commands.command()
    async def pat(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} pat {random.choice(ctx.message.guild.members).mention}...‏‏‎", color=14671839))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} pat {list(args)[0]}...‏‏‎", color=14671839))


    # wave command doesn't change any points
    @commands.command()
    async def wave(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} royally shook their hand towards {random.choice(ctx.message.guild.members).mention}‏‏‎ ‎‏‏‎ ‎😉", color=16776960))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} royally shook their hand towards {list(args)[0]}‏‏‎ ‎‏‏‎ ‎😉", color=16776960))



    # kiss command rewards 1 point
    @commands.command()
    async def kiss(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} nervously kissed {random.choice(ctx.message.guild.members).mention}'s cheek!‏‏‎ ‎‏‏‎ ‎💕", color=16739560))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} nervously kissed {list(args)[0]}'s cheek!‏‏‎ ‎‏‏‎ ‎💕", color=16739560))

        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] += 1
            self.write('data', data, f)



    # slap command doesn't change any points
    @commands.command()
    async def slap(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} calmly swung their palm accross {random.choice(ctx.message.guild.members).mention}'s face!‏‏‎ ‎‏‏‎ ‎✋", color=16776960))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} calmly swung their palm accross {list(args)[0]}'s face!‏‏‎ ‎‏‏‎ ‎✋", color=16776960))



    # cry command gives doesn't change any points
    @commands.command()
    async def cry(self, ctx, *args):
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} is **crying** alone... someone should cheer them up!‏‏‎ ‎‏‏‎ ‎😢', color=43775))



    # highfive command rewards 1 point
    @commands.command()
    async def highfive(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} joyfully highfived {random.choice(ctx.message.guild.members).mention}!‏‏‎ ‎‏‏‎ ‎😄", color=2883328))
        else:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} joyfully highfived {list(args)[0]}!‏‏‎ ‎‏‏‎ ‎😄", color=2883328))

        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] += 1
            self.write('data', data, f)



    # burn command removes 1 point
    @commands.command()
    async def burn(self, ctx, *args):
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} just brutally burned {list(args)[0]}'))
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] += 1
            self.write('data', data, f)



    # cuddle command rewards 1 point
    @commands.command()
    async def cuddle(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} is **cuddling** with {random.choice(ctx.message.guild.members).mention}... shall this turn into a marriage?‏‏‎ ‎‏‏‎ ‎😳'))
        else:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} is **cuddling** with {list(args)[0]}... shall this turn into a marriage?‏‏‎ ‎‏‏‎ ‎😳'))
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] += 1
            self.write('data', data, f)



    # cheer command rewards 1 point
    @commands.command()
    async def cheer(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} has heroically **cheered up** {random.choice(ctx.message.guild.members).mention}!‏‏‎ ‎‏‏‎ ‎🎉'))
        else:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} has heroically **cheered up** {list(args)[0]}!‏‏‎ ‎‏‏‎ ‎🎉'))
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] += 1
            self.write('data', data, f)



    # scare command rewards 1 point
    @commands.command()
    async def scare(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f'**BOO!** {ctx.author.mention} jump scared {random.choice(ctx.message.guild.members).mention}!‏‏‎ ‎‏‏‎ ‎🎃', color=16744192))
        else:
            await ctx.send(embed=discord.Embed(description=f'**BOO!** {ctx.author.mention} jump scared {list(args)[0]}!‏‏‎ ‎‏‏‎ ‎🎃', color=16744192))
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] += 1
            self.write('data', data, f)



    # punching command removes one point
    @commands.command()
    async def punch(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} fed {random.choice(ctx.message.guild.members).mention} a fat knuckle sandwich!‏‏‎ ‎‏‏‎ ‎🤜', color=16776960))
        else:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} fed {list(args)[0]} a fat knuckle sandwich!‏‏‎ ‎‏‏‎ ‎🤜', color=16776960))
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] -= 1
            self.write('data', data, f)



    # kicking command removes 1 point
    @commands.command()
    async def dropkick(self, ctx, *args):
        if not args:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} aggressively dropkicked {random.choice(ctx.message.guild.members).mention} in their little butt!‏‏‎ ‎‏‏‎ ‎🦶', color=16776960))
        else:
            await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} aggressively dropkicked {list(args)[0]} in their little butt!‏‏‎ ‎‏‏‎ ‎🦶', color=16776960))
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] -= 1
            self.write('data', data, f)


    # fun kill event
    @commands.command()
    async def kill(self, ctx, user : discord.Member):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            if data[str(ctx.message.guild.id)]["commands"]["kill_command"]["kill_timer"] <= 0:
                await ctx.message.delete(); await ctx.message.channel.set_permissions(user, send_messages=False)
                await ctx.send('**A dead body has been found!**'); hint = (str(ctx.author)[:3] + str(ctx.author)[7:])
                await ctx.send(embed=discord.Embed(description=f'Someone has murdered {user.mention}! Find the killer to revive them! **Hint: {hint}**', color=12517376))
                try:
                    msg = await self.client.wait_for("message", check=lambda m: m.channel == ctx.message.channel, timeout=10)
                    if str(ctx.author.id) in str(msg.content).strip("<").strip(">").strip("@").replace("!",""):
                        await ctx.message.channel.set_permissions(user, send_messages=True)
                        await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} has been arrested for murdering {user.mention}‏‏‎ ‎‏‏‎ ‎⛓️', color=12517376))
                        data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] -= 50; self.write('data', data, f)
                except:
                    data[str(ctx.message.guild.id)]["users"][str(ctx.message.author.id)]["points"] += 100; self.write('data', data, f)
                    await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} has gotten away with {user.mention}'s 100$", color=12517376))
                    await ctx.message.channel.set_permissions(user, send_messages=True)

                data[str(ctx.message.guild.id)]["commands"]["kill_command"]["kill_timer"] = 1; self.write('data', data, f)
                await asyncio.sleep(300) # waits 5 minutes before being able to use =kill again
                data[str(ctx.message.guild.id)]["commands"]["kill_command"]["kill_timer"] = 0; self.write('data', data, f)
            else:
                await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} the doctors are still cleaning up from the last murder', color=12517376))





def setup(client):
    client.add_cog(Fun(client))

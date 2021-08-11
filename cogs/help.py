import discord, os, os.path, json, asyncio, random
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client


    def embeds(self, value):
        if value == "fun":
            embed = discord.Embed(title='List of Fun Commands', color=65535)
            embed2 = discord.Embed(color=65535)
            embed.add_field(name='Bite', value='Bites an user\n =bite @user')
            embed.add_field(name='Bonk', value='Bonks an user\n =bonk @user')
            embed.add_field(name='Barf', value='Barfs on an user\n =barf @user')
            embed.add_field(name='‏‏‎ ‎\nPout', value='Pout\n =pout')
            embed.add_field(name='‏‏‎ ‎\nThumbs Up', value='Sends a thumbsup to an user\n =thumbsup @user')
            embed.add_field(name='‏‏‎ ‎\nSleepy', value="Tell people you're sleepy\n =sleepy")
            embed.add_field(name='‏‏‎ ‎\nStab', value='Stab an user\n =stab @user')
            embed.add_field(name='‏‏‎ ‎\nWink', value='Winks at an user\n =wink @user')
            embed.add_field(name='‏‏‎ ‎\nStop', value='Stop...\n =stop')
            embed.add_field(name='‏‏‎ ‎\nWag', value='Wag your tail\n =wag')
            embed.add_field(name='‏‏‎ ‎\nDance', value='Dance with an users significant other\n =dance @user')
            embed.add_field(name='‏‏‎ ‎\nSpit', value='Spit on an user\n =spit @user')
            embed.add_field(name='‏‏‎ ‎\nPoke', value='Poke an user\n =poke @user')
            embed.add_field(name='‏‏‎ ‎\nStare', value='Stares at an user\n =stare @user')
            embed.add_field(name='‏‏‎ ‎\nPat', value='Pats an users back\n =pat @user')
            embed.add_field(name='‏‏‎ ‎\nWave', value='Waves at an user\n =wave @user')
            embed.add_field(name='‏‏‎ ‎\nKiss', value='Kiss an user\n =kiss @user')
            embed.add_field(name='‏‏‎ ‎\nSlap', value='Slaps an user\n =slap @user')
            embed.add_field(name='‏‏‎ ‎\nCry', value='Cry...\n =cry')
            embed.add_field(name='‏‏‎ ‎\nHighfive', value='Highfive an user\n =highfive @user')
            embed.add_field(name='‏‏‎ ‎\nBurn', value='Burn an object\n =burn object')
            embed.add_field(name='‏‏‎ ‎\nCuddle', value='Cuddles with an user\n =cuddle @user')
            embed.add_field(name='‏‏‎ ‎\nCheer', value='Cheers up an user\n =cheer @user')
            embed.add_field(name='‏‏‎ ‎\nScare', value='Scares an user\n =scare @user')
            embed2.add_field(name='‏‏‎Punch', value='Punches an user\n =bite @user')
            embed2.add_field(name='‏‏‎Kill', value='Kills an user and starts an event\n=kill @user')
            embed2.add_field(name='‏‏‎Dropkick', value='Dropkicks an user\n=dropkick @user')
            embed2.add_field(name='‏‏‎ ‎\nMarry', value='Propose to the love of your live\n=marry @user')
            embed2.add_field(name='‏‏‎ ‎\nDivorce', value='Divorce your signifcant other\n=divorce @user')
            embed2.add_field(name='‏‏‎ ‎\nMarriages', value="Check who you're married to\n=marriages")
            embed2.add_field(name='‏‏‎ ‎\nLeaderboard', value="Show the point leaderboard\n=lb")
            embed2.add_field(name='‏‏‎ ‎\nShow Points', value="Check how many points you or an user has\n=points / =points @user")
            embed2.add_field(name='‏‏‎ ‎\nGive Points', value="Give your points to an user\n=give @user (amount of points)")
            return embed, embed2

        if value == "mod":
            pass


        if value == "admin":
            embed = discord.Embed(title='List of Admin Commands', color=65535)
            embed.add_field(name='Setup', value='Sets up the bot\n=setup')
            embed.add_field(name='Set Mod Role', value='Sets the server mod role\n=modrole @role')
            embed.add_field(name='Add Moderator', value='Adds the mod role to an user\n =addmod @user')
            embed.add_field(name='‏‏‎ ‎\nRemove Moderator', value='Removes the mod role from an user\n=delmod @user')
            embed.add_field(name='‏‏‎ ‎\nSet Users Points', value='Sets an users points\n=setpoints @user (amount of points)')
            return embed





    @commands.command()
    async def help(self, ctx):
        await ctx.send(
            embed=discord.Embed(title=f'{ctx.author.name}, please select commands', color=65535),
            components=[
                Select(
                    placeholder="Select Commands",
                    options=[
                        SelectOption(emoji='🎉', label="Fun Commands", value="List of Fun Commands"),
                        SelectOption(emoji='🛠', label="Mod Commands", value="List of Moderator Commands"),
                        SelectOption(emoji='🔒', label="Admin Commands", value="List of Admin Commands"),
                    ],
                )
            ],
        )
        
        res = await self.client.wait_for("select_option")

        if res.component[0].label == 'Fun Commands':
            embed1, embed2 = self.embeds("fun")
            await res.author.send(embed=embed1); await res.author.send(embed=embed2)
            await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{res.author.mention} commands sent to dm's")


        if res.component[0].label == 'Mod Commands':
            await res.author.send(embed=self.embeds("mod"))
            await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{res.author.mention} commands sent to dm's")

        
        if res.component[0].label == 'Admin Commands':
            await res.author.send(embed=self.embeds("admin"))
            await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{res.author.mention} commands sent to dm's")


            
            
            


def setup(client):
    client.add_cog(Help(client))

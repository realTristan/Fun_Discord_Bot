import discord, os, json
from discord.ext import commands
from discord.ext.commands import CommandNotFound, CommandInvokeError
import datetime as datetime
from discord_components import *


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='=', intents=intents)
client.remove_command('help')


def write(file, data, f):
    with open('json\\data.json','w') as f:
        json.dump(data, f, indent=4)
        f.close()


@client.event
async def on_ready():
    DiscordComponents(client)
    print(f'Launched: {client.user.name} // {client.user.id}')


@client.event
async def on_member_join(member):
    with open('json\\data.json','r+') as f:
        data=json.load(f)
        data[str(member.guild.id)]["users"].update({
            f"{member.id}" : {
                "marriages": [],
                "points": 0

            }
        })
        write('data', data, f)



@client.command(description="Loads an extention")
@commands.has_permissions(administrator=True)
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f"**Loaded {extention}**", delete_after=2)

@client.command(description="Unloads an extention")
@commands.has_permissions(administrator=True)
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    await ctx.send(f"**Unloaded {extention}**", delete_after=2)

@client.command(description="Reloads an extention")
@commands.has_permissions(administrator=True)
async def reload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f"**Reloaded {extention}**", delete_after=2)

for filename in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cogs')):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded: cog.{filename[:-3]}')





client.run('YOUR TOKEN')

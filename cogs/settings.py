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
                    "commands" : {
                        "kill_command": {
                            "kill_timer": 0
                        }
                    },
                    "users" : {

                    }
                })

        self.write('data', data, f)


    # Giving points for every message / image they send
    @commands.Cog.listener()
    async def on_message(self, message):
        with open(os.path.dirname(__file__) + '\\..\\json\\data.json','r+') as f:
            data=json.load(f)
            if not message.attachments:
                data[str(message.guild.id)]["users"][str(message.author.id)]["points"] += 0.25
            elif message.attachments:
                data[str(message.guild.id)]["users"][str(message.author.id)]["points"] += 0.5

            self.write('data', data, f)





def setup(client):
    client.add_cog(Settings(client))

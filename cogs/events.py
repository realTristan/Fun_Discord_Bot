import discord, os, os.path, json, asyncio, random
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client







def setup(client):
    client.add_cog(Events(client))

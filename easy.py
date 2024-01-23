# easy.py

from utils import bot_ban
import discord
from discord.ext import commands

class EasyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    async def ban_user(self, ctx, user: discord.User):
        """Ban a user using a simplified command."""
        await bot_ban(ctx.guild, user, ctx)



print("discord.py-easy is working!")

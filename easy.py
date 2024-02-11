# easy.py

from utils import bot_ban
from utils import bot_kick
from utils import bot_mute
from utils import ui_send
import discord
from discord.ext import commands
from asyncio import sleep

print("discord.py-easy is working!")

class EasyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(name='ban')
    @commands.has_permissions(ban_members = True)
    async def ban_user(self, ctx, user: discord.User, reason="Banned by a moderator/admin"):
        """Ban a user using a simplified command."""
        await bot_ban(ctx.guild, user, reason)
    @commands.command(name='kick')
    @commands.has_permissions(kick_members = True)
    async def kick_user(self, ctx, user: discord.User):
        """Kick a user using a simplified command."""
        await bot_kick(ctx.guild, user, ctx)

    @commands.command(name='mute')
    @commands.has_permissions(mute_members = True)   
    async def mute(self, guild, user, ctx, duration):
        await bot_mute(ctx.guild, user, ctx, duration)

    @commands.command(name="userinfo")
    async def ui(ctx, member: discord.Member = None):
        await ui_send(ctx, member)



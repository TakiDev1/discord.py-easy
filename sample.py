# bot.py

import discord
from discord.ext import commands
from utils import bot_ban
from utils import bot_kick
from utils import bot_mute
from utils import ui_send


# Create a bot instance
bot = commands.Bot(command_prefix=',', intents = discord.Intents.all())

@bot.command(name='ban')
@commands.has_permissions(ban_members = True) 
async def ban(ctx, user: discord.User, reason="Banned by a moderator/admin"):
    """Ban a user using a simplified command."""
    await bot_ban(ctx.guild, user, reason, ctx)
# Kick and Mute commands from the easy module
@bot.command(name='kick')
@commands.has_permissions(kick_members = True) 
async def kick_user(ctx, user: discord.User):
    """Kick a user using a simplified command."""
    await bot_kick(ctx.guild, user, ctx)

@bot.command(name='mute')
@commands.has_permissions(mute_members = True) 
async def mute_user(ctx, user: discord.User):
    """Mute a user using a simplified command."""
    await bot_mute(ctx.guild, user, ctx)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print(f'Guilds: {len(bot.guilds)}')
    print('------')
    print("discord.py-easy is working!")

@bot.command(name="ui")
async def userinfo(ctx, member: discord.Member = None):
    await ui_send(ctx, member)

# Other bot setup code...


# Run the bot
bot.run('TOKEN')

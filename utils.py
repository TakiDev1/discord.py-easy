# utils.py

import discord
from discord.ext import commands


async def bot_ban(guild, user):
    """Ban a user using a custom method."""
    try:
        await guild.ban(user)
        print(f"{user.name} has been banned.")
    except discord.Forbidden:
        print("Bot doesn't have the 'Ban Members' permission.")
    except discord.HTTPException as e:
        print(f"An error occurred: {e}")


print("Utils loaded")

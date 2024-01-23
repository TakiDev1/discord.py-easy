import discord
from discord.ext import commands
from easy import bot_ban

# Create a bot instance
bot = commands.Bot(command_prefix='!')

@bot.command(name='ban')
async def ban_user(ctx, user: discord.User):
    await bot_ban(ctx.guild, user)

# Other bot setup code...

# Run the bot
bot.run('YOUR_BOT_TOKEN')

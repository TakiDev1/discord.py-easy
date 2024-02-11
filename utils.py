# utils.py

import discord
from discord.ext import commands
from asyncio import sleep

print("Utils loaded")

async def bot_ban(guild, user, reason, ctx):
    """Ban a user using a custom method."""
    try:
        await guild.ban(user, reason=reason)
        await ctx.send(f"{user.name} has been banned!")
        print(f"{user.name} has been banned.")
    except discord.Forbidden:
        print("Bot doesn't have the 'Ban Members' permission.")
    except discord.HTTPException as e:
        print(f"An error occurred: {e}")


async def bot_kick(guild, user, ctx):
    """Kick a user using a custom method."""
    try:
        await guild.kick(user)
        await ctx.send(f"{user.name} has been kicked!")
        print(f"{user.name} has been kicked.")
    except discord.Forbidden:
        print("Bot doesn't have the 'Kick Members' permission.")
    except discord.HTTPException as e:
        print(f"An error occurred: {e}")


async def bot_mute(guild, user, ctx, duration):
        """Mute a user with a specified timeout."""
        # Implement mute logic
        muted_role = discord.utils.get(guild.roles, name="Muted")

        if not muted_role:
            # If the Muted role doesn't exist, create it
            muted_role = await guild.create_role(name="Muted", reason="Creating Muted role for muting users")
            for channel in guild.channels:
                await channel.set_permissions(muted_role, send_messages=False)

        await user.add_roles(muted_role)
        await ctx.send(f"{user.name} has been muted for {duration} seconds!")

        # Wait for the specified duration and then unmute the user
        await sleep(duration)
        await user.remove_roles(muted_role)
        await ctx.send(f"{user.name} has been unmuted after {duration} seconds.")


async def ui_send(ctx, member):
    member = member or ctx.message.author
    embed = discord.Embed(title=f"{member.name}'s Information", color=0x00ff00)
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Display Name", value=member.display_name, inline=False)
    embed.add_field(name="Account Created At", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    embed.add_field(name="Joined Server At", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        
    await ctx.send(embed=embed)



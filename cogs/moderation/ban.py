from discord.ext import commands
import discord

from utils.time import FutureTime
from utils.responses import generate_error
from database.punishments import insert_punishment
from typing import Union

import time


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, duration: Union[FutureTime, None] = None, *, reason: Union[str, None] = None):

        if member == ctx.author:
            return await generate_error(ctx, "You can't ban yourself, lol.")

        reason = reason or "Unspecified"

        seconds_til_unban = f"{duration.dt.timestamp() - time.time()}," if duration is not None else ""
        # execute_sql(
        #     f"""
        #     INSERT INTO punishments (
        #         user_id,
        #         moderator_id,
        #         guild_id,
        #         punishment_type,
        #         reason,
        #         punished_at,
        #         {'duration,' if duration is not None else ''}
        #         permanent) VALUES (
        #         {member.id},
        #         {ctx.author.id},
        #         {ctx.channel.guild.id},
        #         'ban',
        #         '{reason}',
        #         'now',
        #         {str(round(seconds_til_unban)) + "," if seconds_til_unban is not False else ','}
        #         {'true' if duration is None else 'false'});"""
        # )
        await insert_punishment(
            user_id=member.id,
            moderator_id=ctx.author.id,
            guild_id=ctx.guild.id,
            punishment_type='ban',
            reason=reason,
            duration=seconds_til_unban,
            permanent=duration is None
        )

        try:
            await ctx.guild.ban(member, reason=reason)
        except (AttributeError, discord.HTTPException) as e:
            print(e)

    @ban.error
    async def handle_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            return await generate_error(ctx, "You are missing the required permissions to ban members!")

        print(error)

    # @commands.command()
    # @commands.has_permissions(ban_members=True)
    # @bot.has_permissions(ban_members=True)
    # async def unban(self, ctx, member)


def setup(client):
    client.add_cog(Ban(client))

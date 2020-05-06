import discord
from discord.ext import commands
import asyncio


class ModCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.bot_has_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def kick_command(self, ctx, target: discord.Member=None, res = ''):
        """Command which can kick members of a guild"""
        if target is None:
            await ctx.send('Mention someone')
        else:
            try:
                await target.kick(reason=res)
                await ctx.send(f'I kicked {target.name} from this guild.')
            except discord.Forbidden:
                await ctx.send('Could not kick user. Not enough permissions.')

    @commands.command(name='ban')
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def ban_command(self, ctx, target: discord.Member=None, res = ''):
        """Command which can ban members of a guild"""
        if target is None:
            await ctx.send('Mention someone')
        else:
            try:
                await target.ban(reason=res)
                await ctx.send(f'I banned {target.name} from this guild.')
            except discord.Forbidden:
                await ctx.send('Could not ban user. Not enough permissions.')

    @commands.command(name='clear')
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def clear_command(self, ctx, number: int):
        """Command which can delete messages in a text channel"""
        if number is None:
            await ctx.send('Number required')
        else:
            try:
                await ctx.channel.purge(limit=number + 1)
                clear_message = await ctx.send(f'Deleted {number} messages.')
                await asyncio.sleep(5)
                await clear_message.delete()
            except discord.Forbidden:
                await ctx.send('Could not delete messages. Not enough permissions.')

def setup(bot):
    bot.add_cog(ModCommands(bot))
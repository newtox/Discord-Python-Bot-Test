import  discord
from discord.ext import commands


class OwnerCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Hidden means it won't show up on the default help.
    @commands.command(name='load')
    @commands.is_owner()
    async def load_cog(self, ctx, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'`ERROR:` {type(e).__name__} - {e}')
        else:
            await ctx.send('`SUCCESS`')

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload_cog(self, ctx, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'`ERROR:` {type(e).__name__} - {e}')
        else:
            await ctx.send('`SUCCESS`')

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload_cog(self, ctx, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'`ERROR:` {type(e).__name__} - {e}')
        else:
            await ctx.send('`SUCCESS`')

def setup(bot):
    bot.add_cog(OwnerCommands(bot))
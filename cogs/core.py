import discord
from discord.ext import commands


class CoreCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test')
    async def test_command(self, ctx):
        """Command which is a basic text command"""
        await ctx.send('yo, this is a test!')

    @commands.command(name='embeds')
    async def embed_command(self, ctx):
        """Command which sends an embed message"""
        embed = discord.Embed(
            title='This is the title of an embed',
            description='Description yo',
            color=discord.Color.blurple()
        )
        embed.add_field(name='Field', value='Placeholder for a value', inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='say')
    async def say_command(self, ctx, words=None):
        """Command which makes the bot to repeat your words"""
        try:
            if words is None:
                await ctx.send('Please provide some arguments')
            else:
                try:
                    await ctx.message.delete()
                    await ctx.send(words)
                except discord.Forbidden:
                    await ctx.send('I got not enough permissions.')
        except Exception as e:
            await ctx.send(f'`ERROR:` {type(e).__name__} - {e}')

    @commands.command(name='memberinfo')
    async def memberinfo_command(self, ctx, target: discord.Member=None):
        """Command which gives you information about yourself or a member of your current guild"""
        roles = ''
        perms = ''
        if target is None:
            target = ctx.author
        embed = discord.Embed(
            color=discord.Color.blurple(),
            title=(f'Userinfo about {target.name}')
        )
        embed.set_thumbnail(url=target.avatar_url)
        embed.add_field(name='Id', value=f'{target.id}', inline=False)
        embed.add_field(name='Username', value=f'{target.name}', inline=False)
        embed.add_field(name='Joined Guild', value=target.joined_at.strftime('%d/%m/%Y %H:%M:%S'), inline=False)
        embed.add_field(name='Account Created', value=target.created_at.strftime('%d/%m/%Y %H:%M:%S'), inline=False)
        for role in target.roles:
            if not role.is_default():
                roles += f'{role.mention}\r\n'
        if roles:
            embed.add_field(name='Roles', value=roles, inline=False)
        perms += ', '.join(perm for perm, value in target.guild_permissions if value)
        embed.add_field(name='Perms', value=perms, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='guildinfo')
    @commands.guild_only()
    async def guildinfo_command(self, ctx):
        """Command which gives you information about your current guild"""
        guild = None
        if guild is None:
            guild = ctx.message.guild
        embed = discord.Embed(
            color=discord.Color.dark_magenta(),
            title=f'Guild: {guild.name}'
        )
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name='Id', value=guild.id, inline=False)
        embed.add_field(name='Region', value=guild.region, inline=False)
        embed.add_field(name='Guild Owner', value=guild.owner.mention, inline=False)
        embed.add_field(name='Verification Level', value=guild.verification_level, inline=False)
        embed.add_field(name='Membercount', value=guild.member_count, inline=False)
        embed.add_field(name='Number of roles', value=len(guild.roles), inline=False)
        embed.add_field(name='Number of emotes', value=len(guild.emojis), inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(CoreCommands(bot))

import discord
from discord.ext import commands
import asyncio


# This function will change the status every 30 seconds.

async def status_change():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Python Bot'), status=discord.Status.dnd)
    await asyncio.sleep(30)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='cogs'), status=discord.Status.online)

# Prefix for the bot. Mention is working too.

def get_prefix(client, message):
    prefixes = ['!', '?', '_', ':', 't!']

    return commands.when_mentioned_or(*prefixes)(client, message)

# Adding cogs

initial_extensions = ['cogs.core', 'cogs.moderation', 'cogs.owner']

client = commands.Bot(command_prefix=get_prefix)

# Load extensions (cogs)

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

@client.event
async def on_ready():

    print(f'\n\nLogged in as: {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\n')

    # Set activity.

    # Basic Status
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='with code'), status=discord.Status.online)
    await client.loop.create_task(status_change())
    print(f'Successfully logged in and booted...!')

client.run('TOKEN', bot=True, reconnect=True)
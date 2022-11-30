# Imports
import asyncio, os, config
import discord
from discord.ext import commands

# Intents & Prefix
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
  command_prefix = '.',
  intents = intents
)

# Events
@bot.event
async def on_ready():
  print('Bot is now online!\n---------------------')

# Loading Cog
async def load():
  for folder in os.listdir(f'./commands/.'):
    for filename in os.listdir(f'./commands/{folder}/.'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{folder}.{filename[:-3]}')

# To run the bot
async def main():
  await load()
  await bot.start(config.token)

asyncio.run(main())
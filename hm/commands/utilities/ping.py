import discord
from discord.ext import commands
from discord import app_commands

class Ping(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('Cog: Ping cog has been loaded.')
  
  @app_commands.command(
    name = 'ping',
    description = 'Sends the bot latency.',
  )
  async def ping(self, interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! 🏓 `{round(self.bot.latency * 1000)}ms`')

async def setup(bot):
  await bot.add_cog(Ping(bot), guild = discord.Object(id = 1038406073054404658))
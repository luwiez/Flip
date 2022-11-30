import discord, asyncio, config
from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord.app_commands import AppCommandError


class Handler(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

    bot.tree.on_error = self.on_app_command_error

  @commands.Cog.listener()
  async def on_ready(self):
    print('Cog: Error cog has been loaded.')
  
  async def on_app_command_error(self, interaction: Interaction, error: AppCommandError):
    if isinstance(error, app_commands.MissingRole):
      embed = discord.Embed(
        title = 'Flip - Error',
        description = '**Missing Roles!**' + '\n' + '> Required role(s): <@&1038408626928357437>',
        color = 0xffffff
      )  
      embed.set_footer(
          text = 'Flip - Predictor'
        )
      await interaction.response.defer()
      await asyncio.sleep(1.5)
      await interaction.followup.send(embed = embed)
    else: raise error

async def setup(bot):
  await bot.add_cog(Handler(bot))

from discord.ext import commands
from discord import app_commands
from random import randint
import discord, config, asyncio, random

class Towers(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('Cog: Towers cog has been loaded.')

  @app_commands.command(
    name = 'ptowers',
    description = 'Sends a premium towers prediction.'
  )
  @app_commands.describe(
    spots = 'How many spots do you want me to predict?',
    hash = 'Please put your current game server-hash.'
  )
  @app_commands.rename(hash = "server-hash")
  @app_commands.checks.has_role('buyer')
  async def towers(self, interaction: discord.Interaction, spots: int, hash: str):
    if spots < 1:
      embed = discord.Embed(color = 0xffffff, title = 'Flip - Error', description = '**Spots can\'t be less than 1!**\n> Spots can be only between 1 - 8!')
      embed.set_footer(
        text = 'Flip - Predictor'
      )
      await interaction.response.defer()
      await asyncio.sleep(1.5)
      await interaction.followup.send(embed = embed)
      
    if spots > 8: 
      embed = discord.Embed(color = 0xffffff, title = 'Flip - Error', description = '**Spots can\'t be more than 8!**\n> Spots can be only between 1 - 8!')
      embed.set_footer(
        text = 'Flip - Predictor'
      )
      await interaction.response.defer()
      await asyncio.sleep(1.5)
      await interaction.followup.send(embed = embed)
    if len(hash) == 64:
      grid = [['❌ ','❌ ','❌ '],['❌ ','❌ ','❌ '],['❌ ','❌ ','❌ '],['❌ ','❌ ','❌ '],['❌ ','❌ ','❌ '],['❌ ','❌ ','❌ '],['❌ ','❌ ','❌ '],['❌ ','❌ ','❌ ']]

      count = 0
      while count < spots:
          a = randint(0,2)
          grid[count][a] = '⭐ '
          count += 1

      chance = randint(45,95)
      if spots < 4:
              chance = chance - 15

      em = discord.Embed(color=0x0025ff, title = 'Flip - Predictor', description = 'Using a __random server-hash__ will make a __random prediction__.' + "\n" + "**Thanks for purchasing our paid predictor! Your prediction is right below this message.**")
      em.add_field(name='🌟 — Paid Plan ', value="```"+grid[7][0]+grid[7][1]+grid[7][2]+"\n"+grid[6][0]+grid[6][1]+grid[6][2]+"\n"+grid[5][0]+grid[5][1]+grid[5][2]+"\n"+grid[4][0]+grid[4][1]+grid[4][2] +"\n"+ \
            grid[3][0]+grid[3][1]+grid[3][2] + "\n" + grid[2][0]+grid[2][1]+grid[2][2] + "\n" + grid[1][0]+grid[1][1]+grid[1][2] + "\n" + grid[0][0]+grid[0][1]+grid[0][2] + "```" )
        
      em.add_field(
        name = '🔮 — Requested by',
        value = '\n```' + interaction.user.name + '#' + interaction.user.discriminator + '```\n'
      )
    
      em.set_footer(
        text = 'Flip - Predictor'
      )
      await interaction.response.defer()
      await asyncio.sleep(1.5)
      await interaction.followup.send(embed=em)
    else: 
      em = discord.Embed(color=0xffffff, title = 'Flip - Error', description = '**Server-hash invalid!**\n> Please put a valid server-hash.')
      em.set_footer(
        text = 'Flip - Predictor',
      )
      await interaction.response.defer()
      await asyncio.sleep(1.5)
      await interaction.followup.send(embed = em)

async def setup(bot):
  await bot.add_cog(Towers(bot), guild = discord.Object(id = 1038406073054404658))
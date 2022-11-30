import discord, random, config
import asyncio
from discord.ext import commands
from discord import app_commands

class Mines(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('Cog: Mines cog has been loaded.')

  @app_commands.command(name = 'pmines', description = 'Sends a premium mines prediction.')
  @app_commands.describe(spots = 'How many spots do you want me to predict?', hash = 'Please put your current game server-hash.')
  @app_commands.checks.has_role('buyer')
  @app_commands.rename(hash = 'server-hash')
  async def mines(self, interaction: discord.Interaction, spots: int, hash : str):
    if spots < 1:
      embed = discord.Embed(color = 0xffffff, title = 'Flip - Error', description = '**Spots can\'t be less than 1!**\n> Spots can be only between 1 - 24!')
      embed.set_footer(
        text = 'Flip - Predictor'
      )
      await interaction.response.defer()
      await asyncio.sleep(1.5)
      await interaction.followup.send(embed = embed)
      
    if spots > 24: 
      embed = discord.Embed(color = 0xffffff, title = 'Flip - Error', description = '**Spots can\'t be more than 24!**\n> Spots can be only between 1 - 24!')
      embed.set_footer(
        text = 'Flip - Predictor'
      )
      await interaction.response.defer()
      await asyncio.sleep(1.5)
      await interaction.followup.send(embed = embed)
    if len(hash) == 64: 
      grid = ['💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ','💣 ']
      already_used = []

      count = 0
      while spots > count:
        a = random.randint(0, 24)
        if a in already_used:
          continue
        already_used.append(a)
        grid[a] = '⭐ '
        count += 1
        
      chance = random.randint(45,95)
      if spots < 4:
        chance = chance - 15

      em = discord.Embed(color=0xffffff, title = 'Flip - Predictor', description = 'Using a __random server-hash__ will make a __random prediction.' + "\n" + "**Thanks for purchasing our paid predictor! Your prediction is right below this message.**")
      em.add_field(name='🌟 — Paid Plan ', value="\n" + "```"+grid[0]+grid[1]+grid[2]+grid[3]+grid[4]+"\n"+grid[5]+grid[6]+grid[7]+grid[8]+grid[9]+"\n"+grid[10]+grid[11]+grid[12]+grid[13]+grid[14]+"\n"+grid[15]+grid[16]+grid[17] \
            +grid[18]+grid[19]+"\n"+grid[20]+grid[21]+grid[22]+grid[23]+grid[24] + "```\n",inline=False)
      em.add_field(
        name = '🔮 — Requested by',
        value = '\n```' + interaction.user.name + '#' + interaction.user.discriminator + '```\n', inline=False
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
        text = 'Flip - Predictor'
      )
      await interaction.response.defer()
      await asyncio.sleep(1.5)
      await interaction.followup.send(embed = em)

async def setup(bot):
  await bot.add_cog(Mines(bot), guild = discord.Object(id = 1038406073054404658))
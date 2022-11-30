import discord, asyncio, config
from discord.ext import commands
from discord import app_commands

class Plans(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('Cog: Plans cog has been loaded.')

  @app_commands.command(
    name = 'plans', 
    description = 'Sends Flip Predictor Paid Plans.'
  )
  async def plans(self, interaction: discord.Interaction):
    plans = discord.Embed(
      color = 0xffffff,
      title = 'Flip - Predictor',      
      description = 'Buying the paid predictor will give you more benifits and also to help us developers.' + '\n' + '\n'+ 'Paid Predictor Plans: ' + '\n' + '__Paypal & Bloxflip__ ↓' + '\n' + '**✨ Monthly Plan** —' + '\n' + '650 bloxflip tip / $3 paypal' + '\n' + '\n' + '**🌟 Lifetime Plan** —' + '\n' + '1 000 bloxflip tip / $5 paypal' + '\n' + '\n' + '__Nitro & Boosts__ ↓' + '\n' + '**1 Month Nitro Boost Gift —**' + '\n' + '1 Month Plan' + '\n' + '**Server Boost**' + '\n' + '*How long you boost = how long you will also get paid plan*' + '\n' + '\n' + 'Please make sure to read #faq before buying!'
    )
    plans.set_footer(
        text = 'Flip - Predictor'
      )
    
    await interaction.response.defer()
    await asyncio.sleep(1.5)
    await interaction.followup.send(embed = plans)

async def setup(bot):
  await bot.add_cog(Plans(bot), guild = discord.Object(id = 1038406073054404658))
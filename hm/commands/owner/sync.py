import discord, config
from discord.ext import commands

class Sync(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('Cog: Sync cog has been loaded.')

  @commands.command()
  async def sync(self, ctx) -> None:
    if ctx.message.author.id == 928309791879741470:
      fmt = await ctx.bot.tree.sync(guild = ctx.guild)
      embed = discord.Embed(
        title = 'Flip - Success',
        description = f'**Synced {len(fmt)} commands.**',
        color = 0xffffff
      )
      await ctx.reply(embed = embed)
    else: 
      embed = discord.Embed(
        title = 'Flip - Error',
        description = '**You are not the owner!**' + '\n' + '> Required role(s): <@&1038416172900692078>',
        color = 0xffffff
      )
      
      await ctx.reply(embed = embed)

async def setup(bot):
  await bot.add_cog(Sync(bot))
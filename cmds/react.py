import discord
from discord.ext import commands
import json
import random
from core.classes import Cog_Extension
    
class Main(Cog_Extension):
    #傳送延遲指令
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'真是太遜了!目前延遲:{round(self.bot.latency*1000)}毫秒')

def setup(bot):
    bot.add_cog(Main(bot))

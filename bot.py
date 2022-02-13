import discord
from discord.ext import commands
import os

TOKEN = os.environ['TOKEN']
JOIN = os.environ['JOIN']
LEAVE = os.environ['LEAVE']

intents = discord.invite.all()

bot = commands.bot(commands_prefix='//',intents = intents)

@bot.event
async def on_ready():
    print("準備完成")
#成員加入
@bot.event
async def on_memer_join(member):
    channel = bot.get_channel(JOIN)
    await channel.send(f'阿呦~這麼好喔 {member} 加入了~!')
#成員離開
@bot.event
async def on_memer_join(member):
    channel = bot.get_channel(LEAVE)
    await channel.send(f'阿呦~ {member} 離開了~真是太遜了~')

@bot.command()
async def ping(ctx):
    await ctx.send(f'這次不開玩笑了 目前延遲:{round(bot.latency*1000)}毫秒')

bot.run(TOKEN)
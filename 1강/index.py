import discord
from discord.ext import commands

token = "봇토큰"

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('봇이 켜졌습니다.')
    
@bot.command()
async def 핑(ctx):
    await ctx.send('퐁!')

bot.run(token)

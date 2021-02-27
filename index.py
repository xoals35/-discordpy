import discord
from discord.ext import commands

token = "ODE1MTYxNzg0NDMxOTM1NTIw.YDoYkg.iReWBC96vjuf91uwUEFiQUtMN3g"

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('봇이 켜졌습니다.')
    
@bot.command()
async def 핑(ctx):
    await ctx.send('퐁!')

bot.run(token)
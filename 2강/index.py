import discord
from discord.ext import commands
import random

token = "ODE1MTYxNzg0NDMxOTM1NTIw.YDoYkg.35EHbixKvX-e1rff8dSvsY6XTtA"

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('봇이 켜졌습니다.')
    
@bot.command(name="핑", help="핑을 보여줌")
async def ping(ctx):
        pings = round(bot.latency*1000)
        if pings < 100:
            pinglevel = '🔵 매우좋음'
        elif pings < 300: 
            pinglevel = '🟢 양호함'
        elif pings < 400: 
            pinglevel = '🟡 보통'
        elif pings < 6000: 
            pinglevel = '🔴 나쁨'
        else: 
            pinglevel = '⚪ 매우나쁨'
        embed = discord.Embed(title='핑', description=f'{pings} ms\n{pinglevel}')
        await ctx.send(embed=embed)

@bot.command()
async def 뽑기(ctx):
        await ctx.trigger_typing()
        randomNum = random.randrange(1, 3)
        if randomNum == 1:
            await ctx.send('당첨')
        if randomNum == 2:
            await ctx.send('꽝')

@bot.command()
async def 밴(ctx, user: discord.User):
	guild = ctx.guild
	mbed = discord.Embed(
		title = '밴 시퀸스 작동알림',
		description = f"{user}님이 밴을 당하셨어요!"
	)
	if ctx.author.guild_permissions.ban_members:
		await ctx.send(embed=mbed)
		await guild.ban(user=user)



@bot.command()
@commands.has_permissions(kick_members=True)
async def 킥(ctx, member:discord.Member):
    if ctx.author.guild_permissions.ban_members:
        await member.kick()
        await ctx.send(f"{member.name}님을 킥했습니다.")



bot.run(token)
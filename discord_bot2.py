from dis import disco
import discord,asyncio,os
from discord.ext import commands
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

game = discord.Game("명령어를 칠려면 !를 쓰세요")
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity=game)

@bot.command(aliases=['안녕', 'hi', '안녕하세요'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 안녕하세요!')

@bot.command(name='관리자')
async def mangerCheck(ctx):
    if ctx.guild:
        if ctx.message.author.guild_permissions.administrator:
            await ctx.send('이 서버의 관리자입니다.')
        else:
            await ctx.send('이 서버의 관리자가 아닙니다.')
    else:
        await ctx.send('DM으론 불가능합니다.')

@bot.command()
async def 인증(ctx):
    await ctx.send(f'{ctx.author.mention}인증 되셨습니다.')

@bot.command()
async def 정보(ctx):
    members = [member.name for member in ctx.guild.members]
    await ctx.send(
        "{} 서버는 {} 서버이며 구성원은 {} 이고 총 {} 명입니다.".format(
            ctx.guild.name, 
            ctx.guild.region, 
            members, 
            ctx.guild.member_count
        )
    )

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        await member.guild.system_channel.send(
            "{}님이 보이스 채널에 접속했습니다.".format(member.name)
        )

@bot.command(aliases=['주사위','r'])
async def roll(ctx, number:int):
    await ctx.send(f'주사위를 굴려 {random.randint(1,int(number))}이(가) 나왔습니다 (1~{number})')
@roll.error
async def roll_error(ctx,error):
    await ctx.send('명령어 오류!!!')

@bot.command()
async def repeat(ctx, *, txt):
    await ctx.send(txt)

@bot.command(aliases=['계산기','계산'])
async def calculate(ctx):
    await ctx.send(f'{ctx.author.mention}계산할 수를 쓰세요')
    x=int
    await ctx.send(f'{ctx.author.mention}사칙연산 또는 제곱을 쓰세요')
    y=ctx
    if y=='곱셈':
        ctx.send(f'{ctx.author.mention}계산할 수(2)를 쓰세요')
        z=int(ctx)
        result=x*z
        ctx.send(f'{ctx.author.mention}결과는 {result}입니다.')
    elif y=='나눗셈':
        ctx.send(f'{ctx.author.mention}계산할 수(2)를 쓰세요')
        z=int(ctx)
        result=x/z
        ctx.send(f'{ctx.author.mention}결과는 {result}입니다.')
    elif y=='뺄셈':
        ctx.send(f'{ctx.author.mention}계산할 수(2)를 쓰세요')
        z=int(ctx)
        result=x-z
        ctx.send(f'{ctx.author.mention}결과는 {result}입니다.')
    elif y=='덧셈':
        ctx.send(f'{ctx.author.mention}계산할 수(2)를 쓰세요')
        z=int(ctx)
        result=x+z
        ctx.send(f'{ctx.author.mention}결과는 {result}입니다.')
    elif y=='제곱':
        await ctx.send(f'{ctx.author.mention}계산할 수(2)를 쓰세요')
        z=int(ctx)
        result=pow(x,z)
        ctx.send(f'{ctx.author.mention}결과는 {result}입니다.')
    else:
        await ctx.send(f'{ctx.author.mention} 잘못 되었으니 다시 실행 시켜주세요.')

async def on_member_join(member):
#on_member_join (유저가 서버에 처음 들어왔을때 발생하는 이벤트입니다.)
    await member.send("어서오세요. 저희 서버에 오신 것을 환영합니다.") 
    #member 매개변수로 처음 들어온 유저의 정보를 받아와 member.send로 해당 유저에게 메세지를 보냅니다.

@bot.event
async def on_message(message): # 메세지가 채널에 올라왔을 때 (해당 매세지)
    b=['ㅅㅂ','ㅄ','ㅂㅅ','씨발','시발','병신','ㅁㅊ','미친','꺼져','새끼','fuck']
    message_content = message.content # 메세지 내용을 message_content라는 변수에 담고
    for i in b:
        bad = message_content.find(i)
        if bad >= 0:
            await message.channel.send("바른말 고운말을 사용합시다.") 
            # 봇이 메세지가 올라온 채널에 해당 메세지를 전송하고
            await message.delete() # 욕설이 담긴 메세지를 삭제합니다.
            break
        await bot.process_commands(message)
'''
    bad = message_content.find("ㅄ")
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    bad = message_content.find("ㅂㅅ")
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    bad = message_content.find("병신")
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    bad = message_content.find("ㅁㅊ")
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    bad = message_content.find("미친")
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    bad = message_content.find("시발")
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    bad = message_content.find("fuck")
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    bad = message_content.find("새끼")
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    bad = message_content.find("씨발")
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message) # 메세지 중 명령어가 있을 경우 처리해주는 코드
'''
@bot.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")

@bot.command(aliases=['도움말', 'h'])
async def 도움(ctx):
    embed = discord.Embed(title="1번째 봇", description="Official Bot for Discord by 1이란", color=0x4432a8)
    embed.add_field(name="1. 인사", value="!hello", inline=False)
    embed.add_field(name="2. 주사위", value="!roll [범위숫자]", inline=False)
    embed.add_field(name="3. 따라하기", value="!repeat [따라할 말]", inline=False)
    embed.add_field(name="4. 욕 밴", value="욕을 쓰면 삭제", inline=False)
    embed.add_field(name="5. 메세지 삭제", value="!clear [숫자(지울 량)]", inline=False)
    embed.add_field(name="6. 정보", value="!정보", inline=False)
    embed.add_field(name="7. 관리자인지 아닌지 확인", value="!관리자", inline=False)
    embed.add_field(name="8. 명령어 인식", value="명령어가 있는지 확인", inline=False)
    await ctx.send(embed=embed)
access_tocken=os.environ["BOT_TOCKEN"]
bot.run(access_token)

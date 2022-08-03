import asyncio, discord, datetime, pytz
import random
from discord.ext import commands
import os


client = discord.Client()
split_list = []
user_cnt = 0

@client.event
async def on_ready():
    print(f"{client.user.name} 활성화 완료")
    print("================================")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("네거티브 마인드 응원"))
    
@client.event
async def on_message(message): #사용자가 메세지 입력했을 때
    if message.content == "-": # 만약 사용자가 '-' 라고 입력했을 때        
        if message.author.mention in split_list:
            await message.channel.send(f"{message.author.mention}님은 이미 입력하셨습니다.")
        else:
            global user_cnt
            user_cnt += 1
            await message.channel.send(f"{message.author.mention}님 추가 완료. 현재 총원 {user_cnt}명")
            user_rand = random.randrange(0,user_cnt)
            split_list.insert(user_rand, message.author.mention)
        
    
#    elif message.content == f"- {user.mention}": 
#        await message.channel.send(f"{user.mention}님 추가 완료")
#        user_rand = random.randrange(0,user_cnt+1)
#        split_list.insert(user_rand, user.mention)
#        user_cnt += 1
         
          
    elif message.content == "=":
        await message.channel.purge(limit=999)
        
        embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
        embed.set_footer(text="Bot Made by. 동펭")
        
        if user_cnt <= 25:
            for i in range(user_cnt):
                embed.add_field(name=str(i+1) + '번째', value=f"{split_list[i]}", inline=True)
            await message.channel.send(embed=embed)
        elif user_cnt > 25 and user_cnt <=50:
            for i in range(25):
                embed.add_field(name=str(i+1) + '번째', value=f"{split_list[i]}", inline=True)
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-25):
                i_25 = i + 25
                embed.add_field(name=str(i_25+1) + '번째', value=f"{split_list[i_25]}", inline=True)                
            await message.channel.send(embed=embed)
        elif user_cnt > 50 and user_cnt <=75:
            for i in range(25):
                embed.add_field(name=str(i+1) + '번째', value=f"{split_list[i]}", inline=True)
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-25):
                i_25 = i + 25
                embed.add_field(name=str(i_25+1) + '번째', value=f"{split_list[i_25]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-50):
                i_50 = i + 50
                embed.add_field(name=str(i_50+1) + '번째', value=f"{split_list[i_50]}", inline=True)                
            await message.channel.send(embed=embed)
        elif user_cnt > 75 and user_cnt <=100:
            for i in range(25):
                embed.add_field(name=str(i+1) + '번째', value=f"{split_list[i]}", inline=True)
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-25):
                i_25 = i + 25
                embed.add_field(name=str(i_25+1) + '번째', value=f"{split_list[i_25]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-50):
                i_50 = i + 50
                embed.add_field(name=str(i_50+1) + '번째', value=f"{split_list[i_50]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-75):
                i_75 = i + 75
                embed.add_field(name=str(i_75+1) + '번째', value=f"{split_list[i_75]}", inline=True)                
            await message.channel.send(embed=embed)
        elif user_cnt > 100 and user_cnt <=125:
            for i in range(25):
                embed.add_field(name=str(i+1) + '번째', value=f"{split_list[i]}", inline=True)
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-25):
                i_25 = i + 25
                embed.add_field(name=str(i_25+1) + '번째', value=f"{split_list[i_25]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-50):
                i_50 = i + 50
                embed.add_field(name=str(i_50+1) + '번째', value=f"{split_list[i_50]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-75):
                i_75 = i + 75
                embed.add_field(name=str(i_75+1) + '번째', value=f"{split_list[i_75]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-100):
                i_100 = i + 100
                embed.add_field(name=str(i_100+1) + '번째', value=f"{split_list[i_100]}", inline=True)                
            await message.channel.send(embed=embed)
        elif user_cnt > 125 and user_cnt <=150:
            for i in range(25):
                embed.add_field(name=str(i+1) + '번째', value=f"{split_list[i]}", inline=True)
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-25):
                i_25 = i + 25
                embed.add_field(name=str(i_25+1) + '번째', value=f"{split_list[i_25]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-50):
                i_50 = i + 50
                embed.add_field(name=str(i_50+1) + '번째', value=f"{split_list[i_50]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-75):
                i_75 = i + 75
                embed.add_field(name=str(i_75+1) + '번째', value=f"{split_list[i_75]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-100):
                i_100 = i + 100
                embed.add_field(name=str(i_100+1) + '번째', value=f"{split_list[i_100]}", inline=True)                
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="정산", description= f"총원 - {user_cnt}명", timestamp=datetime.datetime.now(pytz.timezone('Asia/Seoul')), color=0x62c1cc)
            embed.set_footer(text="Bot Made by. 동펭")
            for i in range(user_cnt-125):
                i_125 = i + 125
                embed.add_field(name=str(i_125+1) + '번째', value=f"{split_list[i_125]}", inline=True)                
            await message.channel.send(embed=embed)
            
    elif '-----' in message.content:
        await message.channel.purge(limit=999)
        user_cnt = 0
        split_list.clear()
        await message.channel.send("리셋 완료")
        
access_token = os.environ["BOT_TOKEN"]     
client.run(access_token)

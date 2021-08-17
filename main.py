import discord 
import time 
import asyncpg
import discord
import os
import requests
import json
from discord.ext import commands, tasks
from itertools import cycle

#  with open ("data.json", "r") as f:
#      token = data["token"]

intents = discord.Intents().all()
client = commands.Bot(command_prefix="?", intents=intents, help_command=None, case_insensitive=True)
guild = discord.Guild

send_help = (commands.MissingRequiredArgument, commands.BadArgument, commands.TooManyArguments, commands.UserInputError)

client = commands.Bot(command_prefix='+')
status = cycle(['ortsero.com','Ortsero Bot'])

# =====================================VX
# This shit not working will review it 

@tasks.loop(seconds= 20)
async def change_status():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"ortsero"))

# =====================================


@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  channel = client.get_channel(871486709328662579)
  status = discord.Embed(title=f"Ortsero is :o2: :regional_indicator_n: " , color= 0x13fb41)
  await channel.send(embed=status)


# =====================================


@client.command()
async def ping(ctx):
    await ctx.send('pong')
    
# =====================================


@client.command()
async def clear(ctx,arg:int ):
  if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
   clear = discord.Embed(title=f":recycle:  Am sters {arg} de mesaje ", description=f"Sters de: {ctx.author.mention}")
   await ctx.channel.purge(limit = arg + 1 )
   await ctx.channel.send(embed=clear)
   time.sleep(3)
   await ctx.channel.purge(limit = 1)
# =====================================

# @clear.error
# async def clear_error(error, ctx):
#     if isinstance(error,discord.ext.commands.errors.MissingRequiredArgument):
#         await ctx.send("You didn't specify the amount of  text")




# =====================================
# KICK

@client.command(name="kick", pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)

# =====================================


# @kick.error
# async def kick_error(error, ctx):
#     if isinstance(error, send_help):
#         text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
#         await bot.send_message(ctx.message.channel, text)

# =====================================


@client.command(name="ban", pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boot: Baned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)

# =====================================


# @ban.error
# async def kick_error(error, ctx):
#     if isinstance(error, MissingPermissions):
#         text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
#         await bot.send_message(ctx.message.channel, text)

# ====================e=================
@client.event
async def on_command_error(ctx, error):
  
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Make sure you put the required arguments.')
        
#+=====================================

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
     try:
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename}')
     except Exception as e:
         print(f'Failed to load {filename}')
         print(f'[ERROR] {e}')

# =====================================


api = "&appid=15ace92fd4dc2d234ef8f160e7f24709"

@client.command(name="weather",pass_context=True)
async def weather(ctx, *, arg):
  response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={arg}{api}&lang=ro")
  var1 = response.json()['weather'][0]['main']
  var3 = response.json()['main']['temp']
  grade = (round(var3-273.15))
  var2 = discord.Embed(title=f":partly_sunny: The Weather in " +arg+ f" is  {var1} and the temperature is {grade} C" , description=f"Weather requested \nBy: {ctx.author.name}")
  await ctx.send(embed=var2)
   
# +=====================================

# @weather.error
# async def weather_error(error, ctx):
#   if isinstance(error, send_help):
#     text2 = "You need to specify the city"
#     await ctx.send(text2)

# +=====================================

@client.command()
async def servers(ctx):
  activeservers = client.guilds
  for guild in activeservers:
    await ctx.send(guild.name)



# +=====================================


@client.command()
async def createmuted(ctx):
  server = ctx.message
  perms = discord.Permissions(send_messages=False, read_messages=True)
  await client.create_role(server, name='NoSend', permissions=perms)



client.run(token)
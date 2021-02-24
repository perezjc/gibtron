import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='8ball', help='Tells you your fortune, you might not like the answer')
async def magic_eightball(ctx):
    fortunes = [
        'no',
        'yes',
        'future unclear',
        'no way dude',
        'unlikely',
        'please try again',
        '100% without a doubt',
    ]
    
    response = random.choice(fortunes)
    await ctx.send(response)
    
bot.run(TOKEN)
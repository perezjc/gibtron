import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

class autobot(discord.Client):

    def self_emoji_remove(self, payload, message):
        #List of emojis you wanna insta remove on self react :)        
        selfemojilist = ['upvote', '👍']
        for x in selfemojilist:
            if payload.emoji.name == x:
                emojiuser = (payload.user_id)
                messageuser = (message.author.id)
  
                if emojiuser == messageuser:
                    return True

    def Lazar(self, payload, message):
        LazarEmoji = ["MonkaLasarEyes"]
        for x in LazarEmoji:
            if payload.emoji.name == x:
                reaction = (message.reactions)
        
                for r in reaction:
                    if r.emoji.name == 'MonkaLasarEyes' and r.count > 4:
                        return True
                    
autobot = autobot()

@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if autobot.self_emoji_remove(payload, message):
        await message.remove_reaction(payload.emoji, payload.member)
    if autobot.Lazar(payload, message):
        await message.delete()

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

@bot.command(name= 'roll', help = 'Roll, like in WoW')
async def roll(ctx, number):
    roll_range = list(range(int(number)))
    response = random.choice(roll_range)
    await ctx.send(response)

bot.run(TOKEN)
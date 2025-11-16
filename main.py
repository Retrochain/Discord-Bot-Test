# Import discord and the necessary commands
import random
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import webserver

# Load the env file 
load_dotenv()

# Get the token for the bot
token = os.getenv('DISCORD_TOKEN')

# Creates or updates the discord.log file to log current bot activity
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Set up our necessary intents for the bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create the bot and give it a prefix
bot = commands.Bot(command_prefix='UTDiddy ', intents=intents)

# Message displayed when bot is running
@bot.event
async def on_ready():
    print("Ready to go!")

# Displays a welcome message when a user joins
@bot.event
async def on_member_join(member):
    # Get the welcome channel ID
    welcomechannel = bot.get_channel(1387631583900602491)
    
    # If the bot doesn't have the channel ID yet, fetch it
    if welcomechannel is None:
        welcomechannel = await bot.fetch_channel(1387631583900602491)
    
    # An array that contains random welcome messages
    welcomemessages = [f'Did I know you from Chill Vibe Rant {member.name}?', f'Oh great, it\'s {member.name}',
                       f'Oh shit, who gave {member.name} access to this server 😨', f'So, {member.name}, this is my goon cave.',
                       f'@everyone: Since {member.name} joined, I should let you know they were the reason Chill Vibe Rant got deleted!']
    
    # Display a random welcome message!
    await welcomechannel.send(random.choice(welcomemessages))
    
# This event basically reads every message that comes its way and sends an appropriate reply
@bot.event
async def on_message(message):
   # Don't want to cause an infinite loop? Then don't let the bot reply to itself!
   if message.author == bot.user:
       return

   # When we override the on_message event, we need to include this line otherwise the bot won't listen for any other messages
   await bot.process_commands(message)

   # This makes it so that there's a 1 in 5 chance of Bolu getting Pregnant Man reacted
   if(random.randint(0, 4) == 2) and (message.author != bot.user):
        if message.author.id == 971593663333429338:
            await message.add_reaction('🫃') 
    
   # Replies for the bot
   replys = ['Idk, do I look smart to you?', "Can you talk in 2x speed?", "I was too busy listening to Dax to hear your question",
          "I think the solution is oiling up!", "I graduated so I could care less about this", "Just cuz I\'m old and wrinkly doesn\'t mean I\'m wise!", 
          "I miss Chill Vibe Rant", "I got a better question: When can I be server owner????", "You\'re getting touched the next time I see you",
          "My hands are chapped rn, can't type", "Working on my ass, ttyl", "I don\'t get it", "Dumbass question, kill your self", "Fuck you",
          "Hold on lemme ask ChatGPT rq", f"I\'m gonna touch you {message.author.mention}", f"Aight {message.author.mention}, time to oil up 💦"]
   
   # Phrases for the bot
   phrases = ['I have a thicc ass', 'My ass is huge', 'Wanna see me clap my ass cheeks?', 
            'I wish I could hang out with y\'all', 'I like to watch my shows in 2x speed',
            'I can say the N-word', 'I got a big ass forehead', 'Im Miles Morales, but you can call me the UTDiddy', 
            'I quite like oil', '@everyone: OIL UP!', 'I think I\'m gonna wear my skin tight Miles Morales costume to a kids park today',
            'I don\'t regret deleting Chill Vibe Rant', 'I wanna play Among Us', 'Codenames anyone?', 'They call me The Flash cuz I flash people in costume',
            'Ain\'t no party like the UTDiddy party!', 'Anyone got some fried chicken?', 'I be gooning all up in this shit', 'I\'m clearly not welcomed here it seems',
            'Did I mention my ass is huge btw?', 'I wish I was good at wordle', 'I\'m the best at paintball']
   
   # If the messages starts with UTDiddy, a random reply is sent
   if message.content.startswith('UTDiddy'):
       await message.channel.send(random.choice(replys))
   
   # Replies to the user when the bot is mentioned
   elif(bot.user in message.mentions):
        await message.channel.send(random.choice(replys))
        
   # This makes it so that there's a 1 in 5 chance of the bot replying with a random phrase
   elif(random.randint(0, 4) == 2) and (message.author != bot.user):
        await message.channel.send(random.choice(phrases))

# Of course we have to run the bot, so this runs the bot
webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
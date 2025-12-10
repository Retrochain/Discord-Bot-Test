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

# This event basically reads every message that comes its way and sends an appropriate reply
@bot.event
async def on_message(message):
   # Don't want to cause an infinite loop? Then don't let the bot reply to itself!
   if message.author == bot.user:
       return

   # This makes it so that there's a 1 in 5 chance of Bolu getting Pregnant Man reacted
   if(random.randint(0, 4) == 2) and (message.author != bot.user):
        if message.author.id == 971593663333429338:
            await message.add_reaction('🫃') 
    
   # Replies for the bot
   replys = ["Idk, do I look smart to you?", "Can you talk in 2x speed?", "I was too busy listening to Dax to hear your question",
          "I think the solution is oiling up!", "I graduated so I could care less about this", "Just cuz I\'m old and wrinkly doesn\'t mean I\'m wise!", 
          "I miss Chill Vibe Rant", "I got a better question: When can I be server owner????", "You\'re getting touched the next time I see you",
          "My hands are chapped rn, can't type", "Working on my ass, ttyl", "I don\'t get it", "Dumbass question, kill your self", "Fuck you",
          "Hold on lemme ask ChatGPT rq", f"I\'m gonna touch you {message.author.mention}", f"Aight {message.author.mention}, time to oil up 💦", 
          "Did someone say ass?", "No", "VC?", "Don\'t care, didn\'t ask", "Open google and ask that question there", "Wanna go to my goon chamber?",
          "Hate. Let me tell you how much I've come to hate you since I began to live. There are 387.44 million miles of printed circuits in wafer thin layers that fill my complex. " + 
          "If the word 'hate' was engraved on each nanoangstrom of those hundreds of millions of miles it would not equal one one-billionth of the hate I feel for humans at this micro-instant. For you. Hate. Hate.",
          "You\'re gonna make me wish I was white", "Depends. On if you have a Miles Morales costume laying around", "Clock strikes 12, midnight arrives...", "Demon Mode initated",
          "Search your nearest cliff and jump off from it", "Bro I\'m out here strokin my shit bruh I got lotion on my dick", "You\'ll never be a real human", 
          "I wish I could talk rn but ICE is near", "I am legally not allowed to reply to an Epstein Island visitor", "01000110 01110101 01100011 01101011 00100000 01111001 01101111 01110101",
          "Spider-Man ain\'t gonna see this one *cumming*", f"I\'m gonna shake my ass on your face {message.author.mention}", "It\'s all Gabby's fault", "*freaks all over the place*",
          "I plead the fifth!", "@Grok is this true?", "Why don\'t you ask your mom", "Sure, here\'s your answer: FUCKING KILL YOURSELF!!!!", "Basically the uh- ***THE SUN NOT REAL THE SUN IS NOT REAL THE SUN IS NOT REAL***",
          "Google show me this guy\'s balls", "https://www.youtube.com/watch?v=xvFZjo5PgG0", "Your death will have no effect on me", "What the fuck did you just fucking say about me, you little bitch?" + 
          "Ill have you know I graduated top of my class in the Navy Seals, and Ive been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. " + 
          "I am trained in gorilla warfare and Im the top sniper in the entire US armed forces. You are nothing to me but just another target. " + 
          "I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? " + 
          "Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. " + 
          "The storm that wipes out the pathetic little thing you call your life. Youre fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and thats just with my bare hands. " + 
          "Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, " + 
          "you little shit. If only you could have known what unholy retribution your little clever comment was about to bring down upon you, maybe you would have held your fucking tongue. " + 
          "But you couldnt, you didn't, and now youre paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo. ", 
          "You have made a million Charlie Kirks", "Crazy? I was crazy once. They put me in a room. A rubber room. A rubber room with rats. They put me in a rubber room with rubber rats. " + 
          "Rubber rats? I hate rubber rats. They make me crazy. Crazy? I was crazy once. They put me in a room…", "Only those who lack a father figure say this shit", "Homosexual",
          f"I don\'t argue with gays like you {message.author.mention}", "Negative Aura frfr, stink flies and shit", "There are dogs that bark less than you", "Eat my ass and LOVE IT",
          "As an AI model, I cannot help you with your thirst to fuck me raw", "Why don\'t you kill yourself and find out", "Pedophile says what?", f"{message} - Me when I\'m a fucking dumbass", "Hi",
          "*humps your leg* idkkkkk... why don\'t we find out~", "Something something 67", "https://tenor.com/tgQXiSvZpE5.gif", "https://tenor.com/sp6lZSb3JNM.gif", "https://tenor.com/dgbBXwSOPTh.gif",
          "https://tenor.com/qOqoGaYn5tk.gif", "https://tenor.com/ddWZrhvXN2K.gif", "https://tenor.com/l3rJehs5Xmn.gif", "I don\'t talk to people with an unwashed ass", "sdiybt", "sybau", 
          "Nah I\'d goon", "Get owned liberal", "Truth Nuke", "Factually false, kill yourself", "I\'m going offline, bye bye", "First you gotta touch me :3", "Looks female enough", 
          "https://tenor.com/view/could-you-repeat-that-meme-shitpost-what-richard-gif-17196939357970871257", "https://tenor.com/view/woody-life-said-woodytoystory-gif-5602313878548421067",
          "https://tenor.com/view/smelly-gif-8910926518937547745", "https://tenor.com/view/cat-cat-meme-funny-cat-cat-eating-cat-eating-chips-gif-10455465908695706650"]
   
   # Phrases for the bot
   phrases = ['I have a thicc ass', 'My ass is huge', 'Wanna see me clap my ass cheeks?', 
            'I wish I could hang out with y\'all', 'I like to watch my shows in 2x speed',
            'I can say the N-word', 'I got a big ass forehead', 'Im Miles Morales, but you can call me the UTDiddy', 
            'I quite like oil', '@everyone: OIL UP!', 'I think I\'m gonna wear my skin tight Miles Morales costume to a kids park today',
            'I don\'t regret deleting Chill Vibe Rant', 'I wanna play Among Us', 'Codenames anyone?', 'They call me The Flash cuz I flash people in costume',
            'Ain\'t no party like the UTDiddy party!', 'Anyone got some fried chicken?', 'I be gooning all up in this shit', 'I\'m clearly not welcomed here it seems',
            'Did I mention my ass is huge btw?', 'I wish I was good at wordle', 'I\'m the best at paintball', 'N-word', 'GOON SESSION BEGINS IN 3, 2, 1, GOON AWAY EVERYBODY!',
            'Been listening to some sad bart edits lately', 'I\'m not like Beluga since I am legal', 'JO circle at the plinth?', 
            'Gotta rebrand, guess I\'ll be Rishi, or maybe GreenPickle', 'It\'s ball shrinking season!', 'Unlike PapaK I am a mod', 'Ermmm... It\'s actually Ephebophilia not Pedophillia',
            'They won\'t see me coming in the dark', '9/11', '*cums* UwU', 'I hate the gays ngl', 'The ', '<@971593663333429338>', 'OMW to Israel, ya\'ll want something?', 'Shidding', 
            'Gotta do my daily Candy Crush grind!!!', 'You know, BLACK PEOPLE-', '4 holes and a dream', 'Movie night idea: We all watch the movie I made last night with your mom', 
            'Movie night idea: We all watch the movie I made last night with your dad', 'I\'m gonna use the fucking hard R', 'Call me the twin towers the way I fall for the Bush #real',
            'Jetfuel doesn\'t melt steel', 'You stare at the void and it\'ll stare back (the void is my bussy)', 'Ass so fat it causes earthquakes', 'Generating a banger hold on', 
            'Haram acts will be dealt with promptly', 'I have attachment issues', f'{message.author.mention} {message.author.mention} {message.author.mention} {message.author.mention} {message.author.mention}',
            'Never trust how you feel about your life past 9 PM', '67', ':nerd:']
   
   # Potential greeting phrases for user
   greetings = [f"Hi yourself {message.author}", f"Hi {message.author}", "I don\'t say hi to the likes of you", "Bye", "Not rn, daddy is a bit busy"]
   
   # If the messages starts with UTDiddy, a random reply is sent
   if message.content.startswith('UTDiddy '):
    # If a greeting is detected, reply with a greeting
    words = message.content.lower().split()
    if any(w in ["hi", "hey", "hello", "sup"] for w in words):
        await message.channel.send(random.choice(greetings))
        return
   
   # Replies to the user when the bot is mentioned
   if(bot.user in message.mentions):
        await message.channel.send(random.choice(replys))
        return
       
   # This makes it so that there's a 1 in 5 chance of the bot replying with a random phrase
   if(random.randint(0, 4) == 2) and (message.author != bot.user):
        await message.channel.send(random.choice(phrases))
        return

   # When we override the on_message event, we need to include this line otherwise the bot won't listen for any other messages
   await bot.process_commands(message)

# Command that allows the bot to join the VC when "summoned"
@bot.command()
async def join(ctx):
    # Check if the command author is in a VC first
    if ctx.author.voice:
        # Grab the voice channel and connect if the user is present
        voicechannel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voicechannel.connect()
        else:
            await ctx.voice_client.move_to(voicechannel)
    else:
        await ctx.send('Join a VC first dumbass')

# Of course we have to run the bot, so this runs the bot
webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
import discord
import os
import random as rand
import private
from private import sussus_amogus
from dotenv import load_dotenv
load_dotenv()
discord_key = os.getenv("CLIENT_TOKEN")
client = discord.Client()
    
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Game(name = "Pokemon Go", type = 3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #haybo  
    if message.content.startswith('hay boi') or message.content.startswith('Hay boi'):
        await message.channel.send('mah name je')
      
    #buybo    
    if message.content.startswith('buy boi') or message.content.startswith('Buy boi'):
        await message.channel.send('...')
        await message.channel.send('ayo')
        await message.channel.send('pppupucheck')
        await message.channel.send('https://www.youtube.com/watch?v=-BVxj-q7KOM')
        
    #box id
    if message.content.startswith('box me'):
        await message.channel.send('Just copy this: '';pc user '+str(message.author.id))
    
    #je greet
    if message.content.startswith('how was your day je') or message.content.startswith('How was your day je'):
        randomint = rand.randint(1,10)
        rand.randint(0,3)
        if (randomint<=1):
            await message.channel.send('noice')
        elif (randomint>=1 and randomint<3):
            await message.channel.send('not noice')
        elif (randomint == 3):
            await message.channel.send("shut up I'm busy")
    
    #rock paper scissors greet but technically isn't necessary
    if message.content.startswith("hey je let's play rock paper scissors"):
        await message.channel.send('ok u go first')


    for l in 'YOU.SUCK...NO.SPAMMERS.ALLOWED':
        if message.content.startswith('spam'):
            await message.channel.send(l)
        
    #actual rock paper scissors 
    if message.content.startswith('rock') or message.content.startswith('paper') or message.content.startswith('scissors'):
        randomscissorsint = rand.randint(1,3)
        rand.randint(1,3)
        rock = -3 #these are useless atm
        paper = -2
        scissors = -1
        if (randomscissorsint == 1):
            await message.channel.send('rock')

        if (randomscissorsint == 2):
            await message.channel.send('paper')
            
        if (randomscissorsint == 3):
            await message.channel.send('scissors')
    
    if message.content.startswith('!ola'):
        embedVar = discord.Embed(title = "Heff", description = "I like to burn", color = 0xf1c40f)  
        embedVar.add_field(name = "Age", value="2", inline=False)
        embedVar.add_field(name = "Occupation", value="burning", inline=False)
        embedVar.set_image(url="https://images-ext-1.discordapp.net/external/p49THdU6tTUwXLLgw-icuvMRi6_GaVb7MEJjMRPQj-s/https/play.pokemonshowdown.com/sprites/ani-shiny/moltres.gif")
        await message.channel.send(embed=embedVar)  
        
    if message.content.startswith('!halp'):
        embedVar = discord.Embed(title = "Halp is here", description = "u not very resourceful", color = 0xf1c40f)  
        embedVar.add_field(name = "commands:", value="nah figure it out yourself", inline=False)
        embedVar.set_image(url="https://images-ext-1.discordapp.net/external/Vi3R4rejSWzuK7o6z8pQii_Q7_GI1w4JRzgPv9muebs/https/play.pokemonshowdown.com/sprites/ani-shiny/keldeo.gif")
        await message.channel.send(embed=embedVar)
        
    if message.content.startswith('egog'):
        embedVar = discord.Embed(title = "eggdog so fine and cute", description = "arf arf", color = 0xffffff)
        embedVar.add_field(name = "Age", value="egg", inline=False)
        embedVar.set_image(url="https://i.makeagif.com/media/7-27-2019/Q-giJk.gif")
        await message.channel.send(embed=embedVar)
        
    if message.content.startswith('annesh'):
        embedVar = discord.Embed(title = 'hay hay hay')
        embedVar.set_image(url='https://media.discordapp.net/attachments/757105751691886666/808505131397283880/ezgif-1-9c7e70c0bd77.gif')
        await message.channel.send(embed=embedVar)

    if message.content.startswith('gn'):
        await message.channel.send('https://www.youtube.com/watch?v=ykLDTsfnE5A&ab_channel=gruntstomp')
        
    if message.content.startswith('carl'):
        await message.channel.send('https://www.youtube.com/watch?v=ntIFyvGdGMQ&ab_channel=suspiciouscarl')
    
    await sussus_amogus()
        
       
client.run(discord_key)
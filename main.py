import discord
import random as rand
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

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
        await message.channel.send('peepeepoopoocheck')
        await message.channel.send('https://www.youtube.com/watch?v=-BVxj-q7KOM')
    
    #;p ping    
    if message.content.startswith(';p'):
        await message.channel.send('I am watching you {}'.format(message.author.mention))
    
    #box id
    if message.content.startswith('box me'):
        await message.channel.send('Just copy this: '';pc user '+str(message.author.id))
    
    #;f notif    
    if message.content.startswith(';f'):
        await message.channel.send('ara ara the fish will not bite today ')
    
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
            
        '''if message.content.startswith('rock') and message.channel.send('paper'):
            await message.channel.send('haha you suck')'''
    
    if message.content.startswith('!ola'):
        embedVar = discord.Embed(title = "Heff", description = "I like to listen to "/next
        +"the screams of my comrades as they burn", color = "fuchsia")  
        embedVar.addfield(name = "Age", value="2", inline=False)
        embedVar.addfield(name = "Occupation", value="burning comrades", inline=False)
        await message.channel.send(embed=embedVar)  

client.run('Nzc5MDg3MTU5OTQ4NDc2NTI2.X7bbdQ._OcMe-MDDOJIK4tyMD3ThaLl6sU')
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

    if message.content.startswith('hay boi') or message.content.startswith('Hay boi'):
        await message.channel.send('mah name je')
        
        
    if message.content.startswith('buy boi') or message.content.startswith('Buy boi'):
        await message.channel.send('...')
        await message.channel.send('ayo')
        await message.channel.send('peepeepoopoocheck')
        await message.channel.send('https://www.youtube.com/watch?v=-BVxj-q7KOM')
        
    if message.content.startswith(';p'):
        await message.channel.send('I am watching you {}'.format(message.author.mention))
    
    if message.content.startswith('box me'):
        await message.channel.send('Just copy this: '';pc user '+str(message.author.id))
        
    if message.content.startswith(';f'):
        await message.channel.send('ara ara the fish will not bite today ')
    
    if message.content.startswith('how was your day je') or message.content.startswith('How was your day je'):
        randomint = rand.randint(1,10)
        rand.randint(0,3)
        if (randomint<=1):
            await message.channel.send('noice')
        elif (randomint>=1 and randomint<3):
            await message.channel.send('not noice')
        elif (randomint == 3):
            await message.channel.send("shut up I'm busy")
    
    if message.content.startswith("hey je let's play rock paper scissors"):
        await message.channel.send('ok u go first')

    if message.content.startswith('rock') or message.content.startswith('paper') or message.content.startswith('scissors'):
        randomscissorsint = rand.randint(1,3)
        rand.randint(1,3)
        rock = -3
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
        

client.run('Nzc5MDg3MTU5OTQ4NDc2NTI2.X7bbdQ._OcMe-MDDOJIK4tyMD3ThaLl6sU')
import discord
import random as rand
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
        await message.channel.send('peepeepoopoocheck')
        await message.channel.send('https://www.youtube.com/watch?v=-BVxj-q7KOM')
    
    #;p ping    
    '''if message.content.startswith(';p'):
        await message.channel.send('I am watching you {}'.format(message.author.mention))'''
        
    #box id
    if message.content.startswith('box me'):
        await message.channel.send('Just copy this: '';pc user '+str(message.author.id))
    
    #;f notif    
    '''if message.content.startswith(';f'):
        await message.channel.send('ara ara the fish will not bite today ')'''
    
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
            
        '''if message.content.startswith('rock') and message.channel.send('paper'):
            await message.channel.send('haha you suck')'''
    
    if message.content.startswith('!ola'):
        embedVar = discord.Embed(title = "Heff", description = "I like to listen to the screams of my comrades as they burn", color = 0xf1c40f)  
        embedVar.add_field(name = "Age", value="2", inline=False)
        embedVar.add_field(name = "Occupation", value="burning comrades", inline=False)
        embedVar.set_image(url="https://images-ext-1.discordapp.net/external/p49THdU6tTUwXLLgw-icuvMRi6_GaVb7MEJjMRPQj-s/https/play.pokemonshowdown.com/sprites/ani-shiny/moltres.gif")
        await message.channel.send(embed=embedVar)  
        
    if message.content.startswith('!halp'):
        embedVar = discord.Embed(title = "Halp is here", description = "u not very resourceful", color = 0xf1c40f)  
        embedVar.add_field(name = "commands:", value="nah figure it out yourself", inline=False)
        embedVar.set_image(url="https://images-ext-1.discordapp.net/external/Vi3R4rejSWzuK7o6z8pQii_Q7_GI1w4JRzgPv9muebs/https/play.pokemonshowdown.com/sprites/ani-shiny/keldeo.gif")
        await message.channel.send(embed=embedVar)
        
    if message.content.startswith('egog'):
        embedVar = discord.Embed(title = "Annesh so fine and cute", description = "arf arf", color = 0xffffff)
        embedVar.add_field(name = "Age", value="egg", inline=False)
        embedVar.set_image(url="https://i.makeagif.com/media/7-27-2019/Q-giJk.gif")
        await message.channel.send(embed=embedVar)
        
    if message.content.startswith('penis'):
        await message.channel.send('nono {} u naughty boi'.format(message.author.mention))

    if message.content.startswith('gn'):
        await message.channel.send('https://www.youtube.com/watch?v=ykLDTsfnE5A&ab_channel=gruntstomp')
        
    if message.content.startswith('carl'):
        await message.channel.send('https://www.youtube.com/watch?v=ntIFyvGdGMQ&ab_channel=suspiciouscarl')
        
    if message.content.startswith('anime pls'):
        await message.channel.send('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvDhcBWIQYlh1tUAtslgBO5gueF05IWaD0Ww&usqp=CAU')
        await message.channel.send('moshi moshi')
        await message.channel.send('.')
        await message.channel.send('doki')
        await message.channel.send('doki')
        await message.channel.send('watashi wa anime gorl kyun <3')
        
        
client.run('Nzc5MDg3MTU5OTQ4NDc2NTI2.X7bbdQ._OcMe-MDDOJIK4tyMD3ThaLl6sU')
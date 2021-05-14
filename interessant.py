import discord
import os
from datetime import datetime
now = datetime.now().time().strftime("%H:%M:%S") 
date = datetime.now().strftime("%Y-%m-%d") 

async def sussus_amogus(message):
    if message.content.startswith('anime pls'):
            await message.channel.send('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvDhcBWIQYlh1tUAtslgBO5gueF05IWaD0Ww&usqp=CAU')
            await message.channel.send('moshi moshi')
            await message.channel.send('.')
            await message.channel.send('doki')
            await message.channel.send('doki')
            await message.channel.send('watashi wa anime gorl kyun <3')

    if message.content.startswith('penis'):
            await message.channel.send('nono {} u naughty boi'.format(message.author.mention))

    if ('india' in message.content) or ('abhijit' in message.content) or ('british' in message.content):
        file = open('disco_data.csv', 'w', newline = '')
        file.write(str(message) + '\n') 
        await message.channel.send('indeed {}'.format(message.author.mention))   
        await message.channel.send('compromising data recorded, you are an enemy of the state...' + str(message))

    #;f notif    
    '''if message.content.startswith(';f'):
        await message.channel.send('ara ara the fish will not bite today ')'''

    #;p ping    
    '''if message.content.startswith(';p'):
        await message.channel.send('I am watching you {}'.format(message.author.mention))'''
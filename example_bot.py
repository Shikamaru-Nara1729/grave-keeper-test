import discord
import random
import asyncio
import re
import os
from dotenv import load_dotenv
load_dotenv()

#client = discord.Client()
class MyClient(discord.Client):
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))
        #print(self.user.name)
        #print(self.user.id)
        print('------')

    async def on_message(self,message):
        gravekeeper_mention=re.compile(r'.*gravekeeper.*', re.IGNORECASE)
        F_respect=re.compile(r'.*Press F.*', re.IGNORECASE)
#-----------------------------------------------------
        if message.author == client.user:
            return
#-----------------------------------------------------
        elif message.content.startswith('Helloow'):
            await message.channel.send('* rises from the grave \U0001FAA6 * Sup?')
#-----------------------------------------------------
        elif message.content.startswith('$guess game'):
            await message.channel.send('Guess a number between 0 and 10.')
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            myguess=random.randint(0,10)

            try:
                guess=await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(myguess))

            if int(guess.content)==myguess:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(myguess))
#------------------------------------------------------        
        elif gravekeeper_mention.match(message.content):
                await message.channel.send('Bruh!')

#------------------------------------------------------
        elif F_respect.match(message.content):
                await message.channel.send('\U0001F490')
            

    

client=MyClient()
client.run(os.getenv('TOKEN'))

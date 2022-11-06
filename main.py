import discord
import requests
import random
from dalle2 import Dalle2

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
dalle = Dalle2("sess-vCG7aGg6zWQumDh04n9akOiLSXYlNx2gH7Pa3X0r")

def get_image(x):
    dalle_image_generation = dalle.generate(x)
    dalle_image_link = dalle_image_generation[0]['generation']['image_path']
    dalle_image_link1 = dalle_image_generation[1]['generation']['image_path']
    dalle_image_link2 = dalle_image_generation[2]['generation']['image_path']
    dalle_image_link3 = dalle_image_generation[3]['generation']['image_path']
    return dalle_image_link, dalle_image_link1, dalle_image_link2, dalle_image_link3

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    
    if message.content.startswith('$dalle'):
        try:
            dalle_prompt = msg[6:]
            dalle_img = get_image(dalle_prompt)
            await message.channel.send(dalle_img[0])
            await message.channel.send(dalle_img[1])
            await message.channel.send(dalle_img[2])
            await message.channel.send(dalle_img[3])
        except:
            await message.channel.send('Something went wrong :confused:')

    if message.content.startswith('$help'):
        await message.channel.send("""Hi! I am Reservoir Dall-e :smile:
        \nI am a discord :robot: that can take user suggestions and create unique images using AI \nJust type the command $dalle followed by a prompt (e.g $dalle shiba inu playing chess).
        \nI look forward to seeing some of the ideas you come up with :art:.""")  

client.run('MTAwNjg0MzA1NjA1OTg1ODk1Ng.GWCsI-.Pl3dcjHO6q-etIXDCddzX6udO4OsipRqS2-0Rc')
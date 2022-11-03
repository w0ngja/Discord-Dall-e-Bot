import discord
import requests
import random
from dalle2 import Dalle2

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
dalle = Dalle2("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

def get_image(x):
    dalle_image_generation = dalle.generate(x)
    dalle_image_link1 = dalle_image_generation[0]['generation']['image_path']
    return dalle_image_link1

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
  
    if message.content.startswith('$dalle'):
        dalle_prompt = msg[6:]
        dalle_img = get_image(dalle_prompt)
        await message.channel.send(dalle_img) 

    if message.content.startswith('$help'):
        await message.channel.send("""Hi! I am Reservoir Dall-e :smile:
        \nI am a discord :robot: that can take user suggestions and create unique images using AI \nJust type the command $dalle followed by a prompt (e.g $dalle shiba inu playing chess).
        \nI look forward to seeing some of the ideas you come up with :art:.""")  

client.run('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
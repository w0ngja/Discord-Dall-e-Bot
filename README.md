# Discord-Dall-e-Bot

A fun discord bot that uses the DALL.E 2 engine to create original, unique images and art from a users text description.

For help using the discord bot type the $help command in the Discord channel:
![alt-text](https://github.com/w0ngja/Discord-Dalle-Bot/blob/main/readme_misc/readme_help_command.PNG)

To generate an image use the $dalle command followed by an image suggestion:
![alt-text](https://github.com/w0ngja/Discord-Dalle-Bot/blob/main/readme_misc/readme_dalle_command.PNG)

Thanks and have fun!

# How to get API keys

# Hosting the Bot
A range of hosting options exist for the bot but for its ease of use, flexibility and relatively low price, I elected to host this Discord bot on a Amazon Web Services (AWS) EC2 t2.micro instance.

  Once the instance has been created, connect using either the AWS CLI or a SSH program (e.g. Putty). 
  
  Update the dependencies (sudo apt-get update) and create a new virtual environment for the bot (python3 -m venv venv).
  
  To keep the bot alive after disconnecting from the terminal, I also recommend installing PM2 (sudo npm install pm2 -g) to daemonize the process.

  I selected a t2.micro instance for my bot as the image generation process isn't computationally difficult . However, I may elect to move to a t2.nano instance in the future.

v1.0.1: Added exception clauses for dalle image generation rules\
v1.0: Initial Release

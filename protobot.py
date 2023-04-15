import discord
import os
from nomic.gpt4all import GPT4All
from datetime import datetime

from discord.ext import commands, tasks

rendersnaek = bool(False)
snaekrendered = bool(False)
bullyrainbow = bool(False)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {client.user}')

    async def on_message_edit(self, before, after):
        # detects edited messages
        if 'http' in before.content.lower():
            return
        else:
            await before.reply("Caught in 8k: " + str(before.content) + " -> " + str(after.content))

    async def on_message_delete(self, message):
        # forwards deleted message to nkvd
        channel = client.get_channel(1052271222932643890)

        if not 'http' in message.content.lower():
            embedd = discord.Embed(title="", description="")
            embedd.add_field(name="Deleted", value=str(message.content))
            await channel.send(embed=embedd)
        else:
            await channel.send(message.content)

        await message.channel.send("delet?")
        # await channel.send("deleted message: -> " + str(deleter) + (": ") + str(message.content))

    async def on_message(self, message):
        # ignores if message is from this bot
        if message.author.id == self.user.id:
            return
        if message.channel.id == 754889880848564285:
            out = m.prompt(message.content)
            await message.reply(out)
            
        # # ignore if rainbowbot
        # if message.author.id == 756530024349302824:
        #     return

        # heart reaction if yadanar
        if message.author.id == 912344991089688636:
            await message.add_reaction("❤")

        # ukraine reaction on heil
        if 'heil' in message.content.lower():
            await message.add_reaction("\U0001F1FA" + "\U0001F1E6")

        # replies with hallo upon hallo
        if message.content.lower().startswith('hallo') and not message.author.id == 756530024349302824:
            await message.reply('Hallo', mention_author=True)

        #replies with hola upon hola
        if message.content.lower().startswith('hola') and not message.author.id == 756530024349302824:
            await message.reply('Hola', mention_author=True)
        
        #replies with hola upon salut
        if message.content.lower().startswith('salut') and not message.author.id == 756530024349302824:
            await message.reply('Salut', mention_author=True)

        # replies message to german if mentioning izu
        # if 'izu' in message.content.lower() and message.author.id == 340471556251582465:
        #     await message.add_reaction("\U0001f3f3\uFE0F\u200D\U0001f308")
        #     await message.reply('Why are you gay?', mention_author=True)

        # slava ukraini geroyam slava and reaction
        if 'slava ukraini' in message.content.lower():
            lastmsg = await message.channel.send('Geroyam Slava!')
            await message.add_reaction("\U0001F1F7" + "\U0001F1FA")
            await message.add_reaction("\U0001F4AA")
            await lastmsg.add_reaction("\U0001F1F7" + "\U0001F1FA")
            await lastmsg.add_reaction("\U0001F4AA")

        # enables bullying rainbow
        global bullyrainbow
        if message.content.lower().startswith('!bullyrainbow'):
            bullyrainbow = True
            await message.channel.send("ja why not?")

        # disables bullying rainbow
        if message.content.lower().startswith('!unbullyrainbow'):
            bullyrainbow = False
            await message.channel.send("wtf???")
        
        # bullies rainbow
        if message.author.id == 206862952823783424 and bullyrainbow:
            await message.add_reaction("\U0001F1FA" + "\U0001F1E6")
            await message.reply('why?', mention_author=True)
        
        # bullies rainbow bot
        if message.author.id == 756530024349302824 and bullyrainbow: 
            await message.add_reaction("\U0001F1FA" + "\U0001F1E6")
            await message.reply('who are you?', mention_author=True)

        # shows bot's time
        if message.content.lower().startswith('!bottime'):
            current_time = datetime.now().strftime("%H:%M:%S")
            await message.channel.send("Bot's current time is = " + current_time)

        if message.content.lower().startswith('!halp'):
            return

        # russian reaction
        if 'russia' in message.content.lower():
            await message.add_reaction("\U0001F1F7" + "\U0001F1FA")

        # if message.content.lower().startswith('/snaekon'):
        #      sendmessage.start()
        # if message.content.lower().startswith('/snaekoff'):
        #      sendmessage.stop()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

with open('token.txt') as f:
    token = f.readline()

m = GPT4All()
m.open()
client.run(token)




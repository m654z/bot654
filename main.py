import os, random, time
from io import BytesIO

import discord
from dotenv import load_dotenv
from keep_running import keep_running

from wojak import addText # Image generation
import markov # Botquote generation

# Set up the environment and keep the bot running
load_dotenv()
keep_running()
TOKEN = os.environ.get('TOKEN')
client = discord.Client()

# Important string
STR_amogus = """```⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌
⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌
⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌
⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪
⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡
⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐
⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔
⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘
⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎
⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗
⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷
⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟
⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰
⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊
⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌
⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁
⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀
⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀
⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟
⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾
⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽```"""

@client.event
async def on_message(message):
    msg = message.content
    msg_lower = message.content.lower()

    # Make sure the bot isn't the author of the message so it
    # doesn't get stuck in an infinite reply loop
    if message.author == client.user:
        # ...unless the message starts with a wojak command
        # (for use with !botsay)
        if msg_lower.startswith("!wojak") or msg_lower.startswith("!chad"):
          pass
        else:
          return

    # 1 in 500 chance to include the 'cringe' message
    reply_chance = random.randint(0, 499)
    if reply_chance == 0:
      await message.channel.send('"' + msg + '"? thats kinda cringe bro ngl')

    # ----- COMMANDS -----

    # BOTSAY
    # !botsay (channel id) (message)
    if msg_lower.startswith("!botsay"):
        msg = msg.split(' ')
        channel = client.get_channel(int(msg[1]))
        await channel.send(' '.join(msg[2:]))
    
    # BOTMUSIC
    elif msg_lower.startswith("!botmusic"):
        time.sleep(1)
        await message.channel.send(file=discord.File(r'assets/botmusic.mp3'))

    # WOJAK
    # !wojak (message)
    elif msg_lower.startswith("!wojak"):
      if(' ' in msg):
        # Split the message at the first space and use the
        # wojak.py module to add the result to an image
        image = addText(msg.split(' ', 1)[1], "w")
        with BytesIO() as binary:
          image.save(binary, 'PNG')
          binary.seek(0)
          await message.channel.send(file=discord.File(fp=binary, filename="assets/wojak.png"))

    # CHAD
    # !chad (message)
    elif msg_lower.startswith("!chad"):
      if(' ' in msg):
        image = addText(msg.split(' ', 1)[1], "c")
        with BytesIO() as binary:
          image.save(binary, 'PNG')
          binary.seek(0)
          await message.channel.send(file=discord.File(fp=binary, filename="assets/wojak.png"))
    
    # BOTQUOTE
    elif msg_lower.startswith("!botquote"):
      # Use the markov.py module to generate some random text
      await message.channel.send('*"' + markov.get_sentence() + '"*')
    
    # ----- MISCELLANIOUS -----

    elif 'dead' in msg_lower:
        if 'chat' in msg_lower:
            with open('assets/dead-chat.gif', 'rb') as f:
                gif = discord.File(f)
                await message.channel.send(file=gif)
        elif 'chad' in msg_lower:
            with open('assets/dead-chad.png', 'rb') as f:
                pic = discord.File(f)
                await message.channel.send(file=pic)

    elif 'alive' in msg_lower:
        if 'chat' in msg_lower:
            with open('assets/alive-chat.gif', 'rb') as f:
                gif = discord.File(f)
                await message.channel.send(file=gif)
        elif 'chad' in msg_lower:
            with open('assets/chad.gif', 'rb') as f:
                gif = discord.File(f)
                await message.channel.send(file=gif)

    elif 'amogus' in msg_lower:
        await message.channel.send(STR_amogus)

    elif 'sus' in ''.join(c for c in msg_lower if c.isalnum()):
        await message.channel.send(STR_amogus)

    elif msg_lower == "gaming":
        await message.channel.send("https://twitter.com/DannyDeVito/status/4924648679?s=20")

client.run(TOKEN)

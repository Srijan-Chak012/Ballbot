import discord
import os
from dotenv import load_doten
import requests
import json
import random
import reply
import gif
from datetime import datetime
import time
import help

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
SEED = os.getenv('TENORKEY')
client = discord.Client()
random.seed(datetime.now())


def GIF(message):
    if len(message) == 4:
        message = "$gif love"
    if message[4] != " ":
        return "Command Not found: Please add a space after $gif"
    url = 'https://api.tenor.com/v1/search?q='+ message[5:] +'&key=' + SEED + '&contentfilter=high'
    r = requests.get(url)
    data = r.json()
    results = data["results"]
    index = random.choice(range(0, len(results)))
    return results[index]["url"]


in_pen = False
score = 0
user = -1
l1 = -1
l2 = -1
d1 = -1
d2 = -1
x = -1

async def defend(channel):
    react, duser = await client.wait_for('reaction_add')
    while str(duser.id) == "884140236257497088":
        react, duser = await client.wait_for('reaction_add')
    # await channel.send(user.mention + "reacted with " + react.emoji)
    print(str(duser.id) + " Here " + str(user))
    if duser.id != user:
        return
    global d1, d2, x, bot_score
    print("Here")
    to_score = random.uniform(0,100)
    if to_score <= d1:
        to_score = 0
    elif to_score <= d2:
        to_score = 1
    else:
        to_score = 2

    user_defense = -1
    print(react.emoji)

    if react.emoji == "\N{Leftwards Black Arrow}":
        user_defense = 0
    elif react.emoji == "\N{Upwards Black Arrow}":
        user_defense = 1
    elif react.emoji == "\N{Black Rightwards Arrow}":
        user_defense = 2

    await channel.send(str(user_defense) + " " + str(to_score))
    if user_defense == to_score:
        await channel.send("You do not suck yet")
    else:
        await channel.send("You suck")
        bot_score += 1
    if user_defense == 0:
        d1 += x
    elif user_defense == 1:
        d1 -= (x / 2)
        d2 += (x / 2)
    elif user_defense == 2:
        d2 -= x

    # await channel.send("d1 and d2: " + str(d1) + " " + str(d2))


async def shoot(channel):
    react, luser = await client.wait_for('reaction_add')
    while str(luser.id) == "884140236257497088":
        react, luser = await client.wait_for('reaction_add')
    # await channel.send(user.mention + "reacted with " + react.emoji)
    print(str(luser.id) + " Here " + str(user))
    if luser.id != user:
        return
    global l1, l2, x, score
    print("Here")
    to_defend = random.uniform(0,100)
    if to_defend <= l1:
        to_defend = 0
    elif to_defend <= l2:
        to_defend = 1
    else:
        to_defend = 2

    user_shot = -1
    print(react.emoji)

    if react.emoji == "\N{Leftwards Black Arrow}":
        user_shot = 0
    elif react.emoji == "\N{Upwards Black Arrow}":
        user_shot = 1
    elif react.emoji == "\N{Black Rightwards Arrow}":
        user_shot = 2

    await channel.send(str(user_shot) + " " + str(to_defend))
    if user_shot == to_defend:
        await channel.send("You suck")
    else:
        await channel.send("You do not suck yet")
        score += 1
    if user_shot == 0:
        l1 += x
    elif user_shot == 1:
        l1 -= (x / 2)
        l2 += (x / 2)
    elif user_shot == 2:
        l2 -= x

    # await channel.send("l1 and l2: " + str(l1) + " " + str(l2))

async def sudden_death(channel):
    while(bot_score == score):
        await channel.send('You are now in SUDDEN DEATH, score and block to win the match!')
        await channel.send('React to this message with the side you want to shoot towards:')
        send = await channel.send(file=discord.File('./penalty.jpg'))
        await send.add_reaction("\N{Leftwards Black Arrow}")
        await send.add_reaction("\N{Upwards Black Arrow}")
        await send.add_reaction("\N{Black Rightwards Arrow}")
        await shoot(channel)
        await channel.send("Your score: " + str(score))
        await channel.send("Bot score: " + str(bot_score))

        await channel.send('React to this message with the side you want your goalkeeper to defend towards:')
        send = await channel.send(file=discord.File('./keeper.jpg'))
        await send.add_reaction("\N{Leftwards Black Arrow}")
        await send.add_reaction("\N{Upwards Black Arrow}")
        await send.add_reaction("\N{Black Rightwards Arrow}")
        await defend(channel)
        await channel.send("Your score: " + str(score))
        await channel.send("Bot score: " + str(bot_score))

    if score > bot_score:
        await channel.send('Congratulations! You have won the SUDDEN DEATH! :partying_face:')

    elif bot_score > score:
        await channel.send('LMAO, you lost against a bot in the SUDDEN DEATH! :rofl:')

async def prepare(channel, user):
    global l1, l2, d1, d2, x
    l1 = 33.33
    l2 = 66.66
    d1 = 33.33
    d2 = 66.66
    x = random.uniform(-2, 5)
    for i in range(5):
        await channel.send('React to this message with the side you want to shoot towards:')
        send = await channel.send(file=discord.File('./penalty.jpg'))
        await send.add_reaction("\N{Leftwards Black Arrow}")
        await send.add_reaction("\N{Upwards Black Arrow}")
        await send.add_reaction("\N{Black Rightwards Arrow}")
        await shoot(channel)
        await channel.send("Your score: " + str(score))
        await channel.send("Bot score: " + str(bot_score))
        diff = abs(score - bot_score)
        if diff > (5-i):
            break

        await channel.send('React to this message with the side you want your goalkeeper to defend towards:')
        send = await channel.send(file=discord.File('./keeper.jpg'))
        await send.add_reaction("\N{Leftwards Black Arrow}")
        await send.add_reaction("\N{Upwards Black Arrow}")
        await send.add_reaction("\N{Black Rightwards Arrow}")
        await defend(channel)
        await channel.send("Your score: " + str(score))
        await channel.send("Bot score: " + str(bot_score))
        diff1 = abs(bot_score-score)
        if diff1 > (5-i):
            break
    
    if score > bot_score:
        await channel.send('Congratulations! You have won! :partying_face:')

    elif bot_score > score:
        await channel.send('LMAO, you lost against a bot :rofl:')
    
    else:
        await channel.send('Sudden Death Time')
        sudden_death(channel)

async def pen(channel, author):
    global in_pen
    global score, bot_score
    global user
    if in_pen:
        await channel.send("Penalty shootout already in progress!")
        return
    in_pen = True
    score = 0
    bot_score = 0
    user = author.id
    await prepare(channel, user)

random.seed(time.time())

print("Bot up!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$reply '):
        await message.channel.send(reply.to_send(message.content))
    elif message.content.startswith('$gif'):
        await message.channel.send(gif.GIF(message.content))
    elif message.content.startswith('$help'):
        await message.channel.send(help.r_help())
    elif message.content.startswith('$penalty'):
        await pen(message.channel, message.author)


# @client.event
# async def on_reaction_add(reaction, user):
#     if reaction.emoji == "🏃":
client.run(TOKEN)

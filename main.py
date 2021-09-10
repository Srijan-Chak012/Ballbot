import discord
import os
import requests
import json
import random
import reply
import gif
import time
import help

client = discord.Client()

in_pen = False
score = 0
user = -1
l1 = -1
l2 = -1
x = -1


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

    await channel.send("l1 and l2: " + str(l1) + " " + str(l2))


async def prepare(channel, user):
    global l1, l2, x
    l1 = 33.33
    l2 = 66.66
    x = random.uniform(-3, 3)
    for i in range(10):
        await channel.send('React to this message with the side you want to shoot towards:')
        send = await channel.send(file=discord.File('./penalty.jpg'))
        await send.add_reaction("\N{Leftwards Black Arrow}")
        await send.add_reaction("\N{Upwards Black Arrow}")
        await send.add_reaction("\N{Black Rightwards Arrow}")
        await shoot(channel)
        await channel.send("Your score: " + str(score))


async def pen(channel, author):
    global in_pen
    global score
    global user
    if in_pen:
        await channel.send("Penalty shootout already in progress!")
        return
    in_pen = True
    score = 0
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
client.run('ODg0MTQwMjM2MjU3NDk3MDg4.YTUJwg.3o_7FjNYusz3yQSHmyT26s8Y1PQ')

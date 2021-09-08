import discord
import os
import requests
import json
import random
import reply
import gif
import help

client = discord.Client()

in_pen = False
score = 0
user = -1

async def shoot(channel):
    react, user = await client.wait_for('reaction_add')
    print(react)
    print(user)

async def prepare(channel, user):
    await channel.send('React to this message with the side you want to shoot towards:')
    send = await channel.send(file=discord.File('./penalty.jpg'))
    await send.add_reaction("\N{Leftwards Black Arrow}")
    await send.add_reaction("\N{Upwards Black Arrow}")
    await send.add_reaction("\N{Black Rightwards Arrow}")
    await shoot(channel)



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

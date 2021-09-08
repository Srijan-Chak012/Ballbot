import discord
import os
import requests
import json
import random
import reply
import gif
import help
import penalty


client = discord.Client()


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
        await penalty.pen(message.channel)

client.run('ODg0MTQwMjM2MjU3NDk3MDg4.YTUJwg.3o_7FjNYusz3yQSHmyT26s8Y1PQ')

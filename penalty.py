import random
import discord

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

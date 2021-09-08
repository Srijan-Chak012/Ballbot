import random
async def take(channel):
    send = await channel.send('''
    React to this message with the side you want to shoot towards:
https://thumbs.dreamstime.com/b/soccer-ball-penalty-spot-23651690.jpg''')
    await channel.send(send.id)

async def pen(channel):
    await take(channel)
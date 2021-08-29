const Discord = require('discord.js')
require("dotenv").config();

const { Client, Intents } = require('discord.js');

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

client.once('ready', () => {
    console.log('ballbot is online!')
});

const commandHandler = require("./commands");

client.on("message", commandHandler);

client.login(process.env.TOKEN);
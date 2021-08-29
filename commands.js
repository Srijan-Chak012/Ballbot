const gif = require("./gif");
const reply = require("./reply");
const help = require("./help");
const club = require("./club");


const commands = { reply, gif, help, club };

module.exports = async function (msg) {
  if (msg.channel.id == "881211935549423667") {
    let tokens = msg.content.split(" ");
    let command = tokens.shift();
    if (command.charAt(0) === ">") {
      command = command.substring(1);
      commands[command](msg, tokens);
    }
  }
};
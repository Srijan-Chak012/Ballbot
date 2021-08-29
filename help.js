module.exports = function (msg, args) {
    msg.channel.send(
`   
These are the supported commands:
Use '>' as prefix to access the commands
**:question: help** - Displays the help menu
**:sunglasses: gif <name>** - Disaplays gifs of your favourite players
**:wink: reply <name>** - My opinions on some of the most famous footballers
`
    );
};
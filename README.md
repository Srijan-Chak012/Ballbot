# Ballbot
A discord bot related to football, this bot enables you to have fun and gets you initiated with the game of football. You can play the penalty shootout against the bot or hear its opinions on some players!

## Functionalities
This bot has 4 functionalities to it:
1. Help
2. Gif 
3. Reply
4. Penalty

## Help:

This is a simple command when run will show a list of possible commands that the bot supports. A combination of emojis as well as the format of the discord command, the help command will display the information in a fun, intuitive way. 
The command is run as:
```
$help
```

## Gif:

Again a simple command that displays GIFs of your favorite players and teams. This uses the TENOR API to obtain the GIFs and is randomised to display different GIFs for common/popular phrases. 
The command is run as:
```
$gif <arguments>
```
where the arguments are the search parameters.

## Reply:

A fun command that gives you popular/unpopular opinionson famous players to take part in this delightful game. This however does not contain every footballer who has ever graced the game, but only a few popular ones. If you have any opinions you'd like to see go up,
reach out to me and tell me what you think!
The command is run as:
```
$reply <name>
```
where name is the name of the player you want to know about.

## Penalty:
A penalty shootout against the bot, the player first plays shoots and then plays as the goalkeeper to defend their goal. The ball can go one of 3 different ways and the player must shoot at a side where the bot keeper does not go and must defend on the side where the bot player shoots.
The input is taken as reactions on the pictures displayed by the bot on the channel. Win against the bot and show well you'd perform in an actual penalty-shootout! 
The command is run as:
```
$penalty
```

### The command to Run the bot is simply: 

```
$ python3 main.py
```


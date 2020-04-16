# Number Game
A game to play when you have free time. Lets you guess number the program generated in given range.

## System Requirements
The only requirement is to have Python 3 up and running.

## Installation
```
$ pip install number-game
```

## Usage
Example code on how to use:
```
>>> from number_game import Game
>>> game = Game() # default bounds (0-100)
>>> game.make_guess(10)
'Your guess is lower than the mystical number :('
>>> game.make_guess(90)
'Your guess is higher than the mystical number :('
>>> game.make_guess(82)
'You found it in 2 attempts!'
```
If you wish to specify lower and upper bounds for the game, you could initialize the game as follows:
```
>>> game = Game(10, 1000)
```
In this case the number the game comes up for you will be between 10 and 1000.

If you do not want to guess the current number, you can also shuffle the number again. In that case run the following:
```
>>> game.change_number() #if no args given, default 0-100 range
>>> game.change_number(30, 50) #the number will be in 30-50 range
```

## Motivation
The aim of the project is just fun.

## File Descriptions
The main part of the project is in number_game folder
game.py - The file containing Game class

## Licenses
The following package is free for use. Created by © Fidan Musazade 2020

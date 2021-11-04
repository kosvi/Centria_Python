# Snake (a computer game)

## Background

This game was made as an exercise to a Python course I took part at [Centria University of applied sciences](https://web.centria.fi/en). It's a first ever try out with Pygame, so please be undestanding when reading the code. I spend around 4-5 hours hacking this together. Code is nonsense, but the game *should* work. 

This game uses linked list to keep track of the snake cells. A smart programmer would probably just have used Pythons own data structures instead of making that horrible implementation of linked list. Also there is no clear separation of responsibilities between all the classes and the main.py -file. 

## Gameplay

Start the game by running [main.py](main.py). Use arrow keys to change the direction of the snake. 

At the beginning of the game the snake is standing still. You have to give it a direction for it to start moving. 

You cannot hit the borders of the screen. Instead the snake just jumps to the opposite side of the screen. 


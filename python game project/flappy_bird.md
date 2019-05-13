# Flappy Bird Game
This ia a python-based project for implementation of the classic flappy bird game using pygame package.
# Pygame package
Pygame is a cross-platform set of Python modules designed for writing video games.
It includes computer graphics and sound libraries designed to be used with the Python
programming language. It is built over the Simple DirectMedia Layer (SDL) library,
with the intention of allowing real-time computer game development without the lowlevel
mechanics of the C programming language and its derivatives. This is based on
the assumption that the most expensive functions inside games (mainly the graphics
part) can be abstracted from the game logic, making it possible to use a high-level
programming language, such as Python, to structure the game.Pygame was built to
replace PySDL after its development stalled. Pygame was originally written by Pete
Shinners and is released under the open source free software GNU Lesser General
Public License. It has been a community project since 2004 or 2005. There are many
tutorials and there are regular competitions to write little games using Python (and
usually but not necessarily, Pygame).
# Overview
In the game, the user will control the vertical velocity of the bird through keyboard or mouse button to make sure that the bird passes through the gaps between pipes. Each time the bird passes through the gap without hitting on either side of the pipe, the user will gain one point for that. The total points will be recorded as an evaluation of the game playing.
# Contents
 - the bird class
 - the pipe class
 - useful functions  
 The structure of the two classes can be shown as below:  
 ![image](https://github.com/RecursiveMatrix/course_projects/blob/master/python%20game%20project/screenshots/bird.jpg)
 ![image](https://github.com/RecursiveMatrix/course_projects/blob/master/python%20game%20project/screenshots/pipe.jpg)
 
# Rules
The game has one player. The player is supposed to manipulate the bird to climb.  
Game will be over if the bird collides with the pipe or hit the boundaries of the upper or lower window. Each time the bird completely passes through the gap between, one point will be gained. Besides, the user can press P for pausing the game and continue game using the same button. Also, the user could preset ESC button to terminate the game.

# Result
 ![image](https://github.com/RecursiveMatrix/course_projects/blob/master/python%20game%20project/screenshots/flappybird_demo.gif) 

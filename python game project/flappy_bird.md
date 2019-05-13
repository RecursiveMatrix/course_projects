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
 notations:  
x, y : the coordinates of the bird;  
ms_to_climb: the number of milliseconds left to climb;  
images: the images used for presenting the bird, in a form of tuple;  
_image.wingup, _image.wingdown: passing the images to these to initialize;  
_mask_wingup,_mask_wingdown: using mask function in pygame and initialize two mask objects with  
_image.wingup and _image.wingdown for detecting a collision;  
Def __init__ : construct function for class;  
Def update: using for updating the bird’s position, delta_frame indicates the number of frames since this method was last called;  
Def image: deciding when to show wing_up or wing_down image;  
Def mask: for detecting the collision;  
Def rect: return Rect object for pygame to store and manipulate with;  
Bird_image_width, bird_image_height: the width and height of the bird image;  
Sink_speed: the bird descends in one second, in pixels per millisecond;  
Climb_speed: the bird ascends in one second, in pixels per millisecond;  
Flying_duration_time: the number of milliseconds it takes the bird to execute a complete climb;  

Pipe_end_img, pipe_body_img: refer to the images used to construct pipe;  
x : represent the x coordinate of the pipe;  
score_counted: a Boolean value to indicate the states of recording score;  
total_num_pipe_body: the number of pipe body need to be built the whole pipe;  
num_pipe_top, num_pipe_bottom: the number of pipe body used to build the top pipe and bottom pipe;  
pos: the position of the bottom pipe;  
bottom_end_y: end position of the bottom pipe;  
bottom_end_piece_pos: position of the pipe end;  
top_end_y: end position of the top pipe;  
Def __init__ : construction function;  
Def top_height_x: calculate the x coordinate of the top pipe;  
Def bottom_height_x: calculate the x coordinate of the bottom pipe;  
Def visible: determine whether such pipe can be seen by user or not;  
Def rect: return a Rect object for pygame to store and manipulate with;  
Def update: update the position of the pipe;  
Def collides_with: return the result of collision;  
Pipe_width: the width of the pipe;  
Pipe_height: the height of the pipe;  
Interval_generating_pipe: time interval to add a new pair of pipes;  
Load images: return all the images used in a form of dictionary;  
Load image: taking the filename of the image and return the image;  
Frame_to_ms: convert frames to milliseconds with a given rate;  
Ms_to_frame: convert milliseconds to frame with a given rate;  

# Rules
The game has one player. The player is supposed to manipulate the bird to climb.  
Game will be over if the bird collides with the pipe or hit the boundaries of the upper or lower window. Each time the bird completely passes through the gap between, one point will be gained. Besides, the user can press P for pausing the game and continue game using the same button. Also, the user could preset ESC button to terminate the game.

# Result
 ![image](https://github.com/RecursiveMatrix/course_projects/blob/master/python%20game%20project/screenshots/flappybird_demo.gif) 

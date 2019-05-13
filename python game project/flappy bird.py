import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *


# Base constants

fps = 60                # frequency rate
Animation_speed = 0.2   # horizontal flying speed
window_width = 284*2   # the width of the window
window_height = 512     # the height of the window

class Bird(pygame.sprite.Sprite):

    bird_image_width = bird_image_height = 50
    speed_up = 0.3
    speed_down = 0.15
    flying_duration_time = 300

    def __init__(self,x,y,ms_to_climb,images):  # construct function

        super(Bird,self).__init__()             # pass the Bird class to its inherited class and initialize
        self.x, self.y = x, y
        self.ms_to_climb = ms_to_climb          # construct at the level of Bird class
        self._image_wingup, self._image_wingdown = images       # construct at the level of the father class
        self._mask_wingup = pygame.mask.from_surface(self._image_wingup)       # mask for later collision detection
        self._mask_wingdown = pygame.mask.from_surface(self._image_wingdown)


    def update(self, delta_frame = 1):          # update the bird's position, delat_frame indicates the number of frames
                                                # since this method was last called
        if self.ms_to_climb > 0 :               # if the bird is flying up


            percentage_motion_done = 1 - self.ms_to_climb/Bird.flying_duration_time      # percentage of the whole flying up motion
            self.y -= (Bird.speed_up * frame_to_ms(delta_frame) * (1 - math.cos(percentage_motion_done * math.pi)))
            # updating the bird position with the defined consine function


            self.ms_to_climb -= frame_to_ms(delta_frame)        # update the ms_to_climb accordingly
        else:
            self.y += Bird.speed_down * frame_to_ms(delta_frame)         # if the bird is flying down, just appling speed_down

    @property
    def image(self):        # deciding when to show wing_up or wing_down
        if pygame.time.get_ticks() % 300>=150:  # returns ms after pygame init()
            return self._image_wingdown
        else:
            return self._image_wingup

    @property
    def mask(self):         # for detecting the collision
        if pygame.time.get_ticks() % 300>=150:
            return self._mask_wingdown
        else:
            return self._mask_wingup

    @property               # return Rect object for pygame to store and manipulate rectangle ares
    def rect(self):
        return Rect(self.x,self.y,Bird.bird_image_width,Bird.bird_image_height)


class Pipe(pygame.sprite.Sprite):

    pipe_width = 80         # width and height of a pipe body, same size with the image of pipe body
    pipe_height = 32
    interval_generating_pipe = 2000         # time interval adding new pipes, in ms

    def __init__(self, pipe_end_img, pipe_body_img):

        self.x = float(window_width - 1)        # new pipe will be added
        self.score_counted = False
        self.image = pygame.Surface((Pipe.pipe_width,window_height), SRCALPHA)      # create a new image object, the pixel format will include a per-pixel alpha
        self.image.convert()
        self.image.fill((0,0,0,0))

        # calculate the number of pipe body need to use for construct a pipe
        total_num_pipe_body = int((window_height - 3 * Bird.bird_image_height - 3 * Pipe.pipe_height)/Pipe.pipe_height)
        # randomly generate number of top and bottom pipes in pair
        self.num_pipe_bottom = randint(1, total_num_pipe_body)
        self.num_pipe_top = total_num_pipe_body - self.num_pipe_bottom

        # for bottom pipe
        for i in range(1, self.num_pipe_bottom+1):

            # calculate the position of the bottom pipe
            pos = (0, window_height - i * Pipe.pipe_height)

            # show the constructed image for pipes with the pipe body image and number of that
            self.image.blit(pipe_body_img, pos)

        # calculate the end position of the pipe without end part
        bottom_end_y = window_height - self.bottom_height_x

        # decide the position of the pipe_end
        bottom_end_piece_pos = (0, bottom_end_y - Pipe.pipe_height)

        # constructed image
        self.image.blit(pipe_end_img, bottom_end_piece_pos)

        # for top pipe
        for i in range(self.num_pipe_top):
            self.image.blit(pipe_body_img,(0, i * Pipe.pipe_height))
        top_end_y = self.top_height_x
        self.image.blit(pipe_end_img, (0, top_end_y))


        # compensate for added end pieces
        self.num_pipe_top += 1
        self.num_pipe_bottom += 1

        # for collision detection
        self.mask = pygame.mask.from_surface(self.image)


    # get the top and bottom pipe's height in pixels
    @property
    def top_height_x(self):
        return self.num_pipe_top * Pipe.pipe_height

    @property
    def bottom_height_x(self):
        return self.num_pipe_bottom * Pipe.pipe_height


    # determine whether such pipe will be visible to user
    @property
    def visible(self):
        return -Pipe.pipe_width < self.x < window_width

    # construct Rect object for pygame to store and manipulate
    @property
    def rect(self):
        return Rect(self.x, 0, Pipe.pipe_width, Pipe.pipe_height)

    # update the pipes' position.
    def update(self, delta_frames=1):       # delta_frames: The number of frames elapsed since this method was last called.

        self.x -= Animation_speed * frame_to_ms(delta_frames)

    # check collision
    def collides_with(self, bird):
        return pygame.sprite.collide_mask(self, bird)


def load_images():

    def load_image(image_name):

        filename = os.path.join('.','images',image_name)
        image = pygame.image.load(filename)
        image.convert()

        return image

    return {

        'background': load_image('background.png'),
        'pipe-end': load_image('pipe_end.png'),
        'pipe-body': load_image('pipe_body.png'),
        # images for animating the flapping bird -- animated GIFs are
        # not supported in pygame
        'bird-wingup': load_image('bird_wing_up.png'),
        'bird-wingdown': load_image('bird_wing_down.png')

    }

# convert frames to milliseconds at the specified framerate
def frame_to_ms(frame,fps=fps):

    return 1000.0*frame/fps

# convert milliseconds to frames at the specified framerate
def ms_to_frame(ms,fps=fps):

    return ms*fps/1000.0


def main():

    # initialize the game.
    pygame.init()

    # set the size of the window and caption of the game
    display_game = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('Flappy Bird')

    # track the amount of time
    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont('arial',64,bold=True)

    images = load_images()

    bird_instance = Bird(50,int(window_height/2-Bird.bird_image_height/2),1,(images['bird-wingup'],images['bird-wingdown']))

    pipes = deque()
    score = 0
    frame_clock = 0
    done = False

    while not done:

        # update the clock
        clock.tick(fps)

        # if game is running, generating pipes for game
        if not frame_clock % ms_to_frame(Pipe.interval_generating_pipe):
            pp = Pipe(images['pipe-end'], images['pipe-body'])
            pipes.append(pp)

        # get the event, decide reactions with respect to each event
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                done = True
                break
            elif event.type == KEYUP and event.key == K_SPACE:
                bird_instance.ms_to_climb = Bird.flying_duration_time


        pipe_collision = any(p.collides_with(bird_instance) for p in pipes)

        # checking for the edge collision
        if pipe_collision or 0 >= bird_instance.y or bird_instance.y >= window_width - Bird.bird_image_height:
            done = True

        # showing the background image
        for x in (0, window_width / 2):
            display_game.blit(images['background'], (x, 0))

        # showing the expected pipes to user
        while pipes and not pipes[0].visible:
            pipes.popleft()

        # updating the pipes
        for p in pipes:
            p.update()
            display_game.blit(p.image, p.rect)

        # updating the bird
        bird_instance.update()
        display_game.blit(bird_instance.image, bird_instance.rect)

        # update and display score
        for p in pipes:
            if p.x + Pipe.pipe_width < bird_instance.x and not p.score_counted:
                score += 1
                p.score_counted = True



        # showing the score
        score_surface = score_font.render(str(score), True, (255, 255, 255))
        score_x = window_width / 2 - score_surface.get_width() / 2
        display_game.blit(score_surface, (score_x, Pipe.pipe_height))

        # update the full display surface to the screen
        pygame.display.flip()
        frame_clock += 1
    print('Game over! Score: %i' % score)
    pygame.quit()



if __name__ == '__main__':
    main()





import pygame
import os
from src.parameters import *


def load_block_image(name):
    return pygame.image.load(os.path.join("..", "images", name))


class Pipe:
    # Pipes images
    LEFT_BODY_PIPE = load_block_image('left_body_pipe.png')
    LEFT_HEAD_PIPE = load_block_image('left_head_pipe.png')
    RIGHT_BODY_PIPE = load_block_image('right_body_pipe.png')
    RIGHT_HEAD_PIPE = load_block_image('right_head_pipe.png')
    UPPER_LEFT_BODY_PIPE = load_block_image('upper_left_body_pipe.png')
    UPPER_LEFT_HEAD_PIPE = load_block_image('upper_left_head_pipe.png')
    UPPER_RIGHT_BODY_PIPE = load_block_image('upper_right_body_pipe.png')
    UPPER_RIGHT_HEAD_PIPE = load_block_image('upper_right_head_pipe.png')

    # Parts pipes
    BODY = LEFT_BODY_PIPE, RIGHT_BODY_PIPE
    HEAD = LEFT_HEAD_PIPE, RIGHT_HEAD_PIPE
    UPPER_BODY = UPPER_RIGHT_BODY_PIPE, UPPER_LEFT_BODY_PIPE
    UPPER_HEAD = UPPER_RIGHT_HEAD_PIPE, UPPER_LEFT_HEAD_PIPE

    def __init__(self, begin_aperture, x):
        self.begin_aperture = begin_aperture
        self.distance_aperture = 4
        self.x = x

    def draw(self, screen):
        y = 0
        i = 0

        # Upper body pipe
        while i + 1 < self.begin_aperture:
            self.draw_part_pipe(screen, y, Pipe.UPPER_BODY)
            y += ELEMENT_SIZE
            i += 1

        # Upper head pipe
        self.draw_part_pipe(screen, y, Pipe.UPPER_HEAD)
        y += (1 + self.distance_aperture) * ELEMENT_SIZE
        i += 1 + self.distance_aperture

        # Head pipe
        self.draw_part_pipe(screen, y, Pipe.HEAD)
        y += ELEMENT_SIZE
        i += 1

        # Body pipe
        while i < DISTANCE_PIPE:
            self.draw_part_pipe(screen, y, Pipe.BODY)
            y += ELEMENT_SIZE
            i += 1

    def draw_part_pipe(self, screen, y, part_pipe):
        screen.blit(part_pipe[0], (self.x, y))
        screen.blit(part_pipe[1], (self.x + ELEMENT_SIZE, y))

    def get_range_aperture(self):
        return self.begin_aperture * ELEMENT_SIZE,\
               (self.begin_aperture + self.distance_aperture) * ELEMENT_SIZE

    def move(self, x):
        self.x -= x

    def is_needed(self):
        return self.x > -2 * ELEMENT_SIZE

    def is_hidden(self):
        return self.x >= WIDTH

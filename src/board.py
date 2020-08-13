import pygame
import os
from src.block import Block
from src.parameters import *


def load_block_image(name):
    return pygame.image.load(os.path.join("..", "images", name))


class Board:
    # Pipes images
    LEFT_BODY_PIPE = load_block_image('left_body_pipe.png')
    LEFT_HEAD_PIPE = load_block_image('left_head_pipe.png')
    RIGHT_BODY_PIPE = load_block_image('right_body_pipe.png')
    RIGHT_HEAD_PIPE = load_block_image('right_head_pipe.png')
    UPPER_LEFT_BODY_PIPE = load_block_image('upper_left_body_pipe.png')
    UPPER_LEFT_HEAD_PIPE = load_block_image('upper_left_head_pipe.png')
    UPPER_RIGHT_BODY_PIPE = load_block_image('upper_right_body_pipe.png')
    UPPER_RIGHT_HEAD_PIPE = load_block_image('upper_right_head_pipe.png')

    @staticmethod
    def get_list_chars(path_world):
        file = open(path_world, "r")
        list_chars = []
        for line in file:
            line = line[0:-1]
            list_chars.append(line)
        file.close()
        return list_chars

    @staticmethod
    def get_list_blocks(path_world):
        chars = Board.get_list_chars(path_world)
        list_blocks = []
        before_first_part_pipe = True
        for i in range(len(chars)):
            blocks = []
            if chars[i][0] == '*':
                for _ in range(len(chars[i])):
                    blocks.append(Block(None))
            else:
                if before_first_part_pipe:
                    before_first_part_pipe = False
                    j = 0
                    # Upper right body pipe
                    while chars[i][j + 1] == 'p':
                        blocks.append(Block(Board.UPPER_RIGHT_BODY_PIPE))
                        j += 1
                    # Upper right head pipe
                    blocks.append(Block(Board.UPPER_RIGHT_HEAD_PIPE))
                    j += 1
                    while chars[i][j] == '*':
                        blocks.append(Block(None))
                        j += 1
                    # Left head pipe
                    blocks.append(Block(Board.LEFT_HEAD_PIPE))
                    j += 1
                    # Left body pipe
                    while j < len(chars[i]):
                        blocks.append(Block(Board.LEFT_BODY_PIPE))
                        j += 1
                else:
                    before_first_part_pipe = True
                    j = 0
                    # Upper left body pipe
                    while chars[i][j + 1] == 'p':
                        blocks.append(Block(Board.UPPER_LEFT_BODY_PIPE))
                        j += 1
                    # Upper left head pipe
                    blocks.append(Block(Board.UPPER_LEFT_HEAD_PIPE))
                    j += 1
                    while chars[i][j] == '*':
                        blocks.append(Block(None))
                        j += 1
                    # Right head pipe
                    blocks.append(Block(Board.RIGHT_HEAD_PIPE))
                    j += 1
                    # Right body pipe
                    while j < len(chars[i]):
                        blocks.append(Block(Board.RIGHT_BODY_PIPE))
                        j += 1
            list_blocks.append(blocks)
        return list_blocks

    def __init__(self, path_world):
        self.blocks = Board.get_list_blocks(path_world)

    def draw(self, screen, x):
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                position = i * ELEMENT_SIZE - x, j * ELEMENT_SIZE
                if -ELEMENT_SIZE <= position[0] <= WIDTH and -ELEMENT_SIZE <= position[1] <= HEIGHT:
                    self.blocks[i][j].draw(screen, position)

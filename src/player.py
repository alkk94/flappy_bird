import pygame
import os
from src.parameters import *


class Player:
    START_POSITION = (WIDTH // 2 - ELEMENT_SIZE, HEIGHT // 2 - ELEMENT_SIZE)
    JUMP_MAX = 2 * ELEMENT_SIZE
    JUMP_SPEED = 4
    FALL_SPEED = 4
    FLAPPY_BIRD = pygame.image.load(os.path.join("..", "images", "flappy_bird.png"))

    def __init__(self):
        self.x = Player.START_POSITION[0]
        self.y = Player.START_POSITION[1]
        self.isJump = False
        self.jumpCount = 0
        self.mask = pygame.mask.from_surface(Player.FLAPPY_BIRD)

    def draw(self, screen):
        screen.blit(Player.FLAPPY_BIRD, (self.x, self.y))

    def jump(self):
        self.y += -Player.JUMP_SPEED
        self.jumpCount += Player.JUMP_SPEED

    def fall(self):
        self.y += Player.FALL_SPEED

    def begin_jump(self):
        self.isJump = True
        self.jumpCount = 0

    def move(self):
        if self.isJump:
            self.jump()
            if self.jumpCount == Player.JUMP_MAX:
                self.isJump = False
        else:
            self.fall()

    def is_lose(self):
        return self.y < 0 or self.y > (DISTANCE_PIPE - 1) * ELEMENT_SIZE

    def get_position(self):
        return self.x, self.y

import pygame
import os
from src.player import Player
from src.board import Board
from src.parameters import *


class Game:
    # Game parameters.
    RESOLUTION = WIDTH, HEIGHT
    FPS = 60
    GAME_SPEED = 4

    # Background
    BG = pygame.image.load(os.path.join("..", "images", "bg.png"))

    pygame.init()
    pygame.display.set_caption('Flappy Bird')

    # Jump sound
    JUMP_SOUND = pygame.mixer.Sound(os.path.join("..", "sounds", "jump.wav"))

    def __init__(self):
        self.run = True
        self.player = Player()
        self.board = Board(os.path.join("..", "worlds", "world1.txt"))
        self.screen = pygame.display.set_mode(Game.RESOLUTION)
        self.clock = pygame.time.Clock()
        self.x = 0

        self.execute()

    def execute(self):
        while self.run:
            self.handle_events()
            self.ticking()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP):
                self.player.begin_jump()
                Game.JUMP_SOUND.play()

    def ticking(self):
        self.clock.tick(Game.FPS)
        self.player.move()
        self.move()

    def draw(self):
        self.screen.blit(Game.BG, (0, 0))
        self.board.draw(self.screen, self.x)
        self.player.draw(self.screen)
        pygame.display.update()

    def move(self):
        self.x += Game.GAME_SPEED

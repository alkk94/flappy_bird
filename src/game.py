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

    # Sounds
    JUMP_SOUND = pygame.mixer.Sound(os.path.join("..", "sounds", "jump.wav"))

    def __init__(self):
        self.run = True
        self.player = Player()
        self.board = Board(os.path.join("..", "worlds", "world.txt"))
        self.screen = pygame.display.set_mode(Game.RESOLUTION)
        self.clock = pygame.time.Clock()

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
        self.board.move(Game.GAME_SPEED)
        self.player.move()
        if self.player.is_off_board():
            self.run = False
        if self.board.is_collision(self.player.get_position()):
            self.run = False

    def draw(self):
        self.screen.blit(Game.BG, (0, 0))
        self.board.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.update()

from src.pipe import Pipe
from src.parameters import *


class Board:
    @staticmethod
    def get_list_pipes(path_world):
        file = open(path_world, 'r')
        list_pipes = []
        x = 3 * WIDTH // 2
        for line in file:
            begin_aperture = int(line)
            list_pipes.append(Pipe(begin_aperture, x))
            x += 6 * ELEMENT_SIZE
        return list_pipes

    def __init__(self, path_world):
        self.pipes = Board.get_list_pipes(path_world)

    def draw(self, screen):
        for pipe in self.pipes:
            if pipe.is_hidden():
                break
            else:
                pipe.draw(screen)

    def move(self, x):
        for pipe in self.pipes:
            pipe.move(x)
        if not self.pipes[0].is_needed():
            self.pipes.pop(0)

    def is_collision(self, player_position):
        for pipe in self.pipes:
            if player_position[0] + ELEMENT_SIZE < pipe.x:
                return False
            elif pipe.is_player_in_range_pipe(player_position[0]):
                return pipe.is_collision(player_position[1])

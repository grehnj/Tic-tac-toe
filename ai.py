from settings import *
from victory import check_if_victory
import random
import time


class Opponent:
    def __init__(self):
        self.start_time = None
        self.move_to_square = None
        self.deciding = False
        self.opponents_turn = False

    def decide(self):
        available_squares = []
        for i in range(len(grid_pos)):
            if all_positions.count(i) > 0:
                continue
            else:
                available_squares.append(i)

        self.move_to_square = available_squares[random.randint(0, len(available_squares) - 1)]

    def place_mark(self):
        if self.deciding:
            if time.time() - self.start_time > 1:
                all_positions.append(self.move_to_square)
                o_positions.append(self.move_to_square)
                self.opponents_turn = False
                self.deciding = False
                if check_if_victory(o_positions, False):
                    return False
        else:
            self.deciding = True
            self.start_time = time.time()
            self.decide()
        return True

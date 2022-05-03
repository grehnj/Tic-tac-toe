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

        # bot makes winning move if it has two marks on the same line:
        if self.calc_placement(o_positions, x_positions, 2):
            # bot stops player if player has two marks on the same line:
            if self.calc_placement(x_positions, o_positions, 2):
                # bot adds a second mark if it already has one on a line:
                if self.calc_placement(o_positions, x_positions, 1):
                    # bot breaks players line if player has one mark on a line:
                    if self.calc_placement(x_positions, o_positions, 1):
                        # bot places a mark at random
                        self.move_to_square = available_squares[random.randint(0, len(available_squares) - 1)]

    def calc_placement(self, position_list, other_position_list, goal):
        for combo in winning_combos:
            missing_nums = []
            matches = 0
            i = 0
            for number in combo:
                i += 1
                if other_position_list.count(number):
                    break
                if position_list.count(number):
                    matches += 1
                else:
                    missing_nums.append(number)
                if matches >= goal and i >= 3:
                    self.move_to_square = missing_nums[0]
                    return False
        return True

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

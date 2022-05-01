from settings import *


def check_if_victory(position_list, is_player):
    for combo in winning_combos:
        matches = 0
        for number in combo:
            if position_list.count(number):
                matches += 1
            if matches >= 3:
                if is_player:
                    print('YOU WIN!')
                else:
                    print('YOU LOSE!')
                return True
    return False

from settings import *

win = False
lose = False


def check_if_victory(position_list, is_player):
    global win, lose

    for combo in winning_combos:
        matches = 0
        for number in combo:
            if position_list.count(number):
                matches += 1
            if matches >= 3:
                if is_player:
                    win = True
                else:
                    lose = True
                return True
    return False


def get_result_msg():
    if win:
        return 'YOU WIN!'
    elif lose:
        return 'YOU LOSE!'
    else:
        return 'IT\'S A TIE!'


from settings import *

win = False
lose = False


def check_if_victory(position_list, is_player):
    global win, lose

    if check_positions(position_list, 3):
        if is_player:
            win = True
        else:
            lose = True
        return True
    else:
        return False


def check_positions(position_list, goal):
    for combo in winning_combos:
        matches = 0
        for number in combo:
            if position_list.count(number):
                matches += 1
            if matches >= goal:
                return True


def get_result_msg():
    if win:
        return 'YOU WIN!'
    elif lose:
        return 'YOU LOSE!'
    else:
        return 'IT\'S A TIE!'


def reset_victory():
    global win, lose

    win = False
    lose = False


import random

import pygame
import sys
from ai import Opponent
from victory import *

# initialization
pygame.init()
screen = pygame.display.set_mode((window_size, window_size))  # use tuple to set resolution
icon = pygame.image.load('graphics/icon.png')
grid = pygame.image.load('graphics/grid.png')
x_img = pygame.image.load('graphics/x.png')
o_img = pygame.image.load('graphics/o.png')
pygame.display.set_caption("Joakim's Tic-tac-toe game")
pygame.display.set_icon(icon)
font_big = pygame.font.Font('freesansbold.ttf', 38)
font_small = pygame.font.Font('freesansbold.ttf', 26)
interactive_rect = (139, 251, 149, 38)
interactive_colors = ((41, 160, 13), (53, 206, 16))
interactive_index = 0

playing = True
opponent = Opponent()

clock = pygame.time.Clock()


def get_mouse_pos():
    pos = pygame.mouse.get_pos()

    for i in range(len(grid_pos)):
        if grid_pos[i][0] < pos[0] < grid_pos[i][0] + square_size:
            if grid_pos[i][1] < pos[1] < grid_pos[i][1] + square_size:
                if x_positions.count(i) > 0 or o_positions.count(i) > 0:
                    return

                all_positions.append(i)
                x_positions.append(i)
                opponent.opponents_turn = True


def draw_marks(position_list, image):
    for i in position_list:
        screen.blit(image, (grid_pos[i][0] + size_margin, grid_pos[i][1] + size_margin))


def draw_text(msg):
    text_render = font_big.render(msg, True, (255, 255, 255))
    text_rect = text_render.get_rect(center=(window_size / 2, window_size / 2))

    button_render = font_small.render('Play again!', True, (255, 255, 255))
    button_rect = button_render.get_rect(center=(window_size / 2, window_size / 2 + 57))

    bg_rect = (text_rect[0] - 5, text_rect[1] - 5, text_rect[2] + 10, text_rect[3] + 10)
    create_rect(text_render, text_rect, bg_rect, (247, 207, 26))
    create_rect(button_render, button_rect, interactive_rect, interactive_colors[interactive_index])


def create_rect(render, rect, bg_rect, color):
    pygame.draw.rect(screen, color, bg_rect)
    screen.blit(render, rect)


def check_if_button():
    mouse_pos = pygame.mouse.get_pos()
    if interactive_rect[0] < mouse_pos[0] < interactive_rect[0] + interactive_rect[2]:
        if interactive_rect[1] < mouse_pos[1] < interactive_rect[1] + interactive_rect[3]:
            return True
    return False


def restart_game():
    global playing, opponent

    x_positions.clear()
    o_positions.clear()
    all_positions.clear()
    reset_victory()

    playing = True
    opponent = Opponent()


# game loop
while True:
    screen.fill((246, 246, 212))  # fill background color
    screen.blit(grid, (12, 12))

    draw_marks(x_positions, x_img)
    draw_marks(o_positions, o_img)
    if not playing:
        if check_if_button():
            interactive_index = 1
        else:
            interactive_index = 0
        draw_text(get_result_msg())

    if len(all_positions) >= len(grid_pos) and playing:
        playing = False

    if opponent.opponents_turn and playing:
        playing = opponent.place_mark()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user clicks window close button
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and playing and not opponent.opponents_turn:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                get_mouse_pos()
                if check_if_victory(x_positions, True):
                    playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not playing:
            if check_if_button():
                restart_game()

    pygame.display.update()
    clock.tick(30)  # cap fps at 30

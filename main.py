import random

import pygame
import sys
from ai import Opponent
from settings import *
from victory import check_if_victory

# initialization
pygame.init()
screen = pygame.display.set_mode((426, 426))  # use tuple to set resolution
icon = pygame.image.load('graphics/icon.png')
grid = pygame.image.load('graphics/grid.png')
x_img = pygame.image.load('graphics/x.png')
o_img = pygame.image.load('graphics/o.png')
pygame.display.set_caption("Joakim's Tic-tac-toe game")
pygame.display.set_icon(icon)

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


# game loop
while True:
    screen.fill((246, 246, 212))  # fill background color
    screen.blit(grid, (12, 12))

    draw_marks(x_positions, x_img)
    draw_marks(o_positions, o_img)

    if len(all_positions) >= len(grid_pos) and playing:
        print('IT\'S A TIE!')
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

    pygame.display.update()
    clock.tick(30)  # cap fps at 30

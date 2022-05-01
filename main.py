import pygame
import sys
import random
from settings import *

# initialization
pygame.init()
screen = pygame.display.set_mode((426, 426))  # use tuple to set resolution
pygame.display.set_caption("Joakim's Tic-tac-toe game")
grid = pygame.image.load('graphics/grid.png')
x_img = pygame.image.load('graphics/x.png')
o_img = pygame.image.load('graphics/o.png')
clock = pygame.time.Clock()


def get_mouse_pos():
    pos = pygame.mouse.get_pos()

    for i in range(len(grid_pos)):
        if grid_pos[i][0] < pos[0] < grid_pos[i][0] + square_size:
            if grid_pos[i][1] < pos[1] < grid_pos[i][1] + square_size:
                if x_positions.count(i) > 0 or o_positions.count(i) > 0:
                    return

                if random.randint(0, 1):
                    x_positions.append(i)
                else:
                    o_positions.append(i)


def draw_marks(position_list, image):
    for i in position_list:
        screen.blit(image, (grid_pos[i][0] + size_margin, grid_pos[i][1] + size_margin))


# game loop
while True:
    screen.fill((246, 246, 212))  # fill background color
    screen.blit(grid, (12, 12))

    draw_marks(x_positions, x_img)
    draw_marks(o_positions, o_img)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user clicks window close button
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                get_mouse_pos()

    pygame.display.update()
    clock.tick(30)  # cap fps at 30

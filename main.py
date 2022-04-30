import pygame
import sys

# initialization
pygame.init()
screen = pygame.display.set_mode((400, 400))  # use tuple to set resolution
pygame.display.set_caption("Joakim's Tic-tac-toe game")
clock = pygame.time.Clock()

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user clicks window close button
            pygame.quit()
            sys.exit()

    screen.fill((246, 246, 212))  # fill background color

    pygame.display.update()
    clock.tick(30)  # cap fps at 30

import pygame
import random

pygame.init()

#game window
screen_width = 800
screen_height = 450

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Crochet Pattern Maker')

run = True
while run:
    screen.fill((0, 255, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
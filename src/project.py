import pygame
import random

pygame.init()

#game window
screen_width = 800
screen_height = 450

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Crochet Pattern Maker')

#test boxes, replace with crochet stitches later
active_box = None
images = []
for i in range(5):
    x = random.randint(50, 700)
    y = random.randint(50, 350)
    w = random.randint(35, 65)
    h = random.randint(35, 65)
    box = pygame.Rect(x, y, w, h)
    images.append(box)

run = True
while run:
    screen.fill((0, 255, 0))
    purple = (255, 0, 0)

    #update and draw items
    for box in images:
        pygame.draw.rect(screen, purple, box)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
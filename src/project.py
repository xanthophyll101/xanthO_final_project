import pygame
    

pygame.init()

#game window
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Crochet Pattern Maker')
clock = pygame.time.Clock()

dt = 0
mouse_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


run = True
while run:
        
    screen.fill("#8fa9cc")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #circle & moving the circle
    pygame.draw.circle(screen, "#b33e3e", mouse_pos, 40)

    if pygame.mouse.get_pressed()[0]:
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            mouse_pos.x = pos[0]
            mouse_pos.y = pos[1]


    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()
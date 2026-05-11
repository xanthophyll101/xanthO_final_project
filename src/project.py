import pygame
import random
    

pygame.init()

#game window
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Crochet Pattern Maker')
chain_st_img = pygame.image.load('one-chain-stitch-symbol.jpg')
chain_img_width, chain_img_height = 50, 50
chain_st = pygame.transform.scale(chain_st_img, (chain_img_width, chain_img_height))

#test boxes, replace with crochet stitches later
active_box = None
# images = []
# for i in range(5):
#     x = random.randint(35, 65)
#     y = random.randint(35, 65)
#     chain = (chain_st, (x,y))
#     images.append(chain)

run = True
while run:
    screen.fill((0, 255, 0))
    purple = (255, 0, 0)

    #screen.blit(chain_st, (0,0))

    #update and draw items
    screen.blit(chain_st)

    pygame.display.flip()

    for event in pygame.event.get():

        #check for left mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                player_pos.x = pos[0]
                player_pos.y = pos[1]
                for num, chain in enumerate(images):
                    if chain.collidepoint(event.pos):
                        active_box = num

        #check for stop clicking box
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                #Move the image
                
                active_box = None

        #check for mouse movement
        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                images[active_box].move_ip(event.rel)


        if event.type == pygame.QUIT:
            run = False
import pygame
    

pygame.init()

#game window
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Crochet Pattern Maker')
clock = pygame.time.Clock()

#load button images
chain_button_img = pygame.image.load('chain_button.jpg')
singleCR_button_img = pygame.image.load('singleCR_button.jpg')
doubleCR_button_img = pygame.image.load('doubleCR_button.jpg')

dt = 0
mouse_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#Button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))


#create button instances
chain_button = Button(100, 200, chain_button_img)
singleCR_button = Button(250, 200, singleCR_button_img)
doubleCR_button = Button(400, 200, doubleCR_button_img)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("#8fa9cc")

    chain_button.draw()
    singleCR_button.draw()
    doubleCR_button.draw()

    #circle & moving the circle
    #pygame.draw.circle(screen, "#b33e3e", mouse_pos, 40)

    if pygame.mouse.get_pressed()[0]:
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            mouse_pos.x = pos[0]
            mouse_pos.y = pos[1]


    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()
import pygame
    

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):

        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            action = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


def main():
    #initialize screen & clock
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Crochet Pattern Maker')
    clock = pygame.time.Clock()

    #buttons
    chain_button_img = pygame.image.load('chain_button.jpg')
    singleCR_button_img = pygame.image.load('singleCR_button.jpg')
    doubleCR_button_img = pygame.image.load('doubleCR_button.jpg')
    #create button instances
    chain_button = Button(100, 200, chain_button_img, 2)
    singleCR_button = Button(250, 200, singleCR_button_img, 2)
    doubleCR_button = Button(400, 200, doubleCR_button_img, 2)

    dt = 0
    mouse_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    #event loop - put everything that renders onscreen here
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill("#8fa9cc")

        if chain_button.draw(screen):  #basically if action == True
            print("Action works! Yay!")
        if singleCR_button.draw(screen):
            print('singleCR works!')
        if doubleCR_button.draw(screen):
            print('doubleCr works!')

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


if __name__ == '__main__':
    main()
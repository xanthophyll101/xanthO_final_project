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


class Chain(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

        #testing new movement
        self.movex = 0 
        self.movey = 0 
        self.frame = 0 #count frames

    def control(self, x, y): #control player movement
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey


def getStitchPosition(pos, group):
    for i, stitch in enumerate(group):
        if stitch.rect.collidepoint(pos):
            active_stitch = i
            return active_stitch
    return False

        
                
def main():
    #initialize screen & clock
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Crochet Pattern Maker')

    #framerate
    clock = pygame.time.Clock()
    FPS = 60

    #buttons
    chain_button_img = pygame.image.load('chain_button.jpg')
    singleCR_button_img = pygame.image.load('singleCR_button.jpg')
    doubleCR_button_img = pygame.image.load('doubleCR_button.jpg')
    #create button instances
    chain_button = Button(100, 200, chain_button_img, 2)
    singleCR_button = Button(250, 200, singleCR_button_img, 2)
    doubleCR_button = Button(400, 200, doubleCR_button_img, 2)

    #stitch instances
    chain_obj = Chain(400, 300, chain_button_img, 0.8)

    #sprite group
    chains_list = pygame.sprite.Group()
    chains_list.add(chain_obj)
    steps = 10
    #chains_list = chains.sprites()

    dt = 0

    #starting state - select buttons & different sprites
    state = 'Select Mode'

    #event loop - put everything that renders onscreen here
    run = True
    while run:

        clock.tick(FPS)

        screen.fill("#8fa9cc")

        #update sprite group
        chain_obj.update()
        chains_list.update()

        #draw sprite group
        chains_list.draw(screen)

        if chain_button.draw(screen):  #basically if action == True
            print(chains_list)
        if singleCR_button.draw(screen):
            print('singleCR works!')
        if doubleCR_button.draw(screen):
            print('doubleCr works!')


        #event handler
        for event in pygame.event.get():
            if state == "Select Mode":
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if chain_button.rect.collidepoint(pos):
                            chain_obj = Chain(400, 300, chain_button_img, 0.8)
                            chains_list.add(chain_obj)

                        if chain_obj.rect.collidepoint(pos):
                            active_obj_idx = getStitchPosition(pos, chains_list)
                            current_list = chains_list.sprites()
                            active_obj = current_list[active_obj_idx]
                            chain_obj = active_obj

                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFTBRACKET:
                        state = "Edit Mode"
                        print("switch once!")
    
            if state == "Edit Mode":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        chain_obj.control(-steps, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        chain_obj.control(steps, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        chain_obj.control(0, -steps)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        chain_obj.control(0, steps)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        chain_obj.control(steps, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        chain_obj.control(-steps, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        chain_obj.control(0, steps)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        chain_obj.control(0, -steps)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHTBRACKET:
                        state = "Select Mode"
                        print("switched back!")

            if event.type == pygame.QUIT:
                run = False


        pygame.display.flip()



    pygame.quit()


if __name__ == '__main__':
    main()
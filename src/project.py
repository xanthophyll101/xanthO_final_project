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


class Stitch(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale):
        super().__init__()
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


def getMostRecentObj(imported_list):
    try:
        most_recent_obj = imported_list.sprites()[-1]
        return most_recent_obj
    except IndexError:
        return
    
def isButtonPressed(button, pos):
    if button.rect.collidepoint(pos) == True:
        return True
    else:
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

    #sprite groups
    # chains_list = pygame.sprite.Group()
    # singleCR_list = pygame.sprite.Group()
    # doubleCR_list = pygame.sprite.Group()
    stitch_list = pygame.sprite.Group()

    dt = 0
    steps = 10
    #starting state - select buttons & different sprites
    state = 'Select Mode'

    #event loop - put everything that renders onscreen here
    run = True
    while run:

        clock.tick(FPS)

        screen.fill("#8fa9cc")

        #update sprite group
        # chains_list.update()
        # singleCR_list.update()
        # doubleCR_list.update()
        stitch_list.update()

        #draw sprite group
        # chains_list.draw(screen)
        # singleCR_list.draw(screen)
        # doubleCR_list.draw(screen)
        stitch_list.draw(screen)

        if chain_button.draw(screen):  #basically if action == True
            print("Chain button")
        if singleCR_button.draw(screen):
            print("SingleCR button")
        if doubleCR_button.draw(screen):
            print("DoubleCR button")

        #event handler
        for event in pygame.event.get():
            if state == "Select Mode":
                pos = pygame.mouse.get_pos()
                chain_obj = Stitch(400, 300, chain_button_img, 0.8)
                singleCR_obj = Stitch(400, 300, singleCR_button_img, 0.8)
                doubleCR_obj = Stitch(400, 300, doubleCR_button_img, 0.8)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if isButtonPressed(chain_button, pos):
                            stitch_list.add(chain_obj)
                        elif isButtonPressed(singleCR_button, pos):
                            stitch_list.add(singleCR_obj)
                        elif isButtonPressed(doubleCR_button, pos):
                            stitch_list.add(doubleCR_obj)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFTBRACKET:
                        state = "Edit Mode"
                        print("switch once!")
    
            if state == "Edit Mode":
                
                obj = getMostRecentObj(stitch_list)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        obj.control(-steps, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        obj.control(steps, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        obj.control(0, -steps)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        obj.control(0, steps)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        obj.control(steps, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        obj.control(-steps, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        obj.control(0, steps)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        obj.control(0, -steps)

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
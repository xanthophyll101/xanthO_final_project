import pygame
import math


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
        self.og_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = self.og_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

        #testing new movement
        self.movex = 0 
        self.movey = 0 
        self.angle = 0
        self.change_angle = 0
        self.frame = 0 #count frames

    def rotate(self):
        self.image = pygame.transform.rotate(self.og_image, self.angle)
        self.angle += self.change_angle
        self.angle = self.angle % 360
        self.rect = self.image.get_rect(center=self.rect.center)

    def control(self, x, y, angle): #control player movement
        self.movex += x
        self.movey += y
        self.change_angle += angle

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.angle = self.angle + self.change_angle


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

        stitch_list.update()

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
                        obj.control(-steps, 0, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        obj.control(steps, 0, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        obj.control(0, -steps, 0)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        obj.control(0, steps, 0)
                    if event.key == pygame.K_o:
                        obj.control(0, 0, -steps)
                        print("rotating")

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        obj.control(steps, 0, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        obj.control(-steps, 0, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        obj.control(0, steps, 0)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        obj.control(0, -steps, 0)
                    if event.key == pygame.K_o:
                        obj.control(0, 0, steps)
                        print("stop rotating")

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
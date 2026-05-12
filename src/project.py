import pygame


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.smoothscale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        action = False

        pos = pygame.mouse.get_pos()
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
    
    def render(self, screen):
        self.export = pygame.image.save(screen, "Crochet_Pattern.jpg")


class Stitch(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale):
        super(Stitch, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.og_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = self.og_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.center = self.rect.center
        self.clicked = False
        self.movex = 0 
        self.movey = 0 
        self.angle = 0
        self.change_angle = 0
        self.frame = 0 #count frames

    def control_move(self, x, y, angle):
        self.movex += x
        self.movey += y
        self.change_angle += angle

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.image = pygame.transform.rotate(self.og_image, self.angle)
        self.angle += self.change_angle
        self.rect = self.image.get_rect(center=self.rect.center)


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
    screen_width = 1200
    screen_height = 900
    move_pix = 5
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Crochet Pattern Maker')

    #framerate
    clock = pygame.time.Clock()
    FPS = 60

    #buttons
    chain_button_img = pygame.image.load('chain.png').convert_alpha()
    singleCR_button_img = pygame.image.load('single-crochet.png').convert_alpha()
    doubleCR_button_img = pygame.image.load('double_crochet.png').convert_alpha()
    render_button_img = pygame.image.load('rendering-button.jpg')

    #create button instances
    chain_button = Button(100, 200, chain_button_img, 0.05)
    singleCR_button = Button(250, 200, singleCR_button_img, 0.05)
    doubleCR_button = Button(400, 200, doubleCR_button_img, 0.05)
    render_button = Button(50, 500, render_button_img, 0.05)

    stitch_list = pygame.sprite.Group()

    dt = 0
    #starting state - select buttons & different sprites
    state = 'Select Mode'

    #event loop
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
        if render_button.draw(screen):
            print("rendering works!")

        #event handler
        for event in pygame.event.get():
            if state == "Select Mode":
                pos = pygame.mouse.get_pos()
                chain_obj = Stitch(400, 300, chain_button_img, 0.05)
                singleCR_obj = Stitch(400, 300, singleCR_button_img, 0.05)
                doubleCR_obj = Stitch(400, 300, doubleCR_button_img, 0.05)

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
                        obj.control_move(-move_pix, 0, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        obj.control_move(move_pix, 0, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        obj.control_move(0, -move_pix, 0)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        obj.control_move(0, move_pix, 0)
                    if event.key == pygame.K_o:
                        obj.control_move(0, 0, move_pix)
                    if event.key == pygame.K_p:
                        obj.control_move(0, 0, -move_pix)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        obj.control_move(move_pix, 0, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        obj.control_move(-move_pix, 0, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        obj.control_move(0, move_pix, 0)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        obj.control_move(0, -move_pix, 0)
                    if event.key == pygame.K_o:
                        obj.control_move(0, 0, -move_pix)
                    if event.key == pygame.K_p:
                        obj.control_move(0, 0, move_pix)

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
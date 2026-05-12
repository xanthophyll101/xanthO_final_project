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
        self.export = pygame.image.save(screen, "Crochet_PatternSS.jpg")


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

    #button/gui images
    chain_button_img = pygame.image.load('chain.png').convert_alpha()
    singleCR_button_img = pygame.image.load('single-crochet.png').convert_alpha()
    doubleCR_button_img = pygame.image.load('double_crochet.png').convert_alpha()
    render_button_img = pygame.image.load('rendering-button-quality.png').convert_alpha()
    toolbar_background_img = pygame.image.load('toolbar_background.png').convert_alpha()
    borderD_img = pygame.image.load('border.png').convert_alpha()
    borderU_img = pygame.image.load('border-top.png').convert_alpha()
    borderL_img = pygame.image.load('border-left.png').convert_alpha()
    borderR_img = pygame.image.load('border-right.png').convert_alpha()

    #create button/other gui instances
    chain_button = Button(85, 75, chain_button_img, 0.08)
    singleCR_button = Button(182, 60, singleCR_button_img, 0.08)
    doubleCR_button = Button(280, 60, doubleCR_button_img, 0.065)
    render_button = Button(30, 790, render_button_img, 0.4)
    toolbar_background = Button(30, 30, toolbar_background_img, 0.5)
    borderD = Button(349, 825, borderD_img, 1)
    borderU = Button(349, 15, borderU_img, 1)
    borderL = Button(15, 199, borderL_img, 1)
    borderR = Button(1120, 199, borderR_img, 1)

    stitch_list = pygame.sprite.Group()

    dt = 0
    #starting state - select buttons & different sprites
    state = 'Select Mode'

    #event loop
    run = True
    while run:

        clock.tick(FPS)

        screen.fill("#e0d0bd")

        stitch_list.update()

        stitch_list.draw(screen)
        toolbar_background.draw(screen)
        chain_button.draw(screen)
        singleCR_button.draw(screen)
        doubleCR_button.draw(screen)
        borderD.draw(screen)
        borderU.draw(screen)
        borderL.draw(screen)
        borderR.draw(screen)
        if render_button.draw(screen):
            render_button.render(screen)

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
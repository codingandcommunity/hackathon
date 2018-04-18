import pygame

# dimensions of the screen
screenWidth = 1000
screenHeight = 600
screenBuffer = 60


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):  # position will be declared later when making the player object
        super().__init__()
        # variables to calculate how far the player is moving
        self.changeX = 0
        self.changeY = 0
        self.speed = 9

        # here's where we set the sprite's image
        self.image = pygame.image.load("resources/frogRight.png")
        self.rect = self.image.get_rect()  # player's 'hitbox'

        # setting the position of the player
        self.rect.x = x
        self.rect.y = y
        self.shifted = 0

    def right(self):
        self.image = pygame.image.load("resources/frogRight.png")
        self.changeX = self.speed

    def left(self):
        self.image = pygame.image.load("resources/frogLeft.png")
        self.changeX = -self.speed

    def stop(self):
        self.changeX = 0
        # self.changeY = 0

    def jump(self):
        if self.rect.bottom >= screenHeight:  # check if player is at the bottom of the screen
            self.changeY = -15  # if so, player is able to jump

    def gravity(self):
        self.changeY += 1  # constantly add to player's downward speed

        if self.rect.bottom >= screenHeight and self.changeY >= 0:  # if player is at botto mof screen
            self.changeY = 0  # stop falling
            self.rect.bottom = screenHeight  # set player position to bottom of screen in case it fell too far

    def update(self):
        self.gravity()  # does everything that the gravity function does
        # update the player's position based on the player's speed
        self.rect.x += self.changeX
        self.rect.y += self.changeY


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):  # platform position and dimensions must be declared upon making the object
        super().__init__()
        # setting the appearance of the platform
        self.width = w
        self.height = h
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))  # it will be a generic block unless you change its image and fill
        self.rect = self.image.get_rect()
        # setting the platform's position
        self.rect.x = x
        self.rect.y = y


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file):  # image file name will be declared later when making the object
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0


class Cloud(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y):  # image file name will be declared later when making the object
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.scaleFactor = 1.0/6  # the cloud images were huge, but we can scale them down
        self.image = pygame.transform.scale(self.image, ((int)(self.scaleFactor*self.rect.width), (int)(self.scaleFactor*self.rect.height)))
        # setting the cloud's position
        self.rect.left = x
        self.rect.top = y


def main():
    pygame.init()

    # setting up the window
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Platformer")

    # group of all the static cosmetic aspects such as the background
    artList = pygame.sprite.Group()
    background = Background("resources/sky.png")
    artList.add(background)

    # make a group to hold the clouds
    cloudList = pygame.sprite.Group()
    # make all the clouds
    cloud1 = Cloud("resources/cloud1.png", 145, 200)
    cloud2 = Cloud("resources/cloud2.png", 700, 80)
    cloud3 = Cloud("resources/cloud3.png", 600, 250)
    # add them to the group
    cloudList.add(cloud1)
    cloudList.add(cloud2)
    cloudList.add(cloud3)

    # group that contains the player's sprite
    spriteList = pygame.sprite.Group()
    player = Player(50, 50)
    spriteList.add(player)

    # group of all the platforms
    platformList = pygame.sprite.Group()

    done = False
    while not done:
        # all events such as mouse clicks and key presses
        for event in pygame.event.get():
            # if the player quits out of the screen
            if event.type == pygame.QUIT:
                done = True

            # handles keyboard presses
            if event.type == pygame.KEYDOWN:
                # movement
                if event.key == pygame.K_LEFT:
                    player.left()
                if event.key == pygame.K_RIGHT:
                    player.right()
                if event.key == pygame.K_UP:
                    player.jump()

            # when the player releases a key
            if event.type == pygame.KEYUP:
                # stop moving
                if event.key == pygame.K_LEFT and player.changeX < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.changeX > 0:
                    player.stop()

            # when the player clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())  # prints screen coordinates for easy map building

        # draw all the things
        # (NOTE: Order matters! The last thing drawn will appear in front of all the things before it)
        screen.fill((209, 255, 214))
        artList.draw(screen)
        cloudList.draw(screen)
        spriteList.update()
        spriteList.draw(screen)
        platformList.draw(screen)

        # scrolling effect
        if player.rect.right >= screenWidth-screenBuffer:  # if player reaches right side of screen
            diff = player.rect.right - (screenWidth-screenBuffer)  # calculate how far past screen buffer player has gone
            player.rect.right = (screenWidth-screenBuffer)  # send em back
            for cloud in cloudList:  # for all clouds in the group
                cloud.rect.x -= diff  # shift them left
                if cloud.rect.right < 0:  # if cloud is off screen
                    cloud.rect.left = screenWidth  # put it in a place where it will appear again
        if player.rect.left <= screenBuffer:  # if player reaches left side of screen
            diff = screenBuffer - player.rect.left  # calculate how far past screen buffer player has gone
            player.rect.left = screenBuffer  # send em back
            for cloud in cloudList:  # for all clouds in the group
                cloud.rect.x += diff  # shift them right
                if cloud.rect.left > screenWidth:  # if cloud is off screen
                    cloud.rect.right = 0  # pt it in a place where it will appear again

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()

main()
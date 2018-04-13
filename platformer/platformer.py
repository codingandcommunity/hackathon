import pygame

screenWidth = 1000
screenHeight = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.changeX = 0
        self.changeY = 0
        self.speed = 4
        self.width = 30
        self.height = 50
        self.image = pygame.image.load("resources/frogRight.png")
        # self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.level = None

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
        if self.rect.bottom >= screenHeight:
            self.changeY = -10

    def gravity(self):
        self.changeY += 1

        if self.rect.y >= screenHeight - self.rect.height and self.changeY >= 0:
            self.changeY = 0
            self.rect.y = screenHeight - self.rect.height

    def update(self):
        self.gravity()
        self.rect.x += self.changeX
        self.rect.y += self.changeY


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.width = w
        self.height = h
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Level():
    def __init__(self):
        self.platformList = pygame.sprite.Group()
        self.shifted = 0


def main():
    pygame.init()

    #setting up the window
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Platformer")

    level = 1
    player = Player(50, 50)
    spriteList = pygame.sprite.Group()
    spriteList.add(player)
    platformList = pygame.sprite.Group()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left()
                if event.key == pygame.K_RIGHT:
                    player.right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.changeX < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.changeX > 0:
                    player.stop()
        screen.fill((0,0,0))
        spriteList.update()
        spriteList.draw(screen)
        platformList.draw(screen)

        clock.tick(60)
        pygame.display.flip()


    pygame.quit()


if __name__ == "__main__":
    main()
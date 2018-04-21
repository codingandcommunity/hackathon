import pygame

screenWidth = 1280
screenHeight = 720


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.changeX = 0
        self.changeY = 0
        self.speed = 4
        self.width = 50
        self.height = 50
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.level = None

    #movements
    def right(self):
        self.changeX = self.speed

    def left(self):
        self.changeX = -self.speed

    def up(self):
        self.changeY = -self.speed

    def down(self):
        self.changeY = self.speed

    def stop(self):
        self.changeX = 0
        self.changeY = 0


    def update(self):
        self.rect.x += self.changeX
        self.rect.y += self.changeY


def main():
    pygame.init()

    #setting up the window
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Top-down")

    player = Player(50, 50)
    spriteList = pygame.sprite.Group()
    spriteList.add(player)
    platformList = pygame.sprite.Group()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # movements
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left()
                if event.key == pygame.K_RIGHT:
                    player.right()
                if event.key == pygame.K_UP:
                    player.up()
                if event.key == pygame.K_DOWN:
                    player.down()

            #to prevent infinite sliding
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.changeX < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.changeX > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.changeY < 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.changeY > 0:
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

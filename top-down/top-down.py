import pygame



(width, height) = (500,300)

screen = pygame.display.set_mode((width, height))
pygame.display.flip()


background_color = (255,255,255)
screen.fill(background_color)

pygame.draw.circle(screen, (0,0,255), (150, 50), 15, 1)

pygame.display.set_caption('Top-down game')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

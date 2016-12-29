import datetime
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
rect_x = 0
rect_y = 0
clock = pygame.time.Clock()


while not done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]: rect_y -= 30
    if pressed[pygame.K_DOWN]: rect_y += 30
    if pressed[pygame.K_RIGHT]: rect_x += 30
    if pressed[pygame.K_LEFT]: rect_x -= 30

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(rect_x, rect_y, 30, 30))

    pomagranite = pygame.image.load('botanical-details-pomegranate-2_3.jpg')
    imagerect = pomagranite.get_rect()
    screen.blit(pomagranite, imagerect)

    pygame.display.flip()
    clock.tick(60)

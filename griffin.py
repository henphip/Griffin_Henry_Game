import datetime
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
rect_x = 0
rect_y = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            rect_y += 30

        rect_x += 10
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(rect_x, rect_y, 30, 30))
        pygame.display.flip()

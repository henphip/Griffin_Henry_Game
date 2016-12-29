import datetime
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
rect_x = 30
rect_y = 75

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            rect_y += 50
            rect_x += 0
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(rect_x, rect_y, 20, 30))

        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 0, 30, 30))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(50, 0, 30, 30))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(25, 15, 30, 30))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(25, 45, 30, 30))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(25, 75, 30, 30))


        pygame.display.flip()
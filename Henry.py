import datetime
import pygame

screen_default = raw_input('Would you like to use default screen dimensions? (y or n)')

if screen_default.lower() in ['y', 'yes', 'sure', 'yay']:
    screen_x = 800
    screen_y = 800
else:
    screen_raw = raw_input('What would you like your x and y to be (use raw int seperated by comma. ex: 800,800): ')
    screen_x = int(screen_raw.split(',')[0])
    screen_y = int(screen_raw.split(',')[1])

rect_1_x = 10
rect_1_y = (screen_y-30)/2
rect_2_x = screen_x-(10+30)
rect_2_y = (screen_y-30)/2

pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()

rawp1 = pygame.image.load('apple.png')
player1 = pygame.transform.scale(rawp1, (40, 40))
rawp2 = pygame.image.load('windows.png')
player2 = pygame.transform.scale(rawp2, (40, 40))

done = False
while not done:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_BACKSPACE]:
        done = True

    if pressed[pygame.K_UP] and rect_1_y > 5: rect_1_y -= 30
    if pressed[pygame.K_DOWN] and rect_1_y < screen_y-30: rect_1_y += 30
    if pressed[pygame.K_RIGHT] and rect_1_x < screen_x-30: rect_1_x += 30
    if pressed[pygame.K_LEFT] and rect_1_x > 5: rect_1_x -= 30

    if pressed[pygame.K_w] and rect_2_y > 5: rect_2_y -= 30
    if pressed[pygame.K_s] and rect_2_y < screen_y-30: rect_2_y += 30
    if pressed[pygame.K_d] and rect_2_x < screen_x-30: rect_2_x += 30
    if pressed[pygame.K_a] and rect_2_x > 5: rect_2_x -= 30

    screen.blit(player1, (rect_1_x, rect_1_y))
    screen.blit(player2, (rect_2_x, rect_1_y))

    pygame.display.flip()
    clock.tick(60)




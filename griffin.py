import datetime
import pygame

# TODO:
# 1. Change the xy coordinate variables from 2 to 1 dict

screen_default = raw_input('Would you like to use default screen dimensions? (y or n)')

if screen_default.lower() in ['y', 'yes', 'sure', 'yay']:
    screen_x = 800
    screen_y = 800
else:
    screen_raw = raw_input('What would you like your x and y to be (use raw int seperated by comma. ex: 800,800): ')
    screen_x = int(screen_raw.split(',')[0])
    screen_y = int(screen_raw.split(',')[1])

tagger_size = 60
runner_size = 30
rect1_size = 30
rect2_size = 30

rect_1_x = 10
rect_1_y = (screen_y-30)/2
rect_2_x = screen_x-(10+30)
rect_2_y = (screen_y-30)/2
player1_score = 0
player2_score = 0
tagger = 1

pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 50)
countdown = datetime.datetime.now()
time = 10

def _format_deltatime(td):
    return 10-td.seconds

done = False
while not done:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_BACKSPACE]:
        done = True

    if pressed[pygame.K_UP] and rect_1_y > 5: rect_1_y -= 15
    if pressed[pygame.K_DOWN] and rect_1_y < screen_y-30: rect_1_y += 15
    if pressed[pygame.K_RIGHT] and rect_1_x < screen_x-30: rect_1_x += 15
    if pressed[pygame.K_LEFT] and rect_1_x > 5: rect_1_x -= 15

    if pressed[pygame.K_w] and rect_2_y > 5: rect_2_y -= 15
    if pressed[pygame.K_s] and rect_2_y < screen_y-30: rect_2_y += 15
    if pressed[pygame.K_d] and rect_2_x < screen_x-30: rect_2_x += 15
    if pressed[pygame.K_a] and rect_2_x > 5: rect_2_x -= 15

    if abs(rect_1_y-rect_2_y) < 45 and abs(rect_1_x-rect_2_x) < 45:
        if tagger == 1:
            player2_score += 1
            tagger = 2
            rect1_size = tagger_size
            rect2_size = runner_size
        else:
            player1_score += 1
            tagger = 1
            rect2_size = tagger_size
            rect1_size = runner_size

        rect_1_x = 10
        rect_1_y = (screen_y-30)/2
        rect_2_x = screen_x-(10+30)
        rect_2_y = (screen_y-30)/2
        countdown = datetime.datetime.now()

    if time < 0:
        rect_1_x = 10
        rect_1_y = (screen_y-30)/2
        rect_2_x = screen_x-(10+30)
        rect_2_y = (screen_y-30)/2
        countdown = datetime.datetime.now()


    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(rect_1_x, rect_1_y, rect1_size, rect1_size))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(rect_2_x, rect_2_y, rect2_size, rect2_size))
    label1 = myfont.render(("Player 1 Score: " + str(player1_score) + '      Player 2 Score: ' + str(player2_score)), 1, (0,0,0))
    screen.blit(label1, (50, 10))
    time = _format_deltatime(datetime.datetime.now() - countdown)
    label2 = myfont.render(str(time), 1, (0,0,0))
    screen.blit(label2, (screen_x-50, screen_y-50))

    pygame.display.flip()
    clock.tick(60)

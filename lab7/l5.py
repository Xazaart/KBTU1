import pygame

pygame.init()

BG_COLOR = (255,255,255)
SIZE = (50,50)
BALL_COLOR = (255,0,0)

screen = pygame.display.set_mode((850, 650))
clock = pygame.time.Clock()

x = 100
y = 100

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20

    screen.fill(BG_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (x,y), 25, 25)

    pygame.display.flip()
    clock.tick(60)
        
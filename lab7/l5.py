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

    

    screen.fill(BG_COLOR)
    cir = pygame.draw.circle(screen, BALL_COLOR, (x,y), 25, 25)
    cir

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and cir.y > 0: y -= 20
    if pressed[pygame.K_DOWN] and cir.y < 650-50: y += 20
    if pressed[pygame.K_LEFT] and cir.x > 0: x -= 20
    if pressed[pygame.K_RIGHT] and cir.x < 850-50: x += 20

    pygame.display.flip()
    clock.tick(60)
        
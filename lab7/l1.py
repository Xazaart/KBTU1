import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

done = False
is_blue = True
x = 100
y = 100
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
            is_blue = not is_blue
        
    screen.fill((0,0,0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -=3
    if pressed[pygame.K_DOWN]: y +=3
    if pressed[pygame.K_LEFT]: x -=3
    if pressed[pygame.K_RIGHT]: x +=3

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 30, 30))

    pygame.display.flip()
    clock.tick(60)



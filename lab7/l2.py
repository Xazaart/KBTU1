import pygame
import datetime

pygame.init()
WIDTH, HEIGHT = 850, 650
CENTER = (WIDTH//2, HEIGHT//2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

mickey = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")

mickey_rect = mickey.get_rect(center=CENTER)
min_hand_rect = min_hand.get_rect(center=CENTER)
sec_hand_rect = sec_hand.get_rect(center=CENTER)


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()


    m_angle = -now.minute*6
    s_angle = -now.second*6

    mi = pygame.transform.rotate(min_hand, m_angle)
    se = pygame.transform.rotate(sec_hand, s_angle)
    mi_rotated = mi.get_rect(center = CENTER)
    se_rotated = se.get_rect(center = CENTER)
    
    screen.fill((255,255,255))
    screen.blit(mickey, mickey_rect)
    screen.blit(mi, mi_rotated)
    screen.blit(se, se_rotated)


    pygame.display.flip()
    clock.tick(60)
import pygame, time, os, random
from pygame import mixer, font

# Основные цифры
HEIGTH, WEIGTH = 850, 650
CENTER = (HEIGTH//2,WEIGTH//2)
BG_COLOR = (255,255,255)
TEXT_COLOR = (0,0,0)
font_size = 40

# Иницализация
mixer.init()
pygame.init()
font.init()

# Экран
screen = pygame.display.set_mode((HEIGTH,WEIGTH))
clock = pygame.time.Clock()
pygame.display.set_caption("🎵 MP3 Player 🎵")
font = font.Font(None, font_size)

# Музыка
ind = random.randint(0,4)
music_dir = "music"
playlist = [x for x in os.listdir(music_dir) if x.endswith(".mp3")]
song = os.path.join(music_dir, playlist[ind])
mixer.music.load(song)
mixer.music.play()
playing = True

# Управление музыкой
def prev_song():
    global ind
    ind = (ind-1) % len(playlist)
    song = os.path.join(music_dir, playlist[ind])
    mixer.music.load(song)
    mixer.music.play()

def next_song():
    global ind
    ind = (ind + 1) % len(playlist)
    song = os.path.join(music_dir, playlist[ind])
    mixer.music.load(song)
    mixer.music.play()

def is_playing():
    if playing:
        mixer.music.pause()
        return False
    else:
        mixer.music.unpause()
        return True

# Основной код
running = True
while running:

    screen.fill(BG_COLOR)

    # Надписи
    song_name = playlist[ind].replace(".mp3", "")
    text_surface1 = font.render("Now playing", True, TEXT_COLOR)
    text_surface2 = font.render(f"{song_name}", True, TEXT_COLOR)
    text_rect1 = text_surface1.get_rect(center=(HEIGTH//2,WEIGTH//2-200))
    screen.blit(text_surface1, text_rect1)
    text_rect2 = text_surface2.get_rect(center = (HEIGTH//2,WEIGTH//2-165))
    screen.blit(text_surface2, text_rect2)

    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            playing = is_playing()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()

        elif event.type == pygame.QUIT:
            mixer.music.stop()
            running = False
    
    pygame.display.flip()
    clock.tick(60)
    
    
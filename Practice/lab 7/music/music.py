import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Keyboard Music Player")

songs =['lab 7/music/first.mp3', 'lab 7/music/second.mp3', 'lab 7/music/third.mp3']


current_song_index = 0
pygame.mixer.music.load(songs[current_song_index])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(songs)
                #0+1%3 = 1(play second song)
                #1+1%3 = 2(play third song)
                #2+1%3 = 0(play first song again)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()

pygame.quit()


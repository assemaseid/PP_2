import pygame
import random,time
from pygame import locals

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Surface and background
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((400,600))
backgroung_image = pygame.image.load("lab 8/Racer/AnimatedStreet.png")
backgroung_sound = pygame.mixer.music.load("lab 8/Racer/background.wav")
pygame.mixer.music.play(-1) #play infinetly

#icon
icon = pygame.image.load("lab 8/Racer/Player.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Racer Game")

#Player
player_image = pygame.image.load("lab 8/Racer/Player.png")
player_movement = 5
player_rect = player_image.get_rect()
player_rect.center = (160, 520)

#Enemy
enemy_image = pygame.image.load("lab 8/Racer/Enemy.png")
enemy_movement = 5
enemy_rect = enemy_image.get_rect()
enemy_rect.center = (random.randint(50,350), 5)

#Font and Texts
score_font = pygame.font.SysFont("Verdana", 20)
score = 0
game_over_font = pygame.font.SysFont("Verdana", 60)
game_over_text = game_over_font.render("Game Over",True,(0,0,0))

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(backgroung_image,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == INC_SPEED:
            enemy_movement += 0.5
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        if player_rect.x < 350:
            player_rect.x += player_movement
    elif pressed_keys[pygame.K_LEFT]:
        if player_rect.x > 5:
            player_rect.x -= player_movement

#DRAW IMAGES
    screen.blit(player_image,player_rect)
    screen.blit(enemy_image,enemy_rect)
    pygame.draw.rect(screen, (0,0,0), player_rect, -1)
    pygame.draw.rect(screen, (0,0,0), enemy_rect, -1)

    
    # Enemy Movement
    enemy_rect.y += enemy_movement
    if enemy_rect.y >= 600:
        score += 1
        enemy_rect.y = 5
        enemy_rect.x = random.randint(50, 350)

    score_surface = score_font.render(f"Score: {str(score)}", True, (0, 0, 0))
    screen.blit(score_surface, (5, 5))

#Crash
    if player_rect.colliderect(enemy_rect):
        crash_sound = pygame.mixer.music.load("lab 8/Racer/crash.wav")
        pygame.mixer.music.play()
        time.sleep(1) #wait for playing sound util quiting
        screen.fill((255,0,0))
        screen.blit(game_over_text,(30,250))
        time.sleep(1)   
        pygame.display.update()
        time.sleep(1) 
        pygame.quit()
    

    pygame.display.update()
    FramePerSec.tick(FPS)

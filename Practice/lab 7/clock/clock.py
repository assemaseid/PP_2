
import pygame
import sys
from pygame.locals import *
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 770, 770
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rotating Image')

image = pygame.image.load('lab 7/clock/hand.png')  
image_rect = image.get_rect()
# I did not paste here 'min.png', because due to size of minute hand 
#the allighnment is getting wrong.  It means needed 
#edge is not fixed at the center. 
image_2 = pygame.image.load('lab 7/clock/hand.png')  
image_rect_2 = image_2.get_rect()

fixed_center = (WIDTH // 2, HEIGHT // 2)

clock = pygame.time.Clock()
while True:
    image2 = pygame.image.load('lab 7/clock/clock.png')
    screen.blit(image2, (0,0)) 

    current_time = datetime.now()
    seconds = current_time.second
    minute = current_time.minute

    rotation_angle = seconds * 6  
    rotation_angle_min = (minute + seconds/60) * 6 
    rotated_image = pygame.transform.rotate(image, -rotation_angle)
    rotated_image_min = pygame.transform.rotate(image_2, -rotation_angle_min)

    rotated_image_rect = rotated_image.get_rect()
    rotated_image_rect_min = rotated_image_min.get_rect()

    offset = pygame.math.Vector2(0, -image_rect.height // 2).rotate(rotation_angle)
    offset_min = pygame.math.Vector2(0, -image_rect_2.height // 2).rotate(rotation_angle_min)
    
    rotated_image_rect.center = fixed_center + offset
    rotated_image_rect_min.center = fixed_center + offset_min

    screen.blit(rotated_image, rotated_image_rect)
    screen.blit(rotated_image_min, rotated_image_rect_min)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)  

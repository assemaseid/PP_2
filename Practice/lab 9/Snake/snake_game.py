import pygame
import random
from pygame.math import Vector2

#initialize pygame
pygame.init()

#Screen, background, icon
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")
icon_image = pygame.image.load("Snake/icon.png")
pygame.display.set_icon(icon_image)


#griding the surface
block_size = 20
#Snake
#drawing
def snake_drawing():
    global snake_body
    snake_body = [Vector2(screen_width//2,screen_height//2),Vector2(screen_width//2 - block_size,screen_height//2),Vector2(360,screen_height//2)]
    for block in snake_body:
        pygame.draw.rect(screen, (0,100,0), pygame.Rect(block.x,block.y,block_size,block_size))
#initail direction
    direction = "Right"
    

#Fruit
#preventing overlaping with sneak   
def update_food_pos(snake_body):
    global fruit
    fruit = [random.randint(1,screen_width//block_size - 1)* block_size,random.randint(1,screen_height//block_size - 1)* block_size] 
    # Check if food position overlaps with snake body
    for pos in snake_body:
        if fruit[0] == pos[0] and fruit[1] == pos[1]:
            return update_food_pos(snake_body)

    return fruit

fruit_rect = pygame.Rect(fruit[0], fruit[1], block_size, block_size)


running = True
while running:
    screen.fill((152, 251, 152))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        snake_body[-1].x += block_size
    if keys[pygame.K_LEFT]:
        snake_body[].x += block_size
    if keys[pygame.K_UP]:
        snake_body[-1].x += block_size
    if keys[pygame.K_DOWN]:
        snake_body[-1].x += block_size
    
        



    #Drawing Fruit
    pygame.draw.rect(screen,(255,0,0),fruit_rect)

    #Drawing Snake
    snake_drawing()

    pygame.display.update()


    
    
    
import pygame
import random,time

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("lab 8/Snake/icon.png")
pygame.display.set_icon(icon)

white = (255, 255, 250)
import pygame
import random,time

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("lab 8/Snake/icon.png")
pygame.display.set_icon(icon)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

font_style = pygame.font.SysFont(None, 50)
snake_block_size = 20
snake_speed = 5 
snake_pos = [screen_width / 2, screen_height / 2] #[400,300]
snake_body = [[snake_pos[0], snake_pos[1]],#[400,300]
              [snake_pos[0] - snake_block_size, snake_pos[1]],#[380,300]
              [snake_pos[0] - (2 * snake_block_size), snake_pos[1]]]#[360,300]


last_food_time = pygame.time.get_ticks()

def display_score_level(score, level):
    value = font_style.render("Score: " + str(score) + "  Level: " + str(level), True, black)
    screen.blit(value, [0, 0])

def display_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_block_size, snake_block_size))

def check_food_collision(snake_pos, food_pos):
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    return False

def update_food_pos(snake_body):
    global food_width, last_food_time
    food_size = random.randint(10, 30)
    food_pos = [random.randrange(1, (screen_width // snake_block_size)) * snake_block_size,
                random.randrange(1, (screen_height // snake_block_size)) * snake_block_size]

    for pos in snake_body:
        if food_pos[0] == pos[0] and food_pos[1] == pos[1]:
            return update_food_pos(snake_body)

    food_width = food_size
    last_food_time = pygame.time.get_ticks()
    return food_pos

def check_wall_collision(snake_pos):
    if snake_pos[0] >= screen_width or snake_pos[0] < 0 or snake_pos[1] >= screen_height or snake_pos[1] < 0:
        return True
    return False

def check_self_collision(snake_body):
    head = snake_body[0]
    if head in snake_body[1:]:
        return True
    return False

direction = 'RIGHT'
change_to = direction
food_pos = update_food_pos(snake_body)
score = 0
level = 1

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= snake_block_size
    if direction == 'DOWN':
        snake_pos[1] += snake_block_size
    if direction == 'LEFT':
        snake_pos[0] -= snake_block_size
    if direction == 'RIGHT':
        snake_pos[0] += snake_block_size

    current_time = pygame.time.get_ticks()
    if current_time - last_food_time > 5000:  
        food_pos = update_food_pos(snake_body)

    if check_food_collision(snake_pos, food_pos):
        score += 1
        pygame.mixer.music.load("lab 9/Snake/ding.mp3")
        pygame.mixer.music.play()
        food_pos = update_food_pos(snake_body)
        snake_body.insert(0, list(snake_pos))
        if score % 3 == 0: 
            level += 1
            snake_speed += 2  

    else:
        snake_body.insert(0, list(snake_pos))
        snake_body.pop()

    if check_wall_collision(snake_pos) or check_self_collision(snake_body):
        pygame.mixer.music.load("lab 9/Snake/crash.mp3")
        pygame.mixer.music.play()
        time.sleep(1)
        game_over = True

    screen.fill(white)
    display_snake(snake_body)
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1],food_width,food_width))

    display_score_level(score, level)

    pygame.display.update()

    pygame.time.Clock().tick(snake_speed)

game_over_message = font_style.render("Game Over!", True, black)
screen.blit(game_over_message, [screen_width / 3, screen_height / 3])
pygame.display.update()
pygame.time.delay(2000)

pygame.quit()
quit()
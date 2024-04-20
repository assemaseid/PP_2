import pygame
import random,time

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("lab 8/Snake/icon.png")
pygame.display.set_icon(icon)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

font_style = pygame.font.SysFont(None, 50)
# Snake initial position and size
snake_block_size = 20
snake_speed = 5  # initial speed
snake_pos = [screen_width / 2, screen_height / 2] #[400,300]
snake_body = [[snake_pos[0], snake_pos[1]],#[400,300]
              [snake_pos[0] - snake_block_size, snake_pos[1]],#[380,300]
              [snake_pos[0] - (2 * snake_block_size), snake_pos[1]]]#[360,300]

# Food weights
food_weights = {10: 3, 20: 2, 30: 1}

# Time when food was last generated
last_food_time = pygame.time.get_ticks()

# Function to display score and level
def display_score_level(score, level):
    value = font_style.render("Score: " + str(score) + "  Level: " + str(level), True, black)
    screen.blit(value, [0, 0])

# Function to display snake
def display_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_block_size, snake_block_size))

# Function to check collision with food
def check_food_collision(snake_pos, food_pos):
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    return False

# Function to update food position
def update_food_pos(snake_body):
    global food_width, last_food_time
    food_size = random.choices(list(food_weights.keys()), weights=list(food_weights.values()))[0]
    food_pos = [random.randrange(1, (screen_width // snake_block_size)) * snake_block_size,
                random.randrange(1, (screen_height // snake_block_size)) * snake_block_size]

    # Check if food position overlaps with snake body
    for pos in snake_body:
        if food_pos[0] == pos[0] and food_pos[1] == pos[1]:
            return update_food_pos(snake_body)

    food_width = food_size
    last_food_time = pygame.time.get_ticks()
    return food_pos

# Function to check collision with walls
def check_wall_collision(snake_pos):
    if snake_pos[0] >= screen_width or snake_pos[0] < 0 or snake_pos[1] >= screen_height or snake_pos[1] < 0:
        return True
    return False

# Function to check collision with itself
def check_self_collision(snake_body):
    head = snake_body[0]
    if head in snake_body[1:]:
        return True
    return False

# Main function
def game():
    global direction, change_to, snake_pos, food_pos, snake_body, score, level, snake_speed, last_food_time
    direction = 'RIGHT'
    change_to = direction
    food_pos = update_food_pos(snake_body)
    score = 0
    level = 1
   
    
    # Game loop
    game_over = False
    while not game_over:
        # Event handling
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

        # Change direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Move snake
        if direction == 'UP':
            snake_pos[1] -= snake_block_size
        if direction == 'DOWN':
            snake_pos[1] += snake_block_size
        if direction == 'LEFT':
            snake_pos[0] -= snake_block_size
        if direction == 'RIGHT':
            snake_pos[0] += snake_block_size

        # Check if food should be regenerated
        current_time = pygame.time.get_ticks()
        if current_time - last_food_time > 7000:  # Regenerate food every 5 seconds
            food_pos = update_food_pos(snake_body)

        # Check if food is eaten
        if check_food_collision(snake_pos, food_pos):
            score += 1
            pygame.mixer.music.load("lab 8/Snake/ding.mp3")
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
            pygame.mixer.music.load("lab 8/Snake/crash.mp3")
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

game()
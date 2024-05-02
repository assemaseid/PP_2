import pygame
import random
import time
import psycopg2

pygame.init()

conn = psycopg2.connect(
    database="snakeuser",
    user="postgres",
    password="72zv5u3xp"
)
cur = conn.cursor()


cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username Text
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        score_id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(user_id),
        score INTEGER,
        level INTEGER
    )
''')

username = input("Enter Username: ")

def insert_users_data(username):
    cur.execute("select * from users where username = (%s)", (username,))
    user = cur.fetchone()
    if user is None:
        cur.execute("INSERT INTO users(username) values(%s)", (username,))
        conn.commit()

insert_users_data(username)

def insert_scores_data(username, score, level):
    cur.execute("select user_id from users where username = (%s)", (username,))
    user_id = cur.fetchone()
    cur.execute("INSERT INTO scores(user_id,score,level) VALUES (%s,%s,%s)",(user_id,score,level))
    conn.commit()

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
snake_pos = [screen_width / 2, screen_height / 2]  # [400,300]
snake_body = [[snake_pos[0], snake_pos[1]],  # [400,300]
              [snake_pos[0] - snake_block_size, snake_pos[1]],  # [380,300]
              [snake_pos[0] - (2 * snake_block_size), snake_pos[1]]]  # [360,300]

last_food_time = pygame.time.get_ticks()

def pause_game():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press space to resume
                    paused = False
                elif event.key == pygame.K_ESCAPE:  # Press escape to quit
                    pygame.quit()
                    quit()
        # Display "Paused" message
        paused_message = font_style.render("Paused", True, black)
        screen.blit(paused_message, [screen_width / 3, screen_height / 3])
        pygame.display.update()
        pygame.time.Clock().tick(5)  # Adjust tick rate to reduce CPU usage
    


def level_1_walls():
    wall_x = 0
    wall_y = 25
    walls = pygame.image.load("/Users/assemseidkarim/Desktop/PP_2/Practice/lab 10/fense.png")
    while wall_x < screen_width:
        screen.blit(walls,(wall_x,wall_y))
        wall_x += 64

    wall_x = -4
    wall_y = 74
    walls_2 = pygame.image.load("/Users/assemseidkarim/Desktop/PP_2/Practice/lab 10/fense2.png")
    while wall_y < screen_height:
        screen.blit(walls_2,(wall_x,wall_y))
        wall_y += 64

    wall_x = 50
    wall_y = abs(60 - screen_height)
    walls_2 = pygame.image.load("/Users/assemseidkarim/Desktop/PP_2/Practice/lab 10/fense.png")
    while wall_x < screen_width - 64:
        screen.blit(walls,(wall_x,wall_y))
        wall_x += 64

    wall_x = abs(68 - screen_width)
    wall_y = 74
    walls_3 = pygame.image.load("/Users/assemseidkarim/Desktop/PP_2/Practice/lab 10/fense1.png")
    while wall_y < screen_height:
        screen.blit(walls_3,(wall_x,wall_y))
        wall_y += 64

def level_2_walls(screen):
    global rock_walls
    rock_walls = pygame.image.load("/Users/assemseidkarim/Desktop/PP_2/Practice/lab 10/rock.png")
    rock_walls_x = 60
    rock_walls_y = screen_height // 2
    while rock_walls_x < screen_width // 3:
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_x += 32

    rock_walls_x = screen_width // 2
    rock_walls_y = 89
    while rock_walls_y < screen_height // 3:
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_y += 32

    rock_walls_x = screen_width // 2
    rock_walls_y = screen_height - screen_height // 3
    while rock_walls_y < screen_height - 64:
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_y += 32
    
    rock_walls_x = screen_width - screen_width // 3
    rock_walls_y = screen_height // 2
    while rock_walls_x < screen_width - 50:
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_x += 32

def level_3_walls(screen):
    rock_walls = pygame.image.load("/Users/assemseidkarim/Desktop/PP_2/Practice/lab 10/rock.png")
# vertical walls
    rock_walls_x = screen_width // 5
    rock_walls_y = screen_height // 3
    while rock_walls_y < screen_width - (screen_width // 2):
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_y += 32

    rock_walls_x = (screen_width // 5) * 2
    rock_walls_y = screen_height // 3
    while rock_walls_y < screen_width - (screen_width // 2):
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_y += 32

    rock_walls_x = (screen_width // 5) * 3
    rock_walls_y = screen_height // 3
    while rock_walls_y < screen_width - (screen_width // 2):
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_y += 32
    
    rock_walls_x = (screen_width // 5) * 4
    rock_walls_y = screen_height // 3
    while rock_walls_y < screen_width - (screen_width // 2):
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_y += 32
# horizomntal
    rock_walls_x = screen_width // 5 + 32
    rock_walls_y = screen_height // 3 - 60
    while rock_walls_x < (screen_width // 5) * 2 - 20:
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_x += 32

    rock_walls_x = screen_width // 5 + 32
    rock_walls_y = screen_width - (screen_width // 2) + 60
    while rock_walls_x < (screen_width // 5) * 2 - 20:
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_x += 32

    rock_walls_x = (screen_width // 5) * 3 + 32
    rock_walls_y = screen_width - (screen_width // 2) + 60
    while rock_walls_x < (screen_width // 5) * 4 - 20:
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_x += 32

    rock_walls_x = (screen_width // 5) * 3 + 32
    rock_walls_y = screen_height // 3 - 60
    while rock_walls_x < (screen_width // 5) * 4 - 20:
        screen.blit(rock_walls,(rock_walls_x,rock_walls_y))
        rock_walls_x += 32

def display_score_level(score, level):
    value = font_style.render("Score: " + str(score) + "  Level: " + str(level), True, black)
    screen.blit(value, [0, 0])


def display_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_block_size, snake_block_size))


def check_food_collision(snake_pos, food_pos, food_pos_2):
    return snake_pos in [food_pos, food_pos_2]


def update_food_pos(snake_body):
    global last_food_time, food_width
    food_size = random.randint(10, 30)
    food_width = food_size
    food_pos = [
        random.randrange(3, (screen_width // snake_block_size)-3) * snake_block_size,
        random.randrange(4, (screen_height // snake_block_size)-4) * snake_block_size
    ]
    food_pos_2 = [
        random.randrange(3, (screen_width // snake_block_size)-3) * snake_block_size,
        random.randrange(4, (screen_height // snake_block_size)-4) * snake_block_size
    ]
    for pos in snake_body:
        if [food_pos, food_pos_2] == pos:
            return update_food_pos(snake_body)
        
    rock_wall_positions = [
            (range(60, screen_width // 3), range(screen_height // 2 - 32, screen_height // 2 + 32)),  # Top-left rock wall
            (range(screen_width // 2 - 32, screen_width // 2 + 32), range(89, screen_height // 3)),   # Top-right rock wall
            (range(screen_width // 2 - 32, screen_width // 2 + 32), range(screen_height - screen_height // 3, screen_height - 64)),  # Bottom-right rock wall
            (range(screen_width - screen_width // 3 - 32, screen_width - 50), range(screen_height // 2 - 32, screen_height // 2 + 32))    # Bottom-left rock wall
            ]
    
    for wall_pos in rock_wall_positions:
        if  food_pos == wall_pos or food_pos_2 == wall_pos:
            return update_food_pos(snake_body)
    

    last_food_time = pygame.time.get_ticks()
    return food_pos, food_pos_2, food_size

def check_wall_collision(snake_pos, level):
    # Check for collision with the boundaries of the screen
    global rock_wall_positions
    if level == 1:
        if snake_pos[0] >= screen_width - 64 or snake_pos[0] < 50 or snake_pos[1] >= screen_height - 64 or snake_pos[1] < 64:
            return True
    if level == 2:
        if snake_pos[0] >= screen_width - 64 or snake_pos[0] < 50 or snake_pos[1] >= screen_height - 64 or snake_pos[1] < 64:
            return True
        
        rock_wall_positions = [
            (range(60, screen_width // 3), range(screen_height // 2 - 16, screen_height // 2 + 16)), 
            (range(screen_width // 2 - 16, screen_width // 2 + 16), range(89, screen_height // 3)),  
            (range(screen_width // 2 - 16, screen_width // 2 + 16), range(screen_height - screen_height // 3, screen_height - 64)),  
            (range(screen_width - screen_width // 3 - 32, screen_width - 50), range(screen_height // 2 - 16, screen_height // 2 + 16))    
            ]
        for wall_x_range, wall_y_range in rock_wall_positions:
            if snake_pos[0] in wall_x_range and snake_pos[1] in wall_y_range:
                return True
    if level >= 3:
        if snake_pos[0] >= screen_width - 64 or snake_pos[0] < 50 or snake_pos[1] >= screen_height - 64 or snake_pos[1] < 64:
            return True
        
        rock_wall_positions = [
            (range(screen_width // 5 - 16, screen_width // 5 + 16), range(screen_height // 3,screen_width - (screen_width // 2))),  
            (range((screen_width // 5) * 2 - 16, (screen_width // 5) * 2 + 16), range(screen_height // 3, screen_width - (screen_width // 2))),
            (range((screen_width // 5) * 3 - 16, (screen_width // 5) * 3 + 16), range(screen_height // 3, screen_width - (screen_width // 2))),  
            (range((screen_width // 5) * 4 - 16, (screen_width // 5) * 4 + 16), range(screen_height // 3, screen_width - (screen_width // 2))),  

            (range(screen_width // 5 + 32, (screen_width // 5) * 2 - 20), range(screen_height // 3 - 60 - 16, screen_height // 3 - 60 + 16)),
            (range(screen_width // 5 + 32, (screen_width // 5) * 2 - 20), range(screen_width - (screen_width // 2) + 60 - 16, screen_width - (screen_width // 2) + 60 + 16)),
            (range((screen_width // 5) * 3 + 32, (screen_width // 5) * 4 - 20), range(screen_width - (screen_width // 2) + 60 - 16, screen_width - (screen_width // 2) + 60 + 16)),    
            (range((screen_width // 5) * 3 + 32, (screen_width // 5) * 4 - 20), range(screen_height // 3 - 60 - 16, screen_height // 3 - 60 + 16))    
            ]
        
        for wall_x_range, wall_y_range in rock_wall_positions:
            if snake_pos[0] in wall_x_range and snake_pos[1] in wall_y_range:
                return True

    
  

            
def check_self_collision(snake_body):
    head = snake_body[0]
    return head in snake_body[1:]


direction = 'RIGHT'
change_to = direction
food_pos, food_pos_2, food_width = update_food_pos(snake_body)
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
            if event.key == pygame.K_p:  # Press 'P' to pause
                pause_game()

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
        food_pos, food_pos_2, food_width = update_food_pos(snake_body)

    if check_food_collision(snake_pos, food_pos, food_pos_2):
        score += 1
        pygame.mixer.music.load("lab 8/Snake/ding.mp3")
        pygame.mixer.music.play()
        food_pos, food_pos_2, food_width = update_food_pos(snake_body)
        snake_body.insert(0, list(snake_pos))
        if score % 3 == 0:
            level += 1
            snake_speed += 2
                
    else:
        snake_body.insert(0, list(snake_pos))
        snake_body.pop()

    if check_wall_collision(snake_pos,level) or check_self_collision(snake_body):
        pygame.mixer.music.load("lab 8/Snake/crash.mp3")
        pygame.mixer.music.play()
        time.sleep(1)
        game_over = True
        insert_scores_data(username, score, level)        

    screen.fill((0,100,0))
    display_snake(snake_body)
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], food_width, food_width))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos_2[0], food_pos_2[1], food_width, food_width))

    display_score_level(score, level)

    if level == 1:
        level_1_walls()
    elif level == 2 :
        level_1_walls()
        level_2_walls(screen)
    elif level >= 3:
        level_1_walls()
        level_3_walls(screen)
    

    pygame.display.update()

    pygame.time.Clock().tick(snake_speed)

game_over_message = font_style.render("Game Over!", True, black)
screen.blit(game_over_message, [screen_width / 3, screen_height / 3])
pygame.display.update()
pygame.time.delay(2000)

cur.close()
conn.close()
pygame.quit()
quit()

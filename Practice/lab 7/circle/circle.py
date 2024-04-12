import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
ball_size = 50
ball_x = 400
ball_y = 300
move_speed= 20


running= True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_x -= move_speed
                if ball_x < 25:
                    ball_x = 25
            elif event.key ==  pygame.K_RIGHT:
                ball_x += move_speed
                if ball_x >= 775:
                    ball_x = 775
            elif event.key == pygame.K_DOWN:
                ball_y += move_speed
                if ball_y >= 575:
                    ball_y = 575
            elif event.key == pygame.K_UP:
                ball_y -= move_speed
                if ball_y <= 25:
                    ball_y = 25
       

    pygame.draw.circle(screen, (255, 0 ,0), (ball_x, ball_y), ball_size//2)
    pygame.display.flip()
pygame.quit()
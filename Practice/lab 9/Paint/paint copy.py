import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")

fps = 180
timer = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (220, 220, 220)
YELLOW = (255,255,0)

erase = pygame.image.load("lab 9/Paint/eraser.png")
erase_x = 200
erase_y = 25
erase_rect = erase.get_rect()
erase_rect.center = (erase_x, erase_y)

def draw_menu():
    pygame.draw.rect(screen, GRAY, (0, 0, 800, 60))
    pygame.draw.line(screen, BLACK, (0,60),(800,60))
    screen.blit(erase, erase_rect)
    
    blue = pygame.draw.rect(screen, BLUE, (10, 10, 30, 30))
    red = pygame.draw.rect(screen, RED, (45, 10, 30, 30))
    green = pygame.draw.rect(screen, GREEN, (80, 10, 30, 30))
    black = pygame.draw.rect(screen, BLACK, (115, 10, 30, 30))
    yellow = pygame.draw.rect(screen, YELLOW, (150, 10, 30, 30))
    eraser = pygame.draw.rect(screen, BLACK, erase_rect, -1)
    rgbs = [BLUE,RED,GREEN,BLACK,YELLOW]
    color_rect = [blue, red, green, black, yellow]

    square = pygame.draw.rect(screen,BLACK, (760, 10, 30, 30),1)
    cicle = pygame.draw.circle(screen,BLACK,(735,25),16,1)
    right_triangle = pygame.draw.polygon(screen, BLACK,[(710,40),(680,40),(695,10)],1)
    equilateral_triangle = pygame.draw.polygon(screen, BLACK, [(675, 40), (635, 40), (655, 10)], 1)
    rhombus = pygame.draw.polygon(screen, BLACK, [(630, 25), (610, 10), (590, 25), (610, 40)], 1)
    rectangle = pygame.draw.rect(screen,BLACK, (540, 10, 40, 30),1)
    figures = [square,cicle,right_triangle,equilateral_triangle,rhombus,rectangle]
    

    return color_rect,rgbs,eraser,figures

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen,paints[i][0],paints[i][1],paints[i][2])

def draw_selected_figure(mouse_pos):
    if selected_figure is not None:
        if selected_figure == 0:  # square
            width = mouse_pos[0] - start_pos[0]
            height = mouse_pos[1] - start_pos[1]
            pygame.draw.rect(screen, active_color, (start_pos[0], start_pos[1], width, height),1)
        elif selected_figure == 1:  # Circle
            radius = max(abs(mouse_pos[0] - start_pos[0]), abs(mouse_pos[1] - start_pos[1]),1)
            pygame.draw.circle(screen, active_color, start_pos, radius)
        # Add other shapes as needed

active_color = WHITE
active_size = 10
painting = []

selected_figure = None
running = True
while running:
    screen.fill(WHITE)

    colors, rgb_colors, eraserr,figure = draw_menu()
    mouse = pygame.mouse.get_pos()
    start_pos = mouse
    
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and mouse[1] > 70:
        painting.append((active_color,mouse,active_size))

    draw_painting(painting)

   

    if mouse[1] > 70:
        pygame.draw.circle(screen,active_color,mouse,active_size)
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            alt_held = keys[pygame.K_LALT] or keys[pygame.K_RALT]
            ctrl_held = keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]
            if event.key == pygame.K_w and ctrl_held:
                running = False
            elif event.key == pygame.K_F4 and alt_held:
                running = False
            elif event.key == pygame.K_r:
                active_color = RED
            elif event.key == pygame.K_g:
                active_color = GREEN
            elif event.key == pygame.K_b:
                active_color = BLUE
            elif event.key == pygame.K_y:
                active_color = YELLOW
            elif event.key == pygame.K_b and pygame.K_l:
                active_color = BLACK

       
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                if erase_rect.collidepoint(mouse):
                    active_color = WHITE
                else:
                    for i in range(len(colors)):
                        if colors[i].collidepoint(mouse):
                            active_color = rgb_colors[i]
            elif event.button == 3:  
                active_size = min(20, active_size + 1) 
            elif event.button == 4: 
                active_size = max(1, active_size - 1)  

            for i in range(len(figure)):
                if figure[i].collidepoint(mouse):
                    selected_figure = i
                    

    draw_selected_figure(mouse)
    
    timer.tick(fps)
    pygame.display.update()

pygame.quit()

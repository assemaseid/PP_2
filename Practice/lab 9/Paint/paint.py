import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

mode = "blue"
radius = 10
# It will be a list of coordinates those are drawn on the surface
drawing = False

points = []

erase = pygame.image.load("Paint/eraser.png")
erase_x = 130
erase_y = 25
erase_rect = erase.get_rect()
erase_rect.center = (erase_x, erase_y)

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            alt_held = keys[pygame.K_LALT] or keys[pygame.K_RALT]
            ctrl_held = keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]
            if event.key == pygame.K_w and ctrl_held:
                running = False
            if event.key == pygame.K_F4 and alt_held:
                running = False
            if event.key == pygame.K_r:
                mode = "red"
            if event.key == pygame.K_g:
                mode = "green"
            if event.key == pygame.K_b:
                mode = "blue"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                radius = min(200, radius + 1)
            if event.button == 3:
                radius = max(1, radius - 1)
            for i in range(len(color_rects)):
                if color_rects[i].collidepoint(event.pos):
                    if i == 0:
                        mode = "blue"
                    elif i == 1:
                        mode = "red"
                    elif i == 2:
                        mode = "green"
        elif event.type == pygame.MOUSEBUTTONUP:
            if erase_rect.collidepoint(event.pos):
                for i in range(len(points) - 1):
                    pygame.draw.line(screen, WHITE, points[i], points[i + 1], 20)
                points = []  # Clear points after erasing

        if event.type == pygame.MOUSEMOTION:
            position = pygame.mouse.get_pos()
            if drawing:
                points.append(position)  # Append the position directly
                points = points[-400:]  # to retain only the most recent 400 points

    if mode == "blue":
        color = BLUE
    elif mode == "red":
        color = RED
    elif mode == "green":
        color = GREEN
    elif mode == "white":
        color = WHITE

    for i in range(len(points) - 1):
        pygame.draw.line(screen, color, points[i], points[i + 1], radius)

    # Draw color selection
    menu = pygame.draw.rect(screen, (220, 220, 220), (0, 0, 800, 60))
    blue = pygame.draw.rect(screen, BLUE, (10, 10, 30, 30))
    red = pygame.draw.rect(screen, RED, (45, 10, 30, 30))
    green = pygame.draw.rect(screen, GREEN, (80, 10, 30, 30))
    color_rects = [blue, red, green]

    # Erase button
    screen.blit(erase, erase_rect)
    pygame.draw.rect(screen, BLACK, erase_rect, -1)

    pygame.display.update()

pygame.quit()

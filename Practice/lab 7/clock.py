import pygame
import os

# Dictionary to cache loaded images
_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert_alpha()
        _image_library[path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

done = False
is_blue = True
x = 30
y = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        y -= 3
    if pressed[pygame.K_DOWN]: 
        y += 3
    if pressed[pygame.K_LEFT]: 
        x -= 3
    if pressed[pygame.K_RIGHT]: 
        x += 3

    screen.fill((255, 255, 255))
    
    # Set color based on is_blue flag
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
        
    # Draw rectangle
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 30, 30))
    
    # Load and blit image
    screen.blit(get_image('mickeyclock.png'))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

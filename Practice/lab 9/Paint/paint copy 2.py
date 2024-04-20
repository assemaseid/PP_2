import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define figures
FIGURES = ["Line", "Rectangle", "Circle"]

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

# Function to draw a figure
def draw_figure(figure_type, start_pos, end_pos, color):
    if figure_type == "Line":
        pygame.draw.line(screen, color, start_pos, end_pos, 5)
    elif figure_type == "Rectangle":
        pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 0)
    elif figure_type == "Circle":
        radius = ((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5
        pygame.draw.circle(screen, color, start_pos, int(radius), 0)

# Main function
def main():
    running = True
    current_figure = None
    start_pos = None
    end_pos = None
    current_color = BLACK

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_l:
                    current_figure = "Line"
                elif event.key == pygame.K_r:
                    current_figure = "Rectangle"
                elif event.key == pygame.K_c:
                    current_figure = "Circle"
                elif event.key == pygame.K_1:
                    current_color = BLACK
                elif event.key == pygame.K_2:
                    current_color = RED
                elif event.key == pygame.K_3:
                    current_color = GREEN
                elif event.key == pygame.K_4:
                    current_color = BLUE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    start_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    end_pos = pygame.mouse.get_pos()
                    if current_figure:
                        draw_figure(current_figure, start_pos, end_pos, current_color)

        screen.fill(WHITE)

        # Draw menu bar
        for i, figure in enumerate(FIGURES):
            pygame.draw.rect(screen, BLACK, (i * 100, 0, 100, 30), 2)
            font = pygame.font.Font(None, 24)
            text = font.render(figure, True, BLACK)
            screen.blit(text, (i * 100 + 10, 5))

        # Draw selected figure
        if current_figure:
            pygame.draw.rect(screen, BLACK, (0, HEIGHT - 30, WIDTH, 30), 2)
            font = pygame.font.Font(None, 24)
            text = font.render(f"Selected: {current_figure}", True, BLACK)
            screen.blit(text, (10, HEIGHT - 25))

        pygame.display.update()

if __name__ == "__main__":
    main()

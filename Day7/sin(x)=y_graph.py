import pygame
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.info("Program started")

# Initialize pygame
pygame.init()

# Set screen dimensions
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

# Function to transform mathematical coordinates to screen coordinates
def transform(x, y):
    screen_x = int((x + 6) * (w // 12))  # Scale and shift x to screen space for [-6, 6]
    screen_y = int((1 - y) * (h // 2))  # Scale and shift y to screen space for [-1, 1]
    return screen_x, screen_y

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))  # Clear the screen with black

    # Plot y = sin(x) on interval [-6, 6]
    for i in range(w):
        x = (i - w // 2) / (w // 12) - 6  # Scale screen x to interval [-6, 6]
        y = math.sin(x)  # y = sin(x) function
        if -1 <= y <= 1:  # Check if y is within the visible range
            screen_x, screen_y = transform(x, y)
            screen.set_at((screen_x, screen_y), (255, 255, 255))

    pygame.display.flip()  # Update the display

pygame.quit()

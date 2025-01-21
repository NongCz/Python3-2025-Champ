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
    screen_x = int((x + 2) * (w // 4))  # Scale and shift x to screen space for [-2, 2]
    screen_y = int((2 - y) * (h // 4))  # Scale and shift y to screen space for [0, 4]
    return screen_x, screen_y

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))  # Clear the screen with black

    # Plot y = x^2 on interval [-2, 2]
    for i in range(w):
        x = (i - w // 2) / (w // 200) - 2  # Scale screen x to interval [-2, 2]
        y = x ** 2  # y = x^2 function
        if 0 <= y <= 4:  # Check if y is within the visible range
            screen_x, screen_y = transform(x, y)
            screen.set_at((screen_x, screen_y), (255, 255, 255))

    pygame.display.flip()  # Update the display

pygame.quit()

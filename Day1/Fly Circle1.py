import pygame
import sys

class Circle:
    def __init__(self, radius, x, y, x_velocity, y_velocity, screen_width, screen_height):
        self.radius = radius
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.x - self.radius <= 0 or self.x + self.radius >= self.screen_width:
            self.x_velocity *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen_height:
            self.y_velocity *= -1

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Circle")
clock = pygame.time.Clock()

circle1 = Circle(radius=30, x=200, y=300, x_velocity=4, y_velocity=3, screen_width=screen_width, screen_height=screen_height)
circle2 = Circle(radius=40, x=500, y=400, x_velocity=-3, y_velocity=5, screen_width=screen_width, screen_height=screen_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    circle1.move()
    circle1.draw(screen)
    circle2.move()
    circle2.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()

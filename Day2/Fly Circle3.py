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

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.x - self.radius <= 0 or self.x + self.radius >= self.screen_width:
            self.x_velocity *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen_height:
            self.y_velocity *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), self.radius)

    def check_collision(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance_squared = dx * dx + dy * dy
        radius_sum = self.radius + other.radius
        if distance_squared <= radius_sum * radius_sum:
            self.x_velocity, other.x_velocity = other.x_velocity, self.x_velocity
            self.y_velocity, other.y_velocity = other.y_velocity, self.y_velocity


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

circles = [
    Circle(30, 200, 300, 4, 3, 800, 600),
    Circle(40, 500, 400, -3, 5, 800, 600)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    for circle in circles:
        circle.move()
        circle.draw(screen)

    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            circles[i].check_collision(circles[j])

    pygame.display.flip()
    clock.tick(60)
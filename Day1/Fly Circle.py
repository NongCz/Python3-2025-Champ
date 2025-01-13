class Circle:
    def __init__(self, radius, x, y, direction):
        self.radius = radius
        self.x = x
        self.y = y
        self.direction = direction
    
    def draw(self):
        print(f"Circle at ({self.x}, {self.y}) with radius {self.radius}")
    
    def move(self, step=1):
        if self.direction == "up":
            self.y += step
        elif self.direction == "down":
            self.y -= step
        elif self.direction == "left":
            self.x -= step
        elif self.direction == "right":
            self.x += step
        else:
            print("Invalid direction. Use 'up', 'down', 'left', or 'right'.")
        
        print(f"Moved to ({self.x}, {self.y})")

circle = Circle(radius=5, x=0, y=0, direction="up")

while True:
    circle.draw()  
    action = input("Enter 'move' to move, 'change' to change direction, or 'exit' to quit: ").strip().lower()
    
    if action == "move":
        step = input("Enter step size (default is 1): ").strip()
        step = int(step) if step.isdigit() else 1
        circle.move(step)
    elif action == "change":
        new_direction = input("Enter new direction (up, down, left, right): ").strip().lower()
        if new_direction in ["up", "down", "left", "right"]:
            circle.direction = new_direction
            print(f"Direction changed to {circle.direction}")
        else:
            print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")
    elif action == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please try again.")


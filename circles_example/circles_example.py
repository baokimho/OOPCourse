import tkinter as tk
import random


class Circle:
    def __init__(self, root, canvas, x, y, initial_radius, color):
        self.root = root
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = initial_radius
        self.color = color

    def update_drawing(self, growth_step, delay, max_radius):
        while self.radius < max_radius:
            self.canvas.delete("all")
            self.canvas.create_oval(self.x - self.radius, self.y - self.radius, 
                                    self.x + self.radius, self.y + self.radius, 
                                    outline="black", fill=self.color)
            self.radius += growth_step
            self.root.update()
            self.root.after(delay)


class VariableColorCircle(Circle):
    def __init__(self, root, canvas, x, y, initial_radius, color):
        super().__init__(root, canvas, x, y, initial_radius, color)

    def update_drawing(self, growth_step, delay, max_radius):
        color_change_counter = 0
        while self.radius < max_radius:
            self.canvas.delete("all")
            if color_change_counter % (500 // delay) == 0:  # Change color every half second
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                self.color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_oval(self.x - self.radius, self.y - self.radius, 
                                    self.x + self.radius, self.y + self.radius, 
                                    outline="black", fill=self.color)
            self.radius += growth_step
            self.root.update()
            self.root.after(delay)
            color_change_counter += 1


class AllCircles:
    def __init__(self):
        self.circles = []

    def add_circle(self, circle):
        self.circles.append(circle)

    def shuffle(self):
        random.shuffle(self.circles)

    def update_draw(self, growth_step, delay, max_radius):
        for circle in self.circles:
            circle.update_drawing(growth_step, delay, max_radius)


def animate():
    root = tk.Tk()
    root.title("Growing Circles")

    canvas = tk.Canvas(root, width=800, height=400)
    canvas.pack()

    all_circles = AllCircles()


    for _ in range(5):  # Create 5 Circles with random positions and colors
        initial_radius = 1
        max_radius = 100
        growth_step = 1
        delay = 40
        x_pos = random.randint(0, 400)
        y_pos = random.randint(0, 400)
        color = random.choice(["red", "green", "blue", "yellow", "purple"])
        circle = Circle(root, canvas, x_pos, y_pos, initial_radius, color)
        all_circles.add_circle(circle)

        
    for _ in range(5):  # Create 5 circles with random positions and colors
        initial_radius = 1
        max_radius = 100
        growth_step = 1
        delay = 40
        x_pos = random.randint(0, 400)
        y_pos = random.randint(0, 400)
        color = random.choice(["red", "green", "blue", "yellow", "purple"])
        circle = VariableColorCircle(root, canvas, x_pos, y_pos, initial_radius, color)
        all_circles.add_circle(circle)



  
    all_circles.shuffle()
    all_circles.update_draw(growth_step, delay, max_radius)

    root.mainloop()


animate()



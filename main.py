import turtle as trtl

class TurtleDrawing:
    def __init__(self, shapes, colors):

        if len(shapes) != len(colors):
            raise ValueError("Shapes and colors lists must be of the same length.")

        self.turtles = []
        self.shapes = shapes
        self.colors = colors
        self.create_turtles()

    def create_turtles(self):
        #creates turtles
        for shape, color in zip(self.shapes, self.colors):
            t = trtl.Turtle(shape=shape)
            t.penup()
            t.color(color)
            self.turtles.append(t)

    def draw_turtles(self):
        #creates hexagon pattern
        startx = 0
        starty = 0
        direction = 90
        step_size = 10

        for t in self.turtles:
            t.setheading(direction)
            t.goto(startx, starty)
            t.pendown()
            t.forward(step_size)
            direction += 60
            startx = t.xcor()
            starty = t.ycor()
            step_size += 5

    def __str__(self):
        #returns a string of the turtle's shapes and colors
        return "\n".join(f"Turtle Shape: {shape}, Color: {color}" for shape, color in zip(self.shapes, self.colors))


if __name__ == "__main__":
    #defines shapes and colors
    turtle_shapes = [
        "arrow", "turtle", "circle", "square", "triangle", "classic",
        "arrow", "turtle", "circle", "square", "triangle", "classic"
    ]
    turtle_colors = [
        "red", "blue", "green", "orange", "purple", "gold",
        "red", "blue", "green", "orange", "purple", "gold"
    ]

    #instance of TurtleDrawing
    drawing = TurtleDrawing(turtle_shapes, turtle_colors)
    
    print(drawing)

    drawing.draw_turtles()

    wn = trtl.Screen()
    wn.mainloop()

import turtle as trtl

my_turtles = []

turtle_shapes = [
    "arrow", "turtle", "circle", "square", "triangle", "classic",
    "arrow", "turtle", "circle", "square", "triangle", "classic"
]
turtle_colors = [
    "red", "blue", "green", "orange", "purple", "gold",
    "red", "blue", "green", "orange", "purple", "gold"
]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    t.penup()
    color = turtle_colors.pop(0)
    t.color(color)
    my_turtles.append(t)

startx = 0
starty = 0
direction = 90
step_size = 10

for t in my_turtles:
    t.setheading(direction)
    t.goto(startx, starty)
    t.pendown()
    t.forward(step_size)
    direction += 60
    startx = t.xcor()
    starty = t.ycor()
    step_size += 5

wn = trtl.Screen()
wn.mainloop()

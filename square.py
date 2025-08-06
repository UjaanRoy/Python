import turtle
turtle.Screen().bgcolor("red3")
turtle.Screen().setup (500,500)
variable=turtle.Turtle()
sides=4
side_length=80
angle=360/sides
for i in range (sides):
    variable.forward(side_length)
    variable.right(angle)
turtle.done()
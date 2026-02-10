import turtle

turtle.setup(600, 400)
turtle.shape("turtle")
turtle.shapesize(2)
turtle.color("orange")
turtle.pensize(3)
turtle.begin_fill()
n_sides = int(turtle.textinput("sides", "how many sides?"))
for i in range(n_sides):
    turtle.fd(80)
    turtle.left(360 / n_sides)
turtle.end_fill()
turtle.penup()
turtle.goto(-200, 100)
turtle.write("hello every body", font=("arial", 22))
turtle.ht()
turtle.done()

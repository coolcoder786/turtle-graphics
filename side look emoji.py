import turtle
my_pen = turtle.Turtle()

my_pen.color("#ffdd00")
my_pen.begin_fill()
my_pen.circle(100)
my_pen.fillcolor("#ffdd00")
my_pen.end_fill()
my_pen.home()

my_pen.goto(-40, 100)
my_pen.color("#555555")
my_pen.begin_fill()
my_pen.circle(15)
my_pen.color("#ffffff")
my_pen.end_fill()
my_pen.penup()
my_pen.goto(-48, 110)
my_pen.pendown()
my_pen.color("Black")
my_pen.begin_fill()
my_pen.circle(5)
my_pen.end_fill()
my_pen.penup()

my_pen.goto(40, 100)
my_pen.pendown()
my_pen.color("#555555")
my_pen.begin_fill()
my_pen.circle(15)
my_pen.color("#ffffff")
my_pen.end_fill()
my_pen.penup()
my_pen.goto(32, 110)
my_pen.pendown()
my_pen.color("Black")
my_pen.begin_fill()
my_pen.circle(5)
my_pen.end_fill()
my_pen.penup()

my_pen.goto(-20, 50)
my_pen.pendown()
my_pen.pensize(10)
my_pen.forward(40)

turtle.done()

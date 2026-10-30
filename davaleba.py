import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(9)

def draw_shape(n, size):
    t.begin_fill()
    for _ in range(n):
        t.forward(size)
        t.left(360/n)
    t.end_fill()

t.pencolor("white")
t.left(180)
t.forward(230)
t.left(180)
t.left(90)
t.forward(140)
t.left(270)

for row in range(4):
    for col in range(4):
        if row % 2 == 0:
            if col % 2 == 0:
                t.color("purple")
            else:
                t.color("orange")
        else:
            if col % 2 == 0:
                t.color("cyan")
            else:
                t.color("pink")

        t.pencolor("gray")
        draw_shape(3, 90)
        t.color("white")
        t.forward(115)

    t.left(180)
    t.forward(460)
    t.left(90)
    t.forward(110)
    t.left(90)

turtle.done()
import random
import turtle

tim = turtle.Turtle()
turtle.colormode(255)

colours = [(203, 165, 109), (150, 73, 49), (165, 151, 45), (225, 202, 133), (55, 93, 125), (131, 34, 25),
           (134, 163, 182), (49, 119, 90), (199, 93, 72), (16, 98, 73), (68, 48, 41), (148, 178, 149), (162, 143, 154),
           (234, 175, 165),
           (112, 75, 78), (53, 46, 48),
           (156, 15, 21), (46, 62, 72), (23, 83, 87), (183, 206, 173), (182, 86, 89), (52, 64, 77), (99, 144, 129),
           (19, 71, 60), (109, 126, 151), (219, 175, 179)]


def draw_one_row():
    for _ in range(10):
        tim.pendown()
        tim.color(random.choice(colours))
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.penup()
        tim.forward(50)


def draw_painting():
    tim.hideturtle()
    tim.penup()
    n = -250
    tim.setpos(-225, n)
    tim.speed(0)
    i = 0

    while i < 10:
        draw_one_row()
        n += 50
        tim.goto(-225, n)
        i += 1


draw_painting()

screen = turtle.Screen()

screen.exitonclick()

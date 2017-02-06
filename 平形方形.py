import turtle

def draw_square(t, size):
        for i in range(4):
                t.forward(size)
                t.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

john = turtle.Turtle()
john.pensize(5)
john.color("hotpink")
for i in range(5):
    draw_square(john, 25)
    john.penup()
    john.forward(50)
    john.pendown()

window.exitonclick()


# -*- coding: utf8 -*-
import turtle             
window = turtle.Screen()  
marry = turtle.Turtle()

window.bgcolor("hotpink")
marry.pensize(5)

colors = ["yellow","red","purple","blue","green"]
for i in colors:
    marry.color(i)
    marry.forward(100)
    marry.right(144)

window.exitonclick()

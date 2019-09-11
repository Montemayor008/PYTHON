import turtle
from turtle import *


penup()
turtle.goto(0,-300)

pendown()
turtle.fillcolor('darkred')
turtle.begin_fill()
turtle.rt(270)
turtle.fd(400)
turtle.rt(45)
turtle.fd(200)
turtle.rt(135)
turtle.fd(400)
turtle.rt(45)
turtle.fd(200)
turtle.rt(45)
turtle.fd(300)
turtle.end_fill()
turtle.fillcolor('firebrick')
turtle.begin_fill()
turtle.rt(90)
turtle.fd(400)
turtle.rt(45)
turtle.fd(200)
turtle.rt(45)
turtle.fd(300)
turtle.rt(135)
turtle.fd(200)
turtle.rt(45)
turtle.fd(300)
turtle.end_fill()

turtle.fillcolor('firebrick')
turtle.begin_fill()
turtle.rt(270)
turtle.fd(400)
turtle.rt(270)
turtle.fd(300)
turtle.rt(270)
turtle.fd(400)
turtle.rt(270)
turtle.fd(300)
turtle.end_fill()
#
turtle.rt(270)
turtle.fd(400)
turtle.rt(270)
turtle.fillcolor('saddlebrown')
turtle.begin_fill()
turtle.fd(40)
turtle.rt(270)
turtle.fd(60)
turtle.rt(90)
turtle.fd(60)
turtle.rt(90)
turtle.fd(60)
turtle.end_fill()

turtle.rt(270)
turtle.fd(40)
turtle.fillcolor('saddlebrown')
turtle.begin_fill()
turtle.fd(40)
turtle.rt(270)
turtle.fd(60)
turtle.rt(90)
turtle.fd(60)
turtle.rt(90)
turtle.fd(60)
turtle.end_fill()

def cuadro(lado):
    for i in range(4):
        turtle.fd(lado)
        turtle.rt(90)
        
y = -100
for i in range(3):
    
    x = -10
    for a in range(4):
        penup()
        turtle.goto(x, y)
        pendown()
        turtle.fillcolor('darkslateblue')
        turtle.begin_fill()
        cuadro(40)
        turtle.end_fill()
        x = x-80
    y = y + 80

y = -100
for i in range(3):
    
    x = -10
    for a in range(4):
        penup()
        turtle.goto(x, y)
        pendown()
        turtle.fillcolor('navyblue')
        turtle.begin_fill()
        cuadro(30)
        turtle.end_fill()
        x = x-80
    y = y + 80


penup()
turtle.goto(0,-300)

#i should delete this
#turtle.rt(270)

pendown()
turtle.rt(180)
turtle.fd(400)
turtle.rt(45)
turtle.fd(100)
turtle.fillcolor('saddlebrown')
turtle.begin_fill()
turtle.rt(135)
turtle.fd(400)
turtle.lt(135)
turtle.fd(40)
turtle.lt(45)
turtle.fd(400)
turtle.lt(135)
turtle.fd(40)
turtle.end_fill()
turtle.rt(315)
turtle.fd(10)

#aqui son 20
for x in range (20):
    turtle.lt(135)
    turtle.fd(40)
    turtle.rt(135)
    turtle.fd(10)
    turtle.rt(45)
    turtle.fd(40)
    turtle.lt(45)
    turtle.fd(10)
    

penup()
turtle.goto(0,-300)
turtle.rt(270)
pendown()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.fd(200)
turtle.lt(45)
turtle.fd(200)
turtle.lt(135)
turtle.fd(200)
turtle.end_fill()

penup()
turtle.goto(0,-300)
turtle.lt(180)
turtle.fd(180)
penup()
turtle.lt(90)
turtle.fd(50)
pendown()
turtle.fd(50)


radio = .1
incremento = .2

for i in range(8):
    turtle.circle(radio,195)
    radio = radio + incremento
    incremento = incremento + i
    
penup()
turtle.goto(-500,250)
pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(60,360)
turtle.end_fill()


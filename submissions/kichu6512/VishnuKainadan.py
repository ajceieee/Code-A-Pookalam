import turtle
from turtle import Turtle, write
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
turtle.bgcolor('antiquewhite')
turtle.penup()
style = ('Verdana', 20,'italic')
turtle.setpos(-130,-250)
turtle.write('Happy Onam!', font=('Courier', 30, 'italic'))
turtle.setpos(-340,220)
turtle.write(' ഏവർക്കും ഹൃദയംനിറഞ്ഞ ഓണാശംസകൾ ', font=style)
turtle.setpos(-70,-270)
turtle.write('by Vishnu Kainadan', font=('verdana', 10, 'bold'))
turtle.setpos(-20,-284)
turtle.write('S2 CSE', font=('verdana', 10, 'bold'))
turtle.hideturtle()
########################

t5=turtle.Turtle()
t5.speed("fastest")
for i in range(6):
    for i in range(4):
        t5.pu()
        t5.goto(0,0)
        t5.pd()
        t5.pensize(3)
        t5.color("maroon")
        t5.begin_fill()
        t5.circle(100,steps=6)
        t5.right(100)
        t5.end_fill()
t5.hideturtle()

###############################

t4=turtle.Turtle()    
t4.speed("fastest")
t4.pu()
t4.goto(0,-180)
t4.pd()
t4.pensize(3)
t4.color("brown")
t4.begin_fill()
t4.circle(180)
t4.right(100)
t4.end_fill()
t4.hideturtle()

#################################       

t3=turtle.Turtle()
t3.speed("fastest")
for i in range(6):
    for i in range(4):
        t3.pu()
        t3.goto(0,0)
        t3.pd()
        t3.pensize(3)
        t3.color("red")
        t3.begin_fill()
        t3.circle(82,steps=6)
        t3.right(100)
        t3.end_fill()
t3.hideturtle()

###############################

t2=turtle.Turtle()    
t2.speed("fastest")
t2.pu()
t2.goto(0,-140)
t2.pd()
t2.pensize(3)
t2.color("orangered")
t2.begin_fill()
t2.circle(140)
t2.right(100)
t2.end_fill()
t2.hideturtle()

###############################  

t1=turtle.Turtle()     
t1.speed("fastest")
for i in range(6):
    for i in range(4):
        t1.pu()
        t1.goto(0,0)
        t1.pd()
        t1.pensize(3)
        t1.color("gold")
        t1.begin_fill()
        t1.circle(60,steps=6)
        t1.right(100)
        t1.end_fill()
t1.hideturtle()

###############################

v=turtle.Turtle()
v.speed("fastest")
for i in range(6):
    for i in range(4):
          v.pu()
          v.goto(0,0)
          v.pd()
          v.color("maroon")
          v.pensize(3)
          v.circle(100,steps=6)
          v.right(100)
v.hideturtle()

###############################

t1=turtle.Turtle()    
t1.speed("fastest")
t1.pu()
t1.goto(0,-100)
t1.pd()
t1.pensize(3)
t1.color("white")
t1.begin_fill()
t1.circle(100)
t1.right(100)
t1.end_fill()
t1.hideturtle()

###############################   

v1=turtle.Turtle()    
v1.speed("fastest")
for i in range(6):
    for i in range(4):
        v1.pu()
        v1.goto(0,0)
        v1.pd()
        v1.pensize(3)
        v1.color("green")
        v1.begin_fill()
        v1.circle(40,steps=6)
        v1.right(100)
        v1.end_fill()
v1.hideturtle()

###############################   

v2=turtle.Turtle()    
v2.speed("fastest")
v2.pu()
v2.goto(0,-60)
v2.pd()
v2.pensize(3)
v2.color("orange")
v2.begin_fill()
v2.circle(60)
v2.right(100)
v2.end_fill()
v2.hideturtle()

###############################   

v3=turtle.Turtle()    
v3.speed("fastest")
v3.pu()
v3.goto(0,-40)
v3.pd()
v3.pensize(3)
v3.color("gold")
v3.begin_fill()
v3.circle(40)
v3.right(100)
v3.end_fill()
v3.hideturtle()

###############################   

def draw_petal(turtle, radius):
    heading = turtle.heading()
    bob.color("maroon")
    bob.begin_fill()
    turtle.circle(radius, 60)
    turtle.left(120)
    bob.end_fill()
    turtle.circle(radius, 60)
    turtle.setheading(heading)

my_radius = int(35)
my_petals = int(16)

bob = Turtle()
bob.speed("fastest")
for _ in range(my_petals):
    draw_petal(bob, my_radius)
    bob.left(360 / my_petals)
    
bob.hideturtle()

###############################   

v3=turtle.Turtle()    
v3.speed("fastest")
v3.pu()
v3.goto(0,-10)
v3.pd()
v3.pensize(3)
v3.color("gold")
v3.begin_fill()
v3.circle(10)
v3.right(100)
v3.end_fill()
v3.hideturtle()

###############################   

v3=turtle.Turtle()    
v3.speed("fastest")
v3.pu()
v3.goto(0,-5)
v3.pd()
v3.pensize(3)
v3.color("saddle brown")
v3.begin_fill()
v3.circle(5)
v3.right(100)
v3.end_fill()
v3.hideturtle()


turtle.done()

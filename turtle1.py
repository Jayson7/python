import turtle
from turtle import *

jayson = turtle.Turtle()
jayson.speed(10)

jayson. color('green', 'yellow')

cl = ['red','green','blue']
jayson.speed(50)
def drawArt(angle,d,x,y):

  jayson.up()
  jayson.goto(x,y)
  jayson.down()
  c = 0
  for i in range(1,400):
    jayson.pencolor(cl[c])
    jayson.forward(d)
    jayson.left(angle)
    d = d - 2
    c = c + 1
    if(c>2):
      c=0

  
drawArt(175,200,0,-50)
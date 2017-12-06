from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape = ("circle")
        self.shapesize(radius/10)
        self.radius =radius
        self.color(color)
        self.speed(speed)

ball1=Ball(10,"black",30)
ball2=Ball(15,"red",40)

def check_collision(ball1,ball2):
    if math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2))<= ball1.radius+ball2.radius:
        print("balls are in collision")

    else:
        print("balls are not colliding")


check_collision(ball1,ball2)

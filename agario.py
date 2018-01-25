import turtle
import time
import random
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()

RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)

MY_BALL=Ball(0,0,70,80,20,"blue")

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]


for i in range (NUMBER_OF_BALLS):
    x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
    y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color=(random.random(),random.random(),random.random())
    Ball1=Ball(x,y,dx,dy,radius,color)
    BALLS.append(Ball1)


for i in BALLS:
    i.move(SCREEN_HEIGHT,SCREEN_WIDTH)


def collide (ball_a, ball_b):

    if ball_a==ball_b:
        return False
    if math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+mat.pow(ball_a.xcor-ball_b.xcor(),2))+10 <= (ball_a.radius+ball_b.radius):
        return True
    else:
        return False



def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS :
            if collide(ball_a,ball_b):
                ball1.r=ball_a.radius
                ball2.r=ball_b.radius
                x.cor=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                y.cor=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color=(random.random(),random.random(),random.random())

           
        
    




    

    

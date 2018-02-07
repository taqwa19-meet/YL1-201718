import turtle,time,random
from ball import Ball
import math
turtle.tracer(delay=0)
turtle.hideturtle()
turtle.bgcolor("pink")
RUNNING=True
SLEEP=0.05
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)

MY_BALL=Ball(0,0,0,0,100,"purple")

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=50
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
    r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color=(random.random(),random.random(),random.random())
    ball=Ball(x,y,dx,dy,r,color)
    BALLS.append(ball)



def move_all_balls():
    for ball in BALLS:
        ball.move(SCREEN_HEIGHT,SCREEN_WIDTH)
    
    

def collide (ball_a, ball_b):
    D=math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(), 2 )+math.pow(ball_a.ycor()-ball_b.ycor(), 2))
    sum_r = ball_a.r + ball_b.r
    if (ball_a== ball_b):
        return False
    if (D+10 <= sum_r):
        return True
    return False
                
        


def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS :
            if collide(ball_a,ball_b):
                x_cor=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                y_cor=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color=(random.random(),random.random(),random.random())

                while dx==0:
                    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                while dy==0:
                    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

                if ball_a.r>ball_b.r:
                  ball_a.r+=1
                  ball_a.shapesize(ball_a.r/10)

                  ball_b.goto(x_cor,y_cor)
                  ball_b.dx=dx
                  ball_b.dy=dy
                  ball_b.color(color)
                  ball_b.r=radius
                  ball_b.shapesize(r/10)

                else:
                    ball_b.r+=1
                    ball_b.shapesize(ball_b.r/10)

                    ball_a.goto(x_cor,y_cor)
                    ball_a.dx=dx
                    ball_a.dy=dy
                    ball_a.color(color)
                    ball_a.r=radius
                    ball_a.shapesize(r/10)

def check_myball_collision():
    for i in BALLS:
        if collide(MY_BALL,i)==True:
            print("balls in collision: "+str(collide(MY_BALL, i)))
            my_r=MY_BALL.r
            ur_r=i.r 
            
            X=random.randint(round(-SCREEN_WIDTH)+MAXIMUM_BALL_RADIUS, round(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
            Y=random.randint(round(-SCREEN_HEIGHT)+MAXIMUM_BALL_RADIUS,round(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS) 

            dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
            while(dx==0):
                dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

            dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
            while(dy==0):
                dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

            Radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
            new_color=(random.random(), random.random(), random.random())

            if(MY_BALL.r<i.r):
                return False
            else:
                if (MY_BALL.r<=500):
                    MY_BALL.r+=1
                    MY_BALL.shapesize(MY_BALL.r/10)
                i.goto(X,Y)
                i.dx=dx
                i.dy=dy
                i.color(new_color)
                i.r = Radius
                i.shapesize(Radius/10)
                return True
    return True


def movearound(event):
    X= event.x - SCREEN_WIDTH
    Y= SCREEN_HEIGHT - event.y
    MY_BALL.goto(X,Y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()


while RUNNING==True:
    if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2:
        SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2) 
        SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)
    move_all_balls()


    check_all_balls_collision()

    #MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)

    RUNNING=check_myball_collision()

    turtle.getscreen().update()

    time.sleep(SLEEP)

turtle.mainloop()

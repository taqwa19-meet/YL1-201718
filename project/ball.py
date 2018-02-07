from turtle import Turtle

class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.x = x
        self.y = y
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color(color)
        self.shape("circle")
        self.shapesize(r/10)

    def move (self,screen_width,screen_height):
        current_x = self.x
        new_x=self.x+self.dx
        current_y = self.y
        new_y = self.y+self.dy
        right_side_ball = new_x+self.r
        left_side_ball= new_x-self.r
        up_side_ball=new_y+self.r
        down_side_ball=new_y-self.r
        self.goto(new_x,new_y)
        if (new_x==-(screen_width*0.5)):
            self.dx=-self.dx
        if (new_y==-(screen_height*0.5)):
            self.dy=-self.dy
        if (new_x==-(screen_width*0.5)):
            self.dx=-self.dx
        if (new_y==-(screen_height*0.5)):
            self.dy=-self.dy

#Ball(50,50,20,20,15,"red")

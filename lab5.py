from turtle import *
#colormode(255)

#class Square (Turtle):
   #def __init__(self,size):
        #Turtle.__init__(self)
        #self.shapesize(size)
        #self.shape("square")

#sss12=Square(20)

class hexagon (Turtle):
    def __init__ (self,size,speed,color):
        Turtle.__init__(self)
        self.speed(speed)
        self.color(color)
        self.begin_poly()
        self.penup()
        for i in range(6):
            self.fd(size)
            self.left(60)
        self.end_poly()

        #self.shapesize(size)
        hx2=self.get_poly()

        register_shape("hexagon", hx2)

        self.shape("hexagon")

hx = hexagon(60)



        
        

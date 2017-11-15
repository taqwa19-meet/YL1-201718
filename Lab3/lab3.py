import turtle

turtle.speed (0)

for eye in range (360):
    
    turtle.forward(180)
    turtle.right(50)
    turtle.forward(100)
    turtle.right(70)
    turtle.forward(50)
    turtle.back(30)
    turtle.forward(40)

    turtle.penup()
    turtle.goto(0,0)
    turtle.right(0.16)
    turtle.pendown()




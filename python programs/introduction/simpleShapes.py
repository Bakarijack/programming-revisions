import  turtle

turtle.pensize(10) #set the pen to 10 pixels thickness
turtle.penup()     #puts the pen up
turtle.goto(-200,-50)
turtle.pendown() #puts the pen down
turtle.circle(40, steps=3)  #drows a triangle

turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.circle(40,steps=4)

turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(40,steps=5)

turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.circle(40,steps=6)

turtle.penup()
turtle.goto(200,-50)
turtle.pendown()
turtle.circle(40)

turtle.penup()
turtle.color("red")
turtle.pensize(10)
turtle.goto(300,-50)
turtle.pendown()
turtle.circle(3)

turtle.done()
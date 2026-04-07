from turtle import *

screen = Screen()

screen.title("Write your name")
screen.bgcolor("Black")
screen.setup(width= 1000, height= 600)

yertle = Turtle()
yertle.color("yellow")
yertle.shape("turtle")

# for j in range(4):
#     for i in range(5):
#         yertle.forward(10)
#         yertle.penup()
#         yertle.forward(10)
#         yertle.pendown()
#     yertle.left(90)

# while True:
#     angle = int(input("What direction do you want Yertle to face?"))
#     yertle.setheading(angle)

# yertle.pu()
# yertle.goto(-100, -100)
# yertle.pd()
# yertle.sety(100)
# yertle.setx(100)
# yertle.sety(-100)
# yertle.setx(-100)
# yertle.home()

# for i in range(360):
#     yertle.forward(1)
#     yertle.right(1)

# yertle.circle(-50, 180)

yertle.pu()
yertle.goto(-300, 0)
yertle.pd()
yertle.goto(-300,100)
yertle.goto(-250,100)
yertle.pu()
yertle.goto(-300,50 )
yertle.pd()
yertle.goto(-250,50)
yertle.pu()
yertle.goto(-300, 0)
yertle.pd()
yertle.goto(-250,0)
yertle.pu()
yertle.goto(-200, 0)
yertle.pd()
yertle.goto(-200, 100)
yertle.pu()
yertle.goto(-150, 0)
yertle.pd()
yertle.goto(-150, 75)
yertle.pu()
yertle.goto(-150,90)
yertle.pd()
yertle.circle(5,360)
yertle.pu()
yertle.goto(-125,25)
yertle.pd()
yertle.setheading(-90)
yertle.circle(25,180)
yertle.forward(75)
yertle.pu()
yertle.goto(-25,0)
yertle.pd()
yertle.setheading(0)
yertle.circle(35)
yertle.pu()
yertle.goto(10,25)
yertle.pd()
yertle.goto(35,0)
yertle.pu()
yertle.goto(55,0)
yertle.pd()
yertle.goto(55,100)
yertle.pu()
yertle.goto(55,50)
yertle.pd()
yertle.forward(25)
yertle.setheading(-90)
yertle.forward(50)















screen.exitonclick()
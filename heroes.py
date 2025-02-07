from turtle import Turtle, Screen
import heroes




my_turtle = Turtle()


my_turtle.shape("turtle")
my_turtle.color("DarkGreen")


for i in range(20):
    if i % 2 == 0:
        my_turtle.pu()
    else:
        my_turtle.pd()
    my_turtle.fd(10)


print(heroes.gen())



screen = Screen()
screen.exitonclick()



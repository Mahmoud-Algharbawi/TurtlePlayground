import turtle as t
import random




#initialize turtle and screen objects
my_turtle = t.Turtle()
screen = t.Screen()
screen.colormode(255)

"""
Function draw_spiro: a function that takes the angle size as an input, and draws a spiro with the turn angle provided

input: 
    size -> int
        The size of the turn angle of which the turtle will turn
"""
def draw_spiro(size):
    my_turtle.speed("fastest")
    
    #divide the circle by the size of the angle provided to turn the turtle 
    for i in range(int(360 / size)):
        colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        my_turtle.color(colors)
        my_turtle.circle(100)
        my_turtle.seth(my_turtle.heading() + size)
    
    
    






# calling the draw_spiro function
draw_spiro(5)



screen.exitonclick()
# from turtle import Turtle, Screen
import random
import turtle





#create the turtle object
my_turtle = turtle.Turtle()

#define the colors that will be chosen
colors = [
    'navy', 'darkblue', 'royalblue', 'steelblue', 'darkgreen',
    'forest green', 'dark orchid', 'medium purple', 'indigo', 'slate blue',
    'dark slate blue', 'medium blue', 'purple', 'dark violet', 'maroon',
    'dark slate gray', 'medium sea green', 'saddle brown', 'midnight blue', 'dark olive green'
]


screen = turtle.Screen()
turtle.colormode(255)




"""
draw_randomly: a function that will take the number of segments to draw and will draw segments in random directions
input:
    frequency -> int
        the number of segments that will be drawn
"""
def draw_randomly(frequency):
    my_turtle.speed("fastest")
    my_turtle.pensize(10)
    screen.colormode(255)
    
    # draw the segments in radnom directions, each degment will be a different by using the (r, g, b) numbers
    for i in range(frequency):
        color = random.choice(colors)
        rgb1 = random.randint(0, 255)
        rgb2 = random.randint(0, 255)
        rgb3 = random.randint(0, 255)
        my_turtle.color(rgb1, rgb2, rgb3)
        angle = random.randint(0, 3) * 90
        my_turtle.seth(angle)
    
        my_turtle.fd(20)
        
#call the function and pass the amount of segments to draw randomly
draw_randomly(200)



screen.exitonclick()
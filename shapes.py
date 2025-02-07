from turtle import Turtle, Screen
import random




my_turtle = Turtle()
colors = [
    'navy', 'darkblue', 'royalblue', 'steelblue', 'darkgreen',
    'forest green', 'dark orchid', 'medium purple', 'indigo', 'slate blue',
    'dark slate blue', 'medium blue', 'purple', 'dark violet', 'maroon',
    'dark slate gray', 'medium sea green', 'saddle brown', 'midnight blue', 'dark olive green'
]

def draw_shape(sides, color):
        
    angle = 360 / sides
    my_turtle.color(color)
    print(angle)
    
    for i in range(0,sides):
    
        my_turtle.fd(100)
        my_turtle.rt(angle)
        
        

    
for i in range(3, 10):
    draw_shape(i, random.choice(colors))
    
screen = Screen()
screen.exitonclick()
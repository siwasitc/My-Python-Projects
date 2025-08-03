import turtle as t
import random

## Below is to extract the color list from the Spot Painting
# import colorgram
#
# colors = colorgram.extract("spot_painting.jpg",24)
# rgb_colors = []
# for i in range(len(colors)):
#     colors[i] = colors[i].rgb
#     r = colors[i].r
#     g = colors[i].g
#     b = colors[i].b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# for i in range(4):
#     rgb_colors.remove(rgb_colors[0])    # Remove the first color, because it is probably White.
# print(rgb_colors)

DOT_SIZE = 20
DOT_SPACING = 50

def paint_the_dot(brush, num_dot):
    for a_dot in range(num_dot):
        color_choice = random.choice(colors_list)
        brush.dot(DOT_SIZE, color_choice)
        brush.forward(DOT_SPACING)

def go_up(brush):
    brush.setheading(90)
    brush.forward(DOT_SPACING)

def turn_left(brush):
    brush.left(90)
    brush.forward(DOT_SPACING)

def turn_right(brush):
    brush.right(90)
    brush.forward(DOT_SPACING)

colors_list = [(180, 177, 8), (174, 4, 60), (244, 19, 147), (243, 65, 5), (9, 139, 18), (42, 195, 236), (8, 132, 207),
               (88, 4, 94), (194, 5, 2), (8, 168, 129), (236, 164, 41), (229, 16, 129), (243, 227, 46), (248, 79, 13),
               (252, 231, 0), (213, 128, 175), (253, 4, 6), (252, 6, 4), (246, 156, 199), (111, 189, 147)]

t.colormode(255)    # Set up the color mode to be RGB mode
screen = t.Screen()
screen.screensize(300,300)

my_brush = t.Turtle()
my_brush.penup()
my_brush.hideturtle()
my_brush.speed("fastest")
my_brush.teleport(-250, -250)   # Set the starting point of the painting

for row in range(10):
    paint_the_dot(my_brush,10)
    go_up(my_brush)
    if row % 2 == 0:
        turn_left(my_brush)
    else:
        turn_right(my_brush)

screen.exitonclick()

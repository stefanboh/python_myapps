import turtle
import random
# import colorgram
#
# colors = colorgram.extract("image.jpg", 40)
# rgb_c = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_c.append(new_color)
# print(rgb_c)
turtle.colormode(255)
tom = turtle.Turtle()
tom.speed("fastest")
tom.hideturtle()
tom.penup()
color_list = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42), (216, 90, 52), (173, 178, 231), (235, 170, 164), (8, 244, 224), (248, 9, 44), (10, 77, 114), (20, 53, 243)]


tom.setheading(225)
tom.forward(300)
tom.setheading(0)
num_of_dots = 101

for dot_count in range(1, num_of_dots):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)
    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
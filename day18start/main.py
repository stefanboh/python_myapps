import turtle as t
import random


tom = t.Turtle()
t.colormode(255)
tom.shape("turtle")
# timmy_the_turtle.color("green")

#1
# for i in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(200)
#2
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#3
# cut = 2
# for _ in range(15):
#     cut += 1
#     angle = 360 / cut
#
#     for turn in range(cut):
#         timmy_the_turtle.right(angle)
#         timmy_the_turtle.forward(100)
#4



def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tom.speed(1000)


def draw(size_of_gap):
    for _ in range(360 // size_of_gap):
        tom.color(rand_color())
        tom.circle(50)
        current_loc = tom.heading()
        tom.setheading(current_loc + size_of_gap)
        tom.circle(50)

draw(10)

screen = t.Screen()
screen.exitonclick()
# colours = ["green", "red", "yellow"," blue", "purple"]
# is_on = True
# timmy_the_turtle.speed(100)
# while is_on:
#     timmy_the_turtle.pensize(15)
#     # timmy_the_turtle.color(random.choice(colours))
#
#     timmy_the_turtle.color(rand_color())
#     road = random.randint(0, 4)
#     for _ in range(road):
#         timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(30)
#5




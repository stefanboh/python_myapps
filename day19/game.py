import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win: ")
colors = ['red', 'orange', "green", "blue", "purple","yellow"]
y_pos = [-130,-80,-30,20,70,120]
all_turtle = []

for turtle_index in range(0,6):

    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 200:
            win_color = turtle.pencolor()
            print(f"{win_color} won")
            if win_color == user_bet:
                print("You win")
            else:
                print("You lost")
            is_race_on = False
        r_distance = random.randint(0,30)
        turtle.forward(r_distance)




screen.exitonclick()
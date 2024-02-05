from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(30)
def turn_l():
    tim.left(15)

def turn_r():
    tim.right(15)
def go_back():
    tim.back(10)

def clear():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_l)
screen.onkey(key="d", fun=turn_r)
screen.onkey(key="s", fun=go_back)
screen.onkey(key="c", fun=clear)


screen.exitonclick()


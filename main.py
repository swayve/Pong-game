from turtle import Turtle, Screen
from screen_assets import Paddle, Paddle2, Line
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)


line = Line()
paddle_right = Paddle()
paddle_left = Paddle2()


screen.listen()
screen.onkey(paddle_right.righto, "Up")
screen.onkey(paddle_right.lefto, "Down")



screen.exitonclick()

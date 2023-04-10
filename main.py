from turtle import Turtle, Screen
from paddle import Paddle, Paddle2
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)



paddle_right = Paddle()
paddle_left = Paddle2()


screen.listen()
screen.onkey(paddle_right.right, "Up")
screen.onkey(paddle_left.left, "Left")



screen.exitonclick()

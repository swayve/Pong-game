from turtle import Turtle, Screen
from screen_assets import Paddle, Line
from pong import Pong
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)



line = Line()
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Pong()


screen.listen()
screen.onkey(paddle_right.righto, "Up")
screen.onkey(paddle_right.lefto, "Down")

screen.onkey(paddle_left.righto, "w")
screen.onkey(paddle_left.lefto, "s")


game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    
    if ball.ycor() > 300 or ball.ycor() > -300:
        ball.bounce()



screen.exitonclick()

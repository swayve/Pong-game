from turtle import Turtle, Screen
from screen_assets import Paddle
from pong import Pong
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Pong()
scoarboard = ScoreBoard()


screen.listen()
screen.onkey(paddle_right.righto, "Up")
screen.onkey(paddle_right.lefto, "Down")

screen.onkey(paddle_left.righto, "w")
screen.onkey(paddle_left.lefto, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with walls on the Horizontal sides
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    
    #Detect collision
    if ball.distance(paddle_right) < 50  and ball.xcor()  > 320:
        ball.bounce_x()
        print("Made contact")
    
    if ball.distance(paddle_left) < 50  and ball.xcor()  > -320:
        ball.bounce_x()
        print("Made contact")
    
    #Detect if ball went out of bound then place it back to the center
    if ball.xcor() > 380:
        time.sleep(0.1)
        ball.center()
        scoarboard.l_score += 1
    
    
    if ball.xcor() > -380:
        time.sleep(0.1)
        ball.center()
        scoarboard.r_score += 1



    


    


screen.exitonclick()

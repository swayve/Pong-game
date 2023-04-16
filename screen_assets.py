from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()                                                                                                                                                                                                                      
        self.shape("square")
        self.setpos((position))
        self.color("white") 
        self.shapesize(5, 1)
        self.penup()

    def righto(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def lefto(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.circle(20)



class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 350)
        self.color("white")
        self.pensize(6)
        self.right(90)

        for i in range(45):
            self.forward(15)
            self.pendown()
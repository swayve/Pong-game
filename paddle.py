from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()                                                                                                                                                                                                                      
        self.shape("square")
        self.setpos(350, 0)
        self.color("white") 
        self.shapesize(5, 1)
        self.penup()

    def right(self):
        self.forward(10)

    def left(self):

        self.forward(10)



class Paddle2(Turtle):
    def __init__(self):
        super().__init__()                                                                                                                                                                                                                      
        self.shape("square")
        self.setpos(-350, 0)
        self.color("white") 
        self.shapesize(5, 1)
        self.penup()
    
    def right(self):
        self.forward(10)

    def left(self):
        self.forward(10)



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import choice,randint


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.shapesize(1,2)
        self.penup()
        self.goto(300,randint(-300,300))
        
    def move(self):
        self.goto(self.xcor()-STARTING_MOVE_DISTANCE,self.ycor())

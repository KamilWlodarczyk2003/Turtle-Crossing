COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import choice,randint


class CarManager(Turtle):
    
    def __init__(self,level):
        self.speed=STARTING_MOVE_DISTANCE+(level-1)*STARTING_MOVE_DISTANCE
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.shapesize(1,2)
        self.penup()
        self.goto(300,randint(-300,300))
        
    def move(self):
        self.goto(self.xcor()-self.speed,self.ycor())

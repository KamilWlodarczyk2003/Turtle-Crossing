COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] #colors of cars
STARTING_MOVE_DISTANCE = 5 #starting speed
MOVE_INCREMENT = 10 #speed increment
from turtle import Turtle
from random import choice,randint


class CarManager(Turtle):
    
    def __init__(self,level):
        self.speed=STARTING_MOVE_DISTANCE+(level-1)*STARTING_MOVE_DISTANCE  #every level increase the speed of cars
        super().__init__()
        self.shape("square")    #shape of cars
        self.color(choice(COLORS))  #randomly choose color of a car
        self.shapesize(1,2) #shape of a car
        self.penup()
        self.goto(300,randint(-300,300))    #starting position
        
    def move(self):     #function moving cars across x axis
        self.goto(self.xcor()-self.speed,self.ycor())

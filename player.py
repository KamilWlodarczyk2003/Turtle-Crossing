from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280     #point in y axis where you win if you pass it


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")    #shape of a player
        self.left(90)   #rotate turtle to face upward
        self.penup()
        self.shapesize()
        self.goto(STARTING_POSITION)
        
    def restart(self):      #move player to starting position
        self.goto(STARTING_POSITION)
        
    def move(self):     #move a player upwards
        self.goto(0,self.ycor()+MOVE_DISTANCE)

LEVEL_FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 30, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        self.level=1    #set a starting level
        super().__init__()
        self.penup()
        self.ht()
        self.goto(0,240)    #position of scoreboard
        
        
    def show(self):     #create text in a scoreboard
        self.write(f"Level {self.level}", font=LEVEL_FONT,align="center")
        
    def game_over(self):    #display game over sentence
        self.goto(0,0)
        self.write("game over", font=GAME_OVER_FONT,align="center")

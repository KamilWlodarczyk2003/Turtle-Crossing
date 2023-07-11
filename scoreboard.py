LEVEL_FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 30, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        self.level=1
        super().__init__()
        self.penup()
        self.ht()
        self.goto(0,240)
        
        
    def show(self):
        self.write(f"Level {self.level}", font=LEVEL_FONT,align="center")
        
    def game_over(self):
        self.goto(0,0)
        self.write("game over", font=GAME_OVER_FONT,align="center")

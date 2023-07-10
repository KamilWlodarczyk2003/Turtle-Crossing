import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()

screen.listen()

Cars=[]

game_is_on = True
while game_is_on:
    guess=randint(0,5)
    if guess==1:
        Cars.append(CarManager())
    for x in Cars:
        x.move()
    time.sleep(0.1)
    screen.update()
    screen.onkeypress(player.move,"Up")

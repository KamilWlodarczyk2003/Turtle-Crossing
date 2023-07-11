import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard=Scoreboard()

player=Player()



screen.listen()



game_is_on = True
while game_is_on:
    Cars=[]
    same_level=True
    scoreboard.show()
    while same_level==True:
        guess=randint(0,2)
        if guess==1:
            Cars.append(CarManager(scoreboard.level))
        for x in Cars:
            if player.distance(x.xcor(),x.ycor())<21:
                scoreboard.game_over()
                same_level=False
                game_is_on=False
            x.move()
            if x.xcor()<-350:
                del Cars[Cars.index(x)]
        time.sleep(0.1)
        screen.update()
        screen.onkeypress(player.move,"Up")
        if player.ycor()>300:
            same_level=False
            scoreboard.level+=1
            for x in Cars:
                x.ht()
            scoreboard.clear()
            player.restart()
            
screen.exitonclick()
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()

screen.listen()  #enable collection of key-events

game_is_on = True
while game_is_on:
    Cars = []
    same_level = True  #decide if level has ended
    scoreboard.show()
    while same_level == True:
        guess = randint(0, 2)  #decide if new car appear or not
        if guess == 1:
            Cars.append(CarManager(scoreboard.level))
        for x in Cars:
            if player.distance(x.xcor(), x.ycor()) < 21:  #colision detection
                scoreboard.game_over()  #game over display
                same_level = False
                game_is_on = False
            x.move()
            if x.xcor() < -350:
                del Cars[Cars.index(x)]  #delete cars that arrived the and of X axis
        time.sleep(0.1)
        screen.update()
        screen.onkeypress(player.move, "Up")  #move player on up key press
        if player.ycor() > 300:  #When player reaches the end
            same_level = False
            scoreboard.level += 1   #set new level
            for x in Cars:
                x.ht()      #hide cars from existing level
            scoreboard.clear()
            player.restart()

screen.exitonclick()

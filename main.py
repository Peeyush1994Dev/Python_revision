from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


new_segment = Turtle()
screen = Screen()
snake_activity = Snake()

Snake_food = Food()
Score_board = Scoreboard()


# Snake- key -Movement
screen.listen()
screen.onkey(snake_activity.up, "w")
screen.onkey(snake_activity.down, "s")
screen.onkey(snake_activity.left, "a")
screen.onkey(snake_activity.right, "d")

screen.bgcolor("black")
screen.screensize(600, 600)

Game_is_on = True

while Game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_activity.move()

    if snake_activity.head.distance(Snake_food) < 15:
        Snake_food.refresh()
        snake_activity.extend()
        Score_board.increment()

    if snake_activity.head.xcor() > 300 or snake_activity.head.ycor() > 300 or snake_activity.head.xcor() < -300 or snake_activity.head.ycor() < -300:
        Game_is_on = False
        Score_board.game_over()

    for segment in snake_activity.Snake_segment:
        if segment == snake_activity.head:
            pass
        elif snake_activity.head.distance(segment) < 10:
            Game_is_on = False
            Score_board.game_over()




screen.exitonclick()




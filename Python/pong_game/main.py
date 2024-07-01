from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
game_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    game_ball.move()

    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()

    if (game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320) or game_ball.distance(left_paddle) < 50 and \
            game_ball.xcor() < -320:
        game_ball.bounce_x()

    if game_ball.xcor() > 380:
        game_ball.reset_position()
        scoreboard.left_point()

    elif game_ball.xcor() < -380:
        game_ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()

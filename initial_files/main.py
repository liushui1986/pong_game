from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
game_on = True

bullet = Ball()
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
scoreboard = Scoreboard()


# When escape, the bullet will go back to the start point with original speed, all scores will become 0.
def on_escape():
    bullet.replay()
    scoreboard.restart()


screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'W')
screen.onkeypress(l_paddle.go_down, 'S')
screen.onkey(on_escape, 'Escape')  # When use Esc, the whole game will restart.
screen.listen()

while game_on:
    time.sleep(bullet.move_speed)
    screen.update()
    bullet.move()

    # Detect collision on upwall or downwall
    if bullet.ycor() > 280 or bullet.ycor() < -280:
        bullet.bonce_wall()

    # Detect collision with the paddle
    if bullet.distance(r_paddle) < 50 and bullet.xcor() > 350 or bullet.distance(
            l_paddle) < 50 and bullet.xcor() < -350:
        bullet.bonce_paddle()

    # Detect missing the ball
    if bullet.xcor() > 390:
        bullet.replay()
        scoreboard.l_point()

    if bullet.xcor() < -390:
        bullet.replay()
        scoreboard.r_point()

screen.exitonclick()

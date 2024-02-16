import time
import turtle
from random import randint

window = turtle.Screen()

player = turtle.Turtle()
player.shape("turtle")
player.shapesize(2)
score = 0

timer_text = turtle.Turtle()
timer_text.shape("blank")
timer_text.penup()
timer_text.goto(0, 260)

score_text = turtle.Turtle()
score_text.shape("blank")
score_text.penup()
score_text.goto(0, 220)

gameOver_text = turtle.Turtle()
gameOver_text.shape("blank")
gameOver_text.penup()
gameOver_text.goto(0, 0)

game_over = False


def update_score(x, y):
    global score, game_over
    if not game_over:
        score += 1
        score_text.clear()
        score_text.write(f"Score: {score}", align="center", font=("Courier", 20, "normal"))


player.onclick(update_score)

start = time.time()
while time.time() - start < 21:
    remaining_time = 20 - int(time.time() - start)
    timer_text.clear()
    timer_text.write(f"Time: {remaining_time}", align="center", font=("Courier", 20, "normal"))

    player.penup()
    player.hideturtle()
    player.goto(randint(-300, 300), randint(-300, 300))
    player.showturtle()
    time.sleep(0.5)

    window.update()

game_over = True

if game_over:
    gameOver_text.write("Game Over!", align="center", font=("Courier", 40, "bold"))

turtle.done()

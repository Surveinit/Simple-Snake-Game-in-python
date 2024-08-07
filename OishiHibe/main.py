from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#1e1e1e")
screen.title("OishiHibe")
screen.listen()
screen.tracer(0)

# user input takes float **DIFFICULTY**
user_input = float(
    screen.textinput(title="Difficulty", prompt="0.1, 0.5, 1 which difficulty you can bear? Lesser the harder"))
print(user_input)

###########################################################################################
snake = Snake()
food = Food()
score = Score()

screen.listen()

def vim_key_bindings():
    screen.listen()
    screen.onkey(snake.up, 'k')
    screen.onkey(snake.left, 'h')
    screen.onkey(snake.down, 'j')
    screen.onkey(snake.right, 'l')

game_on = True
vim_key_bindings()

def reset_game():
    global snake, food, score, game_on
    snake.reset()
    food.refresh()
    score.game_over()
    game_on = True
    vim_key_bindings() 


while game_on:
    screen.update()
    time.sleep(user_input)  #user_input this function is responsible for the difficulty set

    snake.move()

    # Detects Food collision
    if snake.head.distance(food) < 15:  # Measures the distance of the given turtle
        print("Won")
        score.increase_score()
        food.refresh()
        snake.extend()

    # Detects Wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
        message = screen.textinput(f"Game Over", f"Your score is {score.score_int}. Play again? (y/n)")

        # Check user input and act accordingly
        if message.lower() == "y":
            game_on = True
            reset_game()
        else:
            game_on = False
            snake.bye()

   # Detects collision with snake itself except for head
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()

# TODO: Add music uwu after coliding!
# TODO: Add ENTER keybinding for difficulty prompt
# TODO: Add requirements.txt
# TODO: Update README.md


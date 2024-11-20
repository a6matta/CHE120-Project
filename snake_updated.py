"""Snake, classic arcade game.
In the original game, the snake is moved across the game screen and needs to eat "food" while avoiding
hitting itself or the edges of the game screen limits. 

In our modified version, there will be randomly placed obstacles that the snake will need to AVOID, and
the game will end if the snake hits the obstacle, itself, or the game screen limits.
"""
from random import randrange
from turtle import *
from freegames import square, vector

food = vector(0, 0)
bad_food = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
snake = [vector(10, 0)]
aim = vector(0, -10)
obstacles = [vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10) for _ in range(3)]


def change(x, y):
    aim.x = x
    aim.y = y

def inside(position):
    return -200 < position.x < 190 and -200 < position.y < 190

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake or head in obstacles:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake length:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    elif head == bad_food:
        print('Ate bad food! Snake length:', len(snake))
        bad_food.x = randrange(-15, 15) * 10
        bad_food.y = randrange(-15, 15) * 10

        if len(snake) > 1:
            snake.pop(0)
        else:
            square(head.x, head.y, 9, 'red')
            update()
            return

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'blue')
    square(bad_food.x, bad_food.y, 9, 'yellow')

    for obstacle in obstacles:
        square(obstacle.x, obstacle.y, 9, 'black')

    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

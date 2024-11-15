#I divided it up into groups of 10ish lines so everyone can choose one to do the comments for
#AB: Ashley Burton
#AM: Alisha Matta
#AH: Areeba Hasan
#GS: Gouri Sureshkumar
"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
#------------------------------------------------------------------------------------

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
#-----------------------------------------------------------------------------------
    #AH 
    snake.append(head)  #AH -> #.append attaches an element to the end of a list so:
    # this adds the new head position to the end of the snake list, which grows the snake by one segment. 
    #Since the last element of the is the head, the new position of the snake's head is added to the end, and this
    #represents the snake moving forward (since the list reflects the snake's body from head to tail - the consistent updatng
    #of head position makes the snake appear to be moving forward as required in game play) 
    
    #AH -> # This section is to check if snake eats the food 
    if head == food:
        print('Snake:', len(snake)) #AH -> #Print length of snake
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #AH -> #The for loop iterates over each segment in the snake list
    for body in snake:
    #AH -> from freegames import square above so square() from the freegames library -> 
    #Draw square at (x, y) with side length size and fill color name. The square is oriented so the bottom left corner is at (x, y)
        square(body.x, body.y, 9, 'black')
#------------------------------------------------------------------------------------
    square(food.x, food.y, 9, 'green')
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

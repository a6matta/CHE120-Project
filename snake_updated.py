"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""
#Import Statements remain the same as the original game 
from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0) #Needs to be edited to reflect the obstacles - need to finalize how many we want (since this is just one food at a time)
#We also need to decide if we want the blocks to move around (maybe every few frames - they change position??) 

#The snake and the snake's direction should also remain the same
snake = [vector(10, 0)] 
aim = vector(0, -10) 

#Doesn't need to be altered 
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

#Doesn't need to be altered 
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

#Doesn't need to be altered 
def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

#________________________________________________________________________________________________________

    if not inside(head) or head in snake: #The end game condition needs to changed to include "running into obstacle = faliure" as well 
        square(head.x, head.y, 9, 'red')
        update()
        return
    
    snake.append(head) #Makes the snake appear to be moving so also does not need to be changed 

    if head == food: #Needs to be changed (since running into obstacle isn't the desired goal anymore) 
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0) #Does the altered game require the snake to grow size? Or do we maintain the same size? If so, this is still needed 
        #But probably need to move it up since we'll need to change the if statement

    clear() #Ensures smooth transitions, also stays the same 
    #Buildng of snake does not need to be altered 
    for body in snake:
        square(body.x, body.y, 9, 'black')

    #Needs to be changed to reflect obstacle position and movement 
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

#Setup stays the same 
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

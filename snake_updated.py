"""Snake, classic arcade game.
In the original game, the snake is moved across the game screen and needs to eat "food" while avoiding
hitting itself or the edges of the game screen limits. 

In our modified version, there will be randomly placed obstacles that the snake will need to AVOID, and
the game will end if the snake hits the obstacle, itself, or the game screen limits. There will also be the addition of "bad" food, that
will shorten the snake, along with the "good" food from the original version. 
"""
from random import randrange  # Import the randrange function for generating random positions
from turtle import *  # Import all turtle functions for graphics and animation
from freegames import square, vector  # Import square (to draw objects) and vector (for positions)

# Initialize the food's position
food = vector(0, 0)

# Initialize the "bad food" at a random position within the grid
bad_food = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)

# Snake's initial position
snake = [vector(10, 0)]

# Direction of movement 
aim = vector(0, -10)

# Obstacles that the snake must avoid in randomized positions (3 random obstacles)
obstacles = [vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10) for _ in range(3)]

def change(x, y): # To change the snake's direction of movement
    aim.x = x
    aim.y = y

def inside(position): # To check if a position is within the game boundaries
    return -200 < position.x < 190 and -200 < position.y < 190

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake or head in obstacles: # Check if the snake collides with the wall, itself, or obstacles
        square(head.x, head.y, 9, 'red') # Draw the head in red to indicate Game Over
        update()
        return

    snake.append(head) #Add new head position to the snake to make it "move" forward 

    if head == food:
        print('Snake length:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    elif head == bad_food: #If snake eats "bad" food 
        print('Ate bad food! Snake length:', len(snake))
        bad_food.x = randrange(-15, 15) * 10
        bad_food.y = randrange(-15, 15) * 10

        if len(snake) > 1: #Shorten the snake's length by one segment for bad food eaten
            snake.pop(0)
        else:
            square(head.x, head.y, 9, 'red') #If the snake only had one segment -> Game Over 
            update()
            return

    else:
        snake.pop(0) #Remove the tail to maintain constant length (if no food eaten)

    clear() #Clear the screen to erase the previous frame -> ensures smooth transitioning between frames

    for body in snake: #Draw the snake
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'blue') #Draw good food as blue square 
    square(bad_food.x, bad_food.y, 9, 'yellow') #Draw bad food as yellow square

    for obstacle in obstacles:
        square(obstacle.x, obstacle.y, 9, 'black') #Draw obstacles in black 

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

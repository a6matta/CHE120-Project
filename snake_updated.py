"""Snake, classic arcade game.
In the original game, the snake is moved across the game screen and needs to eat "food" while avoiding
hitting itself or the edges of the game screen limits. 

In our modified version, there will be randomly placed obstacles that the snake will need to AVOID, and
the game will end if the snake hits the obstacle, itself, or the game screen limits. There will also be the addition of "bad" food, that
will shorten the snake, along with the "good" food from the original version. 

Snake = green
Obstacles = black 
Good food = blue 
Bad food = orange

Currently the way the game is setup, it will generate one good food and one bad food at a random position on the grid, and they will remain 
stationary until the snake "eats" them, at which point they will relocate to a new random position and so on

Three randomly positioned obstacles will also be generated and remain stationary for the duration of the game 

Eating good food will grow the snake by one, eating bad food will shorten the snake by one, and colliding with itself, the obstacles, or the 
screen boundaries will end the game 

Things to consider:
- If we want the obstacles or food to be more dynamic and move around periodically -> will need to setup a way to randomly adjust their positions 
every few frames 
- Also I don't think we consider the condition of the obstacles/food/snake overlapping with each other? We might want to avoid that as well
"""
from random import randrange  # Import the randrange function for generating random positions
from turtle import *  # Import all turtle functions for graphics and animation
from freegames import square, vector  # Import square (to draw objects) and vector (for positions)

# Initialize the food's position
food = vector(0, 0)

# AH -> Initialize the "bad food" at a random position within the grid
bad_food = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)

# Snake's initial position
snake = [vector(10, 0)]

# Direction of movement 
aim = vector(0, -10)

# AH -> Obstacles that the snake must avoid in randomized positions (5 random obstacles)
obstacles = [vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10) for _ in range(5)]

def change(x, y): # To change the snake's direction of movement
    aim.x = x
    aim.y = y

def inside(position): # To check if a position is within the game boundaries
    return -200 < position.x < 190 and -200 < position.y < 190

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake or head in obstacles: #AM # Check if the snake collides with the wall, itself, or obstacles
        square(head.x, head.y, 9, 'red') # Draw the head in red to indicate Game Over
        update()
        return

    snake.append(head) #Add new head position to the snake to make it "move" forward 

    if head == food:
        print('Snake length:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    elif head == bad_food: #AH -> If snake eats "bad" food 
        print('Ate bad food! Snake length:', len(snake))
        bad_food.x = randrange(-15, 15) * 10
        bad_food.y = randrange(-15, 15) * 10
        snake.remove(snake[-1]) #AM: The length of the snake reduces by 1 each time a bad food is eaten
        #AM i think here we should add something to update the obstacles location
        #AM tried using obstacles.x and obstacles.y to randomize them but it wasnt working :(

        if len(snake) > 1: #AH -> Shorten the snake's length by one segment for bad food eaten 
            #AM this line was not working when I tested out the game so I added a line under the bad food if statement
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
    square(bad_food.x, bad_food.y, 9, 'orange') # AH -> Draw bad food as yellow square #AM changed the colour from yellow to orange (easier to see)

    for obstacle in obstacles:
        square(obstacle.x, obstacle.y, 9, 'black') # AH -> Draw obstacles in black 

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

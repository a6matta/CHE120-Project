#CHE 120 Project: Alisha Matta, Ashley Burton, Areeba Hasan, Gouri Sureshkumar

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

Currently the way the game is setup, it will generate one good food and one bad food at a random position on the grid, and the good food 
will remain stationary until the snake "eats" it, while the bad food is programmed to move every five seconds, at which point they will relocate 
to a new random position and so on

Five randomly positioned obstacles will also be generated and are programmed to move every five seconds with ontimer()

Eating good food will grow the snake by one, eating bad food will shorten the snake by one, and colliding with itself, the obstacles, or the 
screen boundaries will end the game 

Added Features:
- Gameplay border
- GAME OVER screen and printed final snake length
- Replay option with different levels of difficulty (different # of obstacles)
- Game Instructions

Further Potential Improvements: 
- Avoid good food/bad food/obstacle overlapping condition 
- Allow user to adjust time for bad food/obstacle movement 

NOTE: Any references or aids used in the creation of this code are cited in the slideshow presentation attached with the project submission  
"""
from random import randrange  # Import the randrange function for generating random positions
from turtle import *  # Import all turtle functions for graphics and animation
from freegames import square, vector  # Import square (to draw objects) and vector (for positions)

#Initialize the counters of eaten foods
good_count = 0
bad_count = 0

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
#Source: (Chaturvedi, 2021), (Stack Overflow user14372, 2014)

# GS -> To write messages on Game screen
pen = Turtle() 
pen.hideturtle()
pen.up() 
#Source: (The Python Software Foundation, 2024)

#AB -> To draw the game border
my_pen = Turtle()
my_pen.hideturtle()
my_pen.penup()

#AB -> To display the counters of eaten foods on the game screen
count_pen = Turtle()
count_pen.hideturtle()
count_pen.penup()

def change(x, y):  # To change the snake's direction of movement
    aim.x = x
    aim.y = y

def inside(position):  # To check if a position is within the game boundaries
    return -200 < position.x < 190 and -200 < position.y < 190

#def restart():  # AH -> Restart the game by resetting all variables and re-calling all functions
#    global food, bad_food, snake, aim, obstacles
#    food = vector(0, 0)  # Re-initialize all variables
#    bad_food = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
#    snake = [vector(10, 0)]
#    aim = vector(0, -10)
#    obstacles = [vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10) for _ in range(5)]
#    pen.clear()  # Clear the "Game Over" screen 
#    clear() 
#    move()  # Recall all necessary functions to start the game 
#    move_obstacles()
#    move_bad_food()

#AM -> Restart the game to easy difficulty. THe number of obstacles is reset to 3
def restart_easy():  # AH -> Restart the game by resetting all variables and re-calling all functions
    global food, bad_food, snake, aim, obstacles, good_count, bad_count #Global variables to change to global scope as variables need to be used across functions
    food = vector(0, 0)  # Re-initialize all variables
    bad_food = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    obstacles = [vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10) for _ in range(3)]
    pen.clear()  # Clear the "Game Over" screen
    clear() 
    move()  # Recall all necessary functions to start the game 
    move_obstacles()
    move_bad_food()
    good_count = 0 #AB -> resets the counters when the game restarts
    bad_count = 0
    eat_count(good_count,bad_count) #AB -> calls the function to display the restet counter 

#AM -> Restart the game to medium difficulty. The number of obstacles is reset to 6.
def restart_med():  
    global food, bad_food, snake, aim, obstacles, good_count, bad_count
    food = vector(0, 0)
    bad_food = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    obstacles = [vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10) for _ in range(6)]
    pen.clear() 
    clear() 
    move()
    move_obstacles()
    move_bad_food()
    good_count = 0
    bad_count = 0
    eat_count(good_count,bad_count)

#AM -> Restart the game to hard difficulty. The number of obstacles is reset to 9.
def restart_hard():  
    global food, bad_food, snake, aim, obstacles, good_count, bad_count
    food = vector(0, 0) 
    bad_food = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    obstacles = [vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10) for _ in range(9)]
    pen.clear() 
    clear() 
    move()
    move_obstacles()
    move_bad_food()
    good_count = 0
    bad_count = 0
    eat_count(good_count,bad_count)

#AM -> Print out the game instructions.
def game_instructions():
    pen.clear()
    clear()
    pen.goto(0, 140) 
    pen.color("black")  
    pen.write("Game Instructions:", align="center", font=("Arial", 14, "italic"))
    pen.goto(0, 115)  
    pen.write("Use the arrow keys to move your snake.", align="center", font=("Arial", 12, "italic"))
    pen.goto(0,100)
    pen.write("Grow your snake to gain points.", align="center", font=("Arial", 12, "italic"))
    pen.goto(0,85)
    pen.write("Don't hit the walls or obstacles!", align="center", font=("Arial", 12, "italic"))
    pen.goto(0, 50) 
    pen.color("green")  
    pen.write("green --> your snake", align="center", font=("Arial", 12, "italic"))
    pen.goto(0, 25) 
    pen.color("blue")  
    pen.write("blue --> good food that makes your snake grow!", align="center", font=("Arial", 12, "italic"))
    pen.goto(0, 0) 
    pen.color("orange")  
    pen.write("orange --> bad food that makes your snake shrink!", align="center", font=("Arial", 12, "italic"))
    pen.goto(0, -25) 
    pen.color("black")  
    pen.write("black --> hitting an obstacle makes you lose the game!", align="center", font=("Arial", 12, "italic"))
    pen.goto(0, -60) 
    pen.write("To play again:", align="center", font=("Arial", 12, "italic")) 
    pen.goto(0, -80) 
    pen.write("Press 'E' for easy difficulty", align="center", font=("Arial", 10, "italic"))
    pen.goto(0, -100) 
    pen.write("Press 'M' for medium difficulty", align="center", font=("Arial", 10, "italic"))
    pen.goto(0, -120) 
    pen.write("Press 'H' for hard difficulty", align="center", font=("Arial", 10, "italic"))
    pen.goto(0, -140)
    pen.write("Press 'I' for game instructions", align="center", font=("Arial", 10, "italic"))
    #Source: (The Python Software Foundation, 2024)

def move():  # Move the snake forward
    if len(snake) == 0:  # AH -> If the snake is of length 0, end the game
        pen.clear()  # GS Write Game Over
        pen.color("red")
        pen.goto(0, 0)
        pen.write("Game Over", align="center", font=("Arial", 20, "bold"))
        pen.goto(0, -30)  # AH -> Move pen below the "Game Over" message
        pen.write("Final Length: " + str(len(snake)), align="center", font=("Arial", 14, "normal"))  # AH -> Print final snake length
        pen.goto(0, -60)  # Move below both messages
        pen.color("black") 
        pen.write("To restart game:", align="center", font=("Arial", 12, "italic")) # AH -> Add a restart message
        pen.goto(0, -80) #AM -> when the game ends, allow the player to play again and select their difficulty.
        pen.write("Press 'E' for easy difficulty", align="center", font=("Arial", 10, "italic"))
        pen.goto(0, -100) 
        pen.write("Press 'M' for medium difficulty", align="center", font=("Arial", 10, "italic"))
        pen.goto(0, -120) 
        pen.write("Press 'H' for hard difficulty", align="center", font=("Arial", 10, "italic"))
        pen.goto(0, -140)
        pen.write("Press 'I' for game instructions", align="center", font=("Arial", 10, "italic"))
        #pen.write("Press 'R' to restart the game", align="center", font=("Arial", 12, "italic"))
        update()
        return

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake or head in obstacles:  # AM # Check if the snake collides with the wall, itself, or obstacles
        square(head.x, head.y, 9, 'red')  # Draw the head in red to indicate Game Over
        update()
        pen.clear() 
        pen.color("red")
        pen.goto(0, 0) 
        pen.write("Game Over", align="center", font=("Arial", 20, "bold")) #Write Game Over
        pen.goto(0, -30)  
        pen.write("Final Length: " + str(len(snake)), align="center", font=("Arial", 14, "normal")) 
        pen.goto(0, -60) 
        pen.color("black") #AM -> when the game ends, allow the player to play again and choose their difficulty. 
        pen.write("To restart game:", align="center", font=("Arial", 12, "italic"))
        pen.goto(0, -80) 
        pen.write("Press 'E' for easy difficulty", align="center", font=("Arial", 10, "italic"))
        pen.goto(0, -100) 
        pen.write("Press 'M' for medium difficulty", align="center", font=("Arial", 10, "italic"))
        pen.goto(0, -120) 
        pen.write("Press 'H' for hard difficulty", align="center", font=("Arial", 10, "italic"))
        pen.goto(0, -140)
        pen.write("Press 'I' for game instructions", align="center", font=("Arial", 10, "italic"))
        return

    snake.append(head)  # Add new head position to the snake to make it "move" forward 

    if head == food:  # If snake eats good food, grows one segment
        print('Ate good food! Snake length:', len(snake)) #Print snake length if good food eaten 
        food.x = randrange(-15, 15) * 10  # Once eaten, food position is randomized to new spot on grid 
        food.y = randrange(-15, 15) * 10
        eat_count(1, 0)#AB --> Update the bad food counter when bad food eaten

    elif head == bad_food:  # AH -> If snake eats "bad" food
        bad_food.x = randrange(-15, 15) * 10  # Once eaten, bad food position is randomized to new spot on grid 
        bad_food.y = randrange(-15, 15) * 10
        if len(snake) > 1:  # AH -> If the snake's length is greater than one, reduce length by one segment
            snake.remove(snake[-1])  # AM # Reduce the snake's length by one segment
            snake.pop(0) #AH -> To ensure snake shrinks 
            print('Ate bad food! Snake length:', len(snake)) #AH -> Print snake length if bad food eaten 
            eat_count(0, 1)#AB --> Update the bad food counter when bad food eaten
        else:  # AH -> If the snake is too short (segment can't be removed), the game ends
            square(head.x, head.y, 9, 'red')  # Draw head in red to indicate Game Over
            update()
            return
    else:
        snake.pop(0)  # Remove the tail to maintain constant length (if no food eaten)

    clear()  # Clear the screen to erase the previous frame -> ensures smooth transitioning between frames

    for body in snake:  # Draw the snake
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'blue')  # Draw good food as blue square 
    square(bad_food.x, bad_food.y, 9, 'orange')  # AH -> Draw bad food as orange square
    # AM changed the colour from yellow to orange (easier to see)

    for obstacle in obstacles:
        square(obstacle.x, obstacle.y, 9, 'black')  # AH -> Draw obstacles in black

    update()  # Refreshes game to display changes and update to current frame
    ontimer(move, 100)  # Schedule for move function after 100 milliseconds -> creating loop for continuous movement
    # Keep game running

def move_obstacles():  # AH -> Randomly move obstacles to new positions after certain time
    for obstacle in obstacles:
        obstacle.x = randrange(-15, 15) * 10  # AH -> Assign new random grid position for obstacles
        obstacle.y = randrange(-15, 15) * 10
    ontimer(move_obstacles, 6000)  # AH -> Schedule obstacle movement every 6 seconds

def move_bad_food():  # AH -> Randomly move bad food to new positions after certain time
    bad_food.x = randrange(-15, 15) * 10  # AH -> Move bad food to new random grid position
    bad_food.y = randrange(-15, 15) * 10
    ontimer(move_bad_food, 6000)  # AH -> Schedule bad food movement every 6 seconds

def window_border():#AB -> oulines the playable area of the game
    my_pen.setposition(-200,200)
    my_pen.pendown()
    for top in range(4):
        my_pen.forward(400)
        my_pen.right(90)
    #AB -> writing the food counter titles 
    my_pen.up()
    my_pen.goto(-195, 205)
    my_pen.write('Good: ', font=("Arial", 10, "normal")) #Source: Reddit
    my_pen.up()
    my_pen.goto(145,205)
    my_pen.write('Bad: ',font=("Arial", 10, "normal")) #Source: Reddit
    #Source: (The Python Software Foundation, 2024)

def eat_count(good, bad):#AB -> keeps track of and then displays the number of eaten food
    global good_count, bad_count #AB -> defines the required variables in the global scope
    good_count += good # AB -> increaes the good food counter by 1 everytime a good food is eaten)
    bad_count += bad # AB -> increaes the bad food counter by 1 everytime a bad food is eaten)
    count_pen.clear() # AB -> removes the old counts
    count_pen.goto(-155, 205)
    count_pen.write(f'{good_count}', font=("Arial", 10, "normal")) #Source: Reddit
    count_pen.goto(175,205)
    count_pen.write(f'{bad_count}',font=("Arial", 10, "normal")) #Source: Reddit
    #Source: (The Python Software Foundation, 2024)

# Game setup
setup(420, 450, 370, 0)  # Setup game window size
window_border() # Creating a border around the playable area
eat_count(good_count, bad_count) # displays the initial counters for the foods
hideturtle()  # Hide turtle cursor 
tracer(False)  # Disable automatic screen updates 
listen()  # Enable keyboard inputs 
onkey(lambda: change(10, 0), 'Right')  # Right arrow key changes snake direction to the right
onkey(lambda: change(-10, 0), 'Left')  # Left arrow key changes snake direction to the left
onkey(lambda: change(0, 10), 'Up')  # Up arrow key changes snake direction up
onkey(lambda: change(0, -10), 'Down')  # Down arrow key changes snake direction down
onkey(restart_easy, 'e')  # AH -> Press letter keys to restart game 
onkey(restart_med, 'm')  #AM -> Press the letter key associated with each difficulty
onkey(restart_hard, 'h')
onkey(game_instructions, 'i') #AM -> Press the letter key "i" to see game instructions
#Source: (GeeksforGeeks, 2020)

# To start game:
move()  # Start the game and the snake's movement
move_obstacles()  # AH -> Start obstacle movement
move_bad_food()  # AH -> Start bad food movement 
done()  # Keeps game window open until user closes it or game is completed

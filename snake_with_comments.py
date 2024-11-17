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

def inside(head): #AM -> This function checks if the snake is within the game boundaries.
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
    #AM -> The game boundaries are from -200 to 190 on the x-axis (horizontal length of the game board) and y-axis (vertical length of the game board).
    #AM -> This function checks if the position of the head is within the horizontal constraints and vertical constraints.
    #AM -> The code uses the "and" operator, so it needs both conditions to be True for the function to return True.
    #AM -> If the snake head is within the boundaries (horizontal and vertical constraints) then the function returns True which is used later in the code.
    #AM -> Since the "and" operator is used, if one (or both) of these conditions are False, the function will return False.
    #AM -> If the snake head is not within the horizontal or vertical boundary (or both), the function returns False which is used later in the code.

def move(): #AM -> This function is used to assign the head to the snake body and move the head depending on the arrow key pressed.
    """Move snake forward one segment."""
    head = snake[-1].copy()
    #AM -> The head of the snake is assigned the front of the snake body
    #AM -> [-1] is used to select the last object in the snake list. This is useful because the last object can be selected no matter how many times the snake list is appended (the snake body grows).
    #AM -> Each time the snake list is updated (the body grows), the head variable is reassigned to the last object (the position of the block that was just eaten).
    #AM -> .copy() makes a copy of the last object in the list so that it is assigned to the head variable.
    head.move(aim)
    #AM -> When an arrow key is pressed, the "aim" vector will update.
    #AM -> The head will move left/right/up/down depending on the player input (the arrow key pressed).

    if not inside(head) or head in snake: #AM -> This "if" statement checks if the player has lost the game.
        #AM -> The "or" operator is used, so only one condition needs to be True for the function to return True.
        #AM -> The code uses the inside(head) function to see if the player has gone out of the game boundaries
        #AM -> If the player has gone out of the game boundaries, inside(head) would be False. The "not" operator would switch this to True
        #AM -> head in snake checks if the position of the snake head is the same as the position of a part of the snake body (if the snake ran into itself).
        #AM -> If the value for "head" is part of the list for "snake", then head in snake would be True.
        #AM -> If one of the above conditions are True, the "if" statement code will run and end the game.
        square(head.x, head.y, 9, 'red')
        #AM -> This line of code will change the colour of the square where the snake's head is.
        #AM -> The position of the head is found according to head.x (the horizontal position) and head.y (the vertical position). The 9 represents the size of the square (9x9)
        #AM -> 'red' changes the colour of this 9x9 square to red.
        update()
        #AM -> When changes are made to the game, this line displays these updates to the user. For example, when the player loses, the head will change to red and update() will make this visible in the GUI.
        return
#-----------------------------------------------------------------------------------
    #AH 
    snake.append(head)  #AH -> #.append attaches an element to the end of a list so:
    # this adds the new head position to the end of the snake list, which grows the snake by one segment. 
    #Since the last element of the list is the head, the new position of the snake's head is added to the end, and this
    #represents the snake moving forward (since the list reflects the snake's body from head to tail - the consistent updatng
    #of head position makes the snake appear to be moving forward as required in game play) 
    
    #AH -> # This section is to check if snake "eats" the food and then update the game accordingly 
    if head == food: #AH -> The condition if head == food, is to check if the snake's head position matches the food position (meaning it can "eat" the food)
        print('Snake:', len(snake)) #AH -> #Print 'Snake' and length of snake
        #AH -> If the if head == food condition is true and the snake can eat the food, the program will print the string 'Snake' and the current length of the snake
     
        #AH -> Then, the following section updates the food position to a new random location on the grid: 
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        #AH -> The above is accomplished by assigning random x and y coordinate values to the "food" using randrange()
        #randrange(start,stop,step) generates random numbers from a specified range, the range specified will generate a random integer between -15 and 14 (stop is exlcusive) that will 
        #represent possible positions in terms of the game grid (the x10 is potentially to scale the grid positions to actual coordinates for the food to be placed?)
        #The above ensures that the food will appear somwhere else on the screen for the snake to chase and the game play to continue
  
    else: #AH -> If head != food, and the above condition evaluates to false indicating that the snake did not "eat" the food, the else condition is valid:
        snake.pop(0) #AH -> .pop removes the element of a list at the specified position 
        #AH -> Since the snake list goes from tail end to head end, the 0th index is the tail so snake.pop(0) removes the first element, the tail, from the snake list 
        #AH -> This ensures that the snake's length remains constant (since a new head position is always appended to make the snake "move" forward, if food is not eaten, 
        #the tail must be removed to ensure that the snake doesn't get longer based on the added "heads" (since in the game of snake, the snake only gets longer when food is eaten) 
#AH -> Therefore the above if statement ensures that the game play follows by growing the snake by one segment everytime food is eaten, and maintaining snake length if not 
  
    #AH -> From import turtle, clear() erases the entire canvas (clears what is displayed on screen but does not reset other properties)
    clear() #AH -> The clear function erases the previous game frame to update to the new one (i.e. the new snake/food positions to ensure seamless transitions between frames) 

    #AH -> #The for loop iterates over each segment in the snake list: 
    for body in snake:
    #AH -> from freegames import square above, so square() from the freegames library -> "Draws square at (x, y) with side length size and fill color name. The square is oriented so the bottom left corner is at (x, y)"
        square(body.x, body.y, 9, 'black')
    #AH-> The line above is responsible for drawing the snake and updating the game screen
    #AH -> The body represents one segment of the snake and is stored as a vector object which contains (x,y) coordinates
    #-> This section of code draws a 9x9 (size) black (colour) square, where body.x and body.y specify the position on screen

    #Therefore each body segment of the snake is drawn as a black square and the food appears as a green sqaure for easy differentiation, representing both the snake, its movement, and the food's location 
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

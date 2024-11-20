#AB: Ashley Burton
#AM: Alisha Matta
#AH: Areeba Hasan
#GS: Gouri Sureshkumar

from random import randrange
#AB -> The method, randrange, imported from the built-in module, random, will allow for the generation of a random number within a (start, stop) set of parameters 
#AB -> Since randrange is the only method required from the random module, it's best to make use of the 'from' keyword so the entire module isn't imported and excessive memory isn't taken up
from turtle import *
#AB -> The turtle method provides the user with a "virtual canvas" as well as an onscreen pen
#AB -> The entire turtle module contents are brought into the namespace so that the following methods can be easily called without typing "turtle.methodName": 
#AB -> update(), clear(), ontimer(), setup(), hideturtle(), tracer(), listen(), and onkey()
#AB -> In the context of the game, Snake, turtle is responsible for the gameplay visuals, including the food and snake itself

from freegames import square, vector
#AB -> The built-in module, freegames, is a collection of free Python games that includes a few methods like square and vector
#AB -> The other methods included with the freegames module weren't needed so the 'from' keyword was used to minimize memory use
#AB -> The square method draws a square from a given point, makes it a specific size, and then colours it (x, y, size, colour). In the game, it is used to create the snake and food 
#AB -> The vector method creates a two-dimensional vector to the location (x,y). In the game, it's used to store the (x,y) coordinates of the snake, food, and direction of the snake

food = vector(0, 0)
#AB -> This assignment is to initialize the food variable as an (x,y) location kept as a vector
#AB -> Initializing the food variable allows for the x and y coordinates to be modified separately while still being associated with the same variable
snake = [vector(10, 0)]
#AB -> This assignment is to initialize the snake variable as an extendable list so that it may grow, have a head, and have a direction to move
#AB -> The snake list is initialized at the vector location (10, 0) so that it can move in any direction

aim = vector(0, -10)
#AB -> This assignment initializes the aim variable as a vector to act as a modifier of the snake's direction in the gameplay
#AB -> It's initialized as a downward movement, but by separately modifying the x and y variables, the snake can be oriented to move left or right and up or down

#AB -> By calling this function, the snake's movement is being modified in the x or y direction
def change(x, y): #AB -> The function is passed one of four arguments depending on the which direction key is pressed
    """Change snake direction."""
    aim.x = x
    aim.y = y
    #AB -> The arguments that the function is called with will be assigned to the corresponding vector coordinates of the aim variable
    #AB -> These variables can either be changed to 0, 10, or -10, but if one variable is not equal to zero, the other must be zero so that the snake only changes one direction at a time
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
    #GS -> Draws a square with the parameters in the bracket: food.x and food.y representing the x & y coordinates of where the square should be, 9 being the size, and green the colour of the square
    update()
    #GS -> function for when changes are made, it will be updated for the player
    ontimer(move, 100)
    #GS -> function is used to create a loop, it will call the move function after 100 seconds so the game is updated 


setup(420, 420, 370, 0)
#GS -> Sets up the parameters of the game screen: 420, 420 is the width and height of the screen and 370,0 is the position of the game screen on the user's screen (370 from left and 0 from top)
hideturtle()
#GS -> hides the cursor on the game screen for less cluttering and distraction for user
tracer(False)
#GS -> disables automatic screen updates: without this function, the game can appear laggy,this function will ensure that all changes to objects(snake,food etc.) are made then the screen is updated for user as opposed to the screen being updated each time for each object
listen()
#GS -> enables the keyboard to be used to communicate to the game otherwise game won't respond to keys being pressed
onkey(lambda: change(10, 0), 'Right')
#GS ->  this function assigns the right arrow key to call the change function: 10,0 represent the horizontal and vertical movement: 10 units right and 0 movement vertically
onkey(lambda: change(-10, 0), 'Left')
#GS -> this function assigns the left arrow key to call the change function: -10,0 represent the horizontal and vertical movement: 10 units left and 0 movement vertically
onkey(lambda: change(0, 10), 'Up')
#GS ->this function assigns the up arrow key to call the change function: 0,10 represent the horizontal and vertical movement: 0 movement horizontally and 10 units up
onkey(lambda: change(0, -10), 'Down')
#GS ->this function assigns the down arrow key to call the change function: 0,-10 represent the horizontal and vertical movement: 0 movement horizontally and 10 units down
move()
#GS ->Starts the game: everything is set up and the movement of the snake can begin: without this the game wouldn't run there would be a frozen screen
done()
#GS ->Makes sure the game screen will stay open until user closes it on their end after the game has completed.

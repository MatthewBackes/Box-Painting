# Class: CS4500 Software Profession
# Student: Matt Backes
# Date: 10/1/2019

# This program will use the Python feature Turtle to draw a grid, paint the individual squares at random until every
# single one has been painted, and continue to do so until the number of paintings required is completed.

# The first thing our program will do is prompt the user to input the size of the grid which will be N x N size,
# with N being no less than 2 and no greater than 15. A simple while loop will make sure the number is appropriate,
# and a try block will ensure that the user input is an integer value. The same will be done for the number of
# paintings, but the number will be between 1 and 10.  We will use a for loop # that will iterate "paintingsCount"
# number of times, each time making a multi-dimensional list "timesPainted" to keep track of # which spaces have been
# painted and which have not. A while loop is used to control our painting process, and will stop once a False value
# is applied to the "continuePaint" variable, which will only happen if no 0's are found in "timesPainted". It will
# then print to the Turtle interface a message to let the user know they have to hit enter to continue. After all the
# paintings are finished, various stats about the paint process are printed to screen, and the program will end.

import turtle  # Allows access to Turtle
import random  # Allows access to random number generator


# The function drawGrid will draw a grid whenever it is called. By using the x and y variables in the for loop,
# the loop will begin by lifting up the pen, setting it to a new position and then placing it back down, before using
# another for loop to actually draw the square. The variable gridArea makes sure the distance moved by the forward
# and set position command are consistent, so there is no empty space in between each square.
def drawGrid():
    for x in range(gridSize):
        for y in range(gridSize):
            turtle.up()
            turtle.setposition(x * gridArea, y * gridArea)
            turtle.down()

            for i in range(4):
                turtle.forward(gridArea)
                turtle.right(90)


# The paintBox function will act in a similar way to the drawGrid function, but will instead use .fillcolor() in
# order to color the squares. Before the color is placed, a dot will be left to indicate that square will be painted
# next, and the dot will be covered after the paint is applied so there can only be one visible at a time.
def paintBox(x, y):
    turtle.up()
    turtle.setposition((x * gridArea) + 10, (y * gridArea) - 10)
    turtle.dot()
    turtle.down()
    color = random.choice(colors)
    turtle.up()
    turtle.setposition(x * gridArea, y * gridArea)
    turtle.down()
    turtle.color("black", color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(gridArea)
        turtle.right(90)
    turtle.end_fill()


# This function will check if a 0 is present in a list. If there isn't, it will return false. This will be used to
# end the paint loop when every square has been painted at least once.
def stopPaint(timesPaint):
    for x in range(gridSize):
        for y in range(gridSize):
            if timesPaint[x][y] == 0:
                return True
    return False


# Function to check for the maximum value of a list.
def maxOfArray(array, size):
    maxValue = array[0]
    for x in range(size):
        if array[x] > maxValue:
            maxValue = array[x]
    return maxValue


# Function to check for the minimum value of a list.
def minOfArray(array, size):
    minValue = array[0]
    for x in range(size):
        if array[x] < minValue:
            minValue = array[x]
    return minValue


colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]  # Multiple colors make the painting look nice
gridSize = 0  # Initializing the variable gridSize and paintingCount here will prevent an error while
paintingCount = 0  # attempting to enter a while loop if the user input something that isn't a number
gridArea = 20  # Number to show how big each square should be

# The following stretch of code will gain values for the size of the grid size and the number of paintings made. Try
# and catch exceptions will control for non-int variables and while loops will make sure the values are what we want
# them to be.
try:
    a = "asf"
    b = "ad"
    print('%s %s' % (a, b))
    gridSize = int(input("Enter a number between 2 and 15 to determine grid size."))  # Prompts user for grid size
except ValueError:
    pass

while gridSize < 2 or gridSize > 15:
    try:
        gridSize = int(input("Input is either not a number, less than 2 or greater than 15. Please try again."))
    except ValueError:
        pass
try:
    paintingCount = int(input("Enter a number between 1 and 10 to determine how many paintings will be made."))
except ValueError:
    pass
while paintingCount < 1 or paintingCount > 10:
    try:
        paintingCount = int(input("Input is either not a number, less than 1 or greater than 10. Please try again."))
    except ValueError:
        pass

turtle = turtle.Turtle()  # Initialize turtle
arrayOfArrays = []  # This will eventually become a three dimensional array that will contain the number of paint
# blots used on every single grid space across all paintings.

for paintNum in range(paintingCount):
    continuePaint = True  # Variable that is used to control the paint loop
    turtle.hideturtle()  # Hides the turtle icon to make the drawing process look nicer
    turtle.speed(10)
    timesPainted = [[0 for x in range(gridSize)] for x in range(gridSize)]  # List to contained how many times a box
    # has been painted
    drawGrid()
    while continuePaint:
        randomNum1 = random.randrange(gridSize)  # Two random numbers to determine which square will be painted
        randomNum2 = random.randrange(gridSize)  #
        paintBox(randomNum1, randomNum2)
        timesPainted[randomNum1][randomNum2] += 1
        continuePaint = stopPaint(timesPainted)
    turtle.up()
    turtle.setposition(-350, 0)
    turtle.down
    turtle.write("Press ENTER to continue.")
    input("Press ENTER to continue.")  # Stops the program until user hits enter.
    turtle.undo()
    arrayOfArrays.append(timesPainted)
    turtle.reset()  # Resets the turtle for the next painting.

mostBlob = [0 for x in range(paintingCount)]  # Keep track of the most blobs on a single space per painting.
numberOfBlobs = [0 for x in range(paintingCount)]  # Keeps track of the total number of blobs on each painting.

# This loop will go through the entire three dimensional array which contains all the information about the number of
# blobs on each space.
for a in range(paintingCount):
    for x in range(gridSize):
        for y in range(gridSize):
            numberOfBlobs[a] += arrayOfArrays[a][x][y]
            if mostBlob[a] < arrayOfArrays[a][x][y]:
                mostBlob[a] = arrayOfArrays[a][x][y]

# The following code will print out various information about the stats gathered from our paint process.
print("The minimum number of paint blots needed to paint a picture: " + str(
    minOfArray(numberOfBlobs, paintingCount)) + "\n")
print("The average number of paint blots needed to paint a picture: " + str(sum(numberOfBlobs) / paintingCount) + "\n")
print("The maximum number of paint blots needed to paint a picture: " + str(
    maxOfArray(numberOfBlobs, paintingCount)) + "\n")

print("The minimum number of the most paint blots on a single spot: " + str(minOfArray(mostBlob, paintingCount)) + "\n")
print("The average number of the most paint blots on a single spot: " + str(sum(mostBlob) / paintingCount) + "\n")
print("The maximum number of the most paint blots on a single spot: " + str(maxOfArray(mostBlob, paintingCount)) + "\n")

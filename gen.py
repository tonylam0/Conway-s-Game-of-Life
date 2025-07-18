import random
import math

WIDTH, HEIGHT = 1000, 800  # size of the pygame window
RESOLUTION = 20  # this constant represents the size of the cells within the grid
grid = []
columns, rows = 0, 0  # placeholder values

mousePos = (0, 0)  # placeholder values for x and y position of mouse click
switchSignal = False  # this signals the update function to create/destroy a cell

# creates a 2D array which will represent the grid
def make2DArray():
    global columns
    global rows
    global grid

    columns = round(WIDTH / RESOLUTION)
    rows = round(HEIGHT / RESOLUTION)

    for i in range(columns):
        grid.append([])
        for j in range(rows):  # makes all the border cells dead to prevent bugs
            if i == 0 or i == columns - 1 or j == 0 or j == rows - 1:
                grid[i].append(0)
            else:
                # randomly assigns a state to each cell in the grid
                # the multiplier determines the amount of live cells there are -> higher chance of 1's
                grid[i].append(math.floor(random.random() * 1.1))

# counts the amount of alive cells from the 8 surrounding cells of an individual cell
def countNeighbors(cellColumn, cellRow, currentState): 
    count = 0

    count += grid[cellColumn - 1][cellRow - 1] + grid[cellColumn - 1][cellRow] + grid[cellColumn - 1][cellRow + 1]
    count += grid[cellColumn][cellRow - 1] + grid[cellColumn][cellRow + 1]
    count += grid[cellColumn + 1][cellRow - 1] + grid[cellColumn + 1][cellRow] + grid[cellColumn + 1][cellRow + 1]

    if currentState == 0 and count == 3:
        currentState = 1
    elif currentState == 1 and (count < 2 or count > 3):
        currentState = 0

    return currentState

# updates the state of individual cells based on its surrounding cells
def updateState():
    global grid
    global createSignal

    for i in range(1, columns - 1):  # the altered range is to prevent calculation on border cells
        for j in range(1, rows - 1):
            grid[i][j] = countNeighbors(i, j, grid[i][j])
    
'''Grid of Cells with Jared
Peter Farrell
Sept. 19, 2017'''

from random import choice

width_of_grid = 101

sz = 600//width_of_grid + 1

class Grid:
    #how to fill the grid randomly
    def __init__(self):
        self.cellList = []
        for i in range(width_of_grid):
            self.cellList.append([])
            for j in range(width_of_grid):
                self.cellList[i].append(choice([0,1]))
                                   
    def update(self,level):
        for y,row in enumerate(self.cellList):
            for x,cell in enumerate(row):
                if cell == 1:
                    fill((3*level)%255,255,255,100) #white
                else:
                    fill(0) #black
                rect(sz*x,sz*y,sz,sz)
                
    def checkNeighbors(self,row,col):
        self.neighbors = 0
        if row > 0: #not in top row
            if col > 0: #not on left edge
                #check the cell above and to the left
                if self.cellList[row-1][col-1]==1:
                    self.neighbors += 1
            #check the cell above
            if self.cellList[row-1][col]==1:
                self.neighbors += 1
            #if the cell isn't on the right edge:
            if col < width_of_grid - 1:
                #check the cell above and to the right
                if self.cellList[row-1][col+1]==1:
                    self.neighbors += 1
        #check the cell to the left
        if col > 0:
            if self.cellList[row][col-1]==1:
                self.neighbors += 1
        #check the cell to the right
        if col < width_of_grid - 1:
            if self.cellList[row][col+1]==1:
                self.neighbors += 1
        if row < width_of_grid - 1: #not in bottom row
            if col > 0: #not on left edge
                #check the cell below and to the left
                if self.cellList[row+1][col-1]==1:
                    self.neighbors += 1
            #check the cell below
            if self.cellList[row+1][col]==1:
                self.neighbors += 1
            if col < width_of_grid - 1:
                #check the cell below and to the right
                if self.cellList[row+1][col+1]==1:
                    self.neighbors += 1
        return self.neighbors
    
    def generateNewLevel(self):
        #create an empty list called "newGrid"
        newGrid = []
        #for every row in range "width of grid"
        for row in range(width_of_grid):
        #add an empty list to newGrid
            newGrid.append([])
            #for every column in range "width_of_grid"
            for col in range(width_of_grid):
                #the number of neighbors is what's returned
                #by the checkNeighbors method
                nbs = self.checkNeighbors(row,col)
                #if that row and column's entry 
                #in cellList is alive
                if self.cellList[row][col] == 1:
                    #if it has two or three neighbors
                    if nbs in [2,3]:
                        #append a 1 to newGrid
                        newGrid[row].append(1)
                    #otherwise:
                    else:
                        #append a 0 to newGrid
                        newGrid[row].append(0)
                #otherwise: (if the cell is dead)
                else:
                    #if the number of neighbors is 3:
                    if nbs == 3:
                        #put a 1 in that row in newGrid
                        newGrid[row].append(1)
                    #otherwise:
                    else:
                        #put a 0 in that row in newGrid
                        newGrid[row].append(0)
        #give cellList all the items in the newGrid list!                
        self.cellList = newGrid

def setup():
    global grid, level
    noStroke()
    colorMode(HSB)
    size(600,600)
    grid = Grid()
    level = 0
    
def draw():
    global grid,level
    grid.generateNewLevel()
    grid.update(level)
    level += 1
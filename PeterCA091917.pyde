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
                                   
    def update(self):
        for y,row in enumerate(self.cellList):
            for x,cell in enumerate(row):
                if cell == 1:
                    fill(255) #white
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
        newGrid = []
        for row in range(width_of_grid):
            newGrid.append([])
            for col in range(width_of_grid):
                neighbors = self.checkNeighbors(row,col)
                if self.cellList[row][col]==1:
                    if neighbors in [2,3]:
                        newGrid[row].append(1)
                    else: 
                        newGrid[row].append(0)
                else: #cell is dead
                    if neighbors == 3:
                        newGrid[row].append(1)
                    else:
                        newGrid[row].append(0)
        self.cellList = newGrid[::]

def setup():
    global grid, level
    size(600,600)
    grid = Grid()
    level = 0
    
def draw():
    global grid,level
    grid.generateNewLevel()
    grid.update()
    level += 1
    
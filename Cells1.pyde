from random import choice

width_of_grid = 101
height_of_grid = 101

#size of cell
sz = 600//width_of_grid + 1 #if 600 is the width of the screen

class Cell:
    def __init__(self,c,r,on):
        self.c = c
        self.r = r
        self.on = on #starts False or "off"
        
    def checkNeighbors(self):
        global cellList
        neighbs = 0 #running sum of "on" neighbors
        if self.r > 0:
            if cellList[self.r-1][self.c].on == 1:
                neighbs += 1

        if self.r < len(cellList)-1:
            if cellList[self.r+1][self.c].on == 1:
                neighbs += 1

        if self.c > 0:
            if cellList[self.r][self.c-1].on == 1:
                neighbs += 1
        if self.c < len(cellList[0])-1:
            if cellList[self.r][self.c+1].on == 1:
                neighbs += 1

        if neighbs in [1,4]:
            return 1
        else:
            return 0
        
    def update(self):
        if self.on == 1:
            fill(255,0,0)
        else:
            fill(0)
        rect(sz*self.c,sz*self.r,sz,sz)

def createCellList():
    global cellList,level
    cellList = [] #empty list for cells 
    
    #populate the first cell list
    for j in range(height_of_grid):
        cellList.append([]) #add empty row
        for i in range(width_of_grid):
            cellList[j].append(Cell(i,j,0)) #add zeroes
    #center cell is set to 1
    cellList[height_of_grid//2][width_of_grid//2].on = 1
        #for i in range(width_of_grid):
            #cellList[j].append(Cell(sz*i,sz*j,choice([0,1])))
    
    level = 0
    return cellList

def setup():
    global cellList
    size(600,600)
    noStroke()
    cellList = createCellList()
    
def draw():
    global cellList,level
    frameRate(20)
    background(0)
    
    #draw the grid from the cell list
    for row in cellList:
         for cell in row:
             cell.update()
    newList = [] #create a new list for the next gen
    for r,row in enumerate(cellList):
        newList.append([]) #add empty row
        for c,cell in enumerate(row):
            if cell.on == 0: #if cell is off
                 #check neighbs and append new value
                newList[r].append(Cell(c,r,cell.checkNeighbors()))
            else: #on cells stay on
                newList[r].append(Cell(c,r,1))
    cellList = newList[::]
    level += 1
    if level == 48:
        cellList = createCellList() # noLoop()
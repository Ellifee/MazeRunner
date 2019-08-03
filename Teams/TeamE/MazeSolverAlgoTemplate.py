
"""
This class is the template class for the Maze solver
"""

import sys
from math import sqrt
import numpy
import queue

class MazeSolverAlgoTemplate:

    EMPTY = 0       # empty cell
    OBSTACLE = 1    # cell with obstacle / blocked cell
    START = 2       # the start position of the maze (red color)
    TARGET = 3      # the target/end position of the maze (green color)

    def __init__(self):
        # TODO: this is you job now :-)
        self.dimCols = 0
        self.dimRows = 0
        self.setStartCol = 0
        self.setStartRow = 0
        self.setEndCol = 0
        self.setEndRow = 0
        self.grid = [[]]

    # Setter method for the maze dimension of the rows
    def setDimRows(self, rows):
        self.setDimRows = rows

    # Setter method for the maze dimension of the columns
    def setDimCols(self, cols):
        self.setDimCols = cols
        
    # Setter method for the column of the start position 
    def setStartCol(self, col):
        self.setStartCol = col

    # Setter method for the row of the start position 
    def setStartRow(self, row):
        self.setStartRow = col

    # Setter method for the column of the end position 
    def setEndCol(self, col):
        self.setEndCol = col

    # Setter method for the row of the end position 
    def setEndRow(self, row):
        self.setEndRow = row

    # Setter method for blocked grid elements
    def setBlocked(self, row, col):
        self.grid[row][col] = OBSTACLE

    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)
    def startMaze(self):
        self.setDimCols = 0
        self.setDimRows = 0
        self.setStartCol = 0
        self.setStartRow = 0
        self.setEndCol = 0
        self.setEndRow = 0
        self.grid = [[]]

        self.grid[0][0] = EMPTY


    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)
    def startMaze(self, columns=0, rows=0):
        #HINT: populate grid with dimension row,column with zeros
        self.setDimCols = 0
        self.setDimRows = 0
        self.setStartCol = 0
        self.setStartRow = 0
        self.setEndCol = 0
        self.setEndRow = 0
        self.grid = [[]]

        if colums>0 and rows>0:
            self.grid = numpy.empty((rows, colums), dtype=int)
            for i in range(row):
                for j in range(columns):
                    self.grid[i][j]=0

    # Define what shall happen after the full information of a maze has been received
    def endMaze(self):
        self.grid[self.setStartRow][self.setStartCol] = self.START
        self.grid[self.setEndRow][self.setEndCol] = self.TARGET

    # just prints a maze on the command line
    def printMaze(self):
        print(self.grid)

    # loads a maze from a file pathToConfigFile
    def loadMaze(self,pathToConfigFile):
        # check whether a function numpy.loadtxt() could be useful
        self.grid=numpy.loadtxt(pathToConfigFile, delimiter=',',dtype=int)
        self.setDimCols=self.grid.shape[0]
        self.setDimRows=self.grid.shape[1]

        start_arr = numpy.where(self.grid == 2)
        self.setStartRow=int(start_arr[0][0])
        self.setStartCol=int(start_arr[1][0])

        end_arr = numpy.where(self.grid == 3)
        self.setEndRow=int(end_arr[0][0])
        self.setEndCol=int(end_arr[1][0])

    # clears the complete maze 
    def clearMaze(self):
        self.startMaze()
  
    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self,row,column):
        if row < 0:
            return False

        if column < 0:
            return False

        if row >= self.grid.shape[0]:
            return False

        if column >= self.grid.shape[1]:
            return False

        return True


    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self,row,column):
        neighbours = []

        # no neighbours for out-of-grid elements
        if self.isInGrid(row,column) == False:
            return neighbours

        # no neighbours for blocked grid elements
        if self.grid[row,column] == self.OBSTACLE:
            return neighbours
    
        nextRow = row + 1    
        if (self.isInGrid(nextRow,column) == True and self.grid[nextRow][column] != self.OBSTACLE):
            neighbours.append([nextRow,column]) 

        previousRow = row - 1    
        if (self.isInGrid(previousRow,column) == True and self.grid[previousRow][column] != self.OBSTACLE):
            neighbours.append([previousRow,column])

        nextColumn = column + 1    
        if (self.isInGrid(row,nextColumn) == True and self.grid[row][nextColumn] != self.OBSTACLE):
            neighbours.append([row,nextColumn])

        previousColumn = column - 1    
        if (self.isInGrid(row,previousColumn) == True and self.grid[row][previousColumn] != self.OBSTACLE):
            neighbours.append([row,previousColumn])

        return neighbours
        # TODO: Add a Unit Test Case --> Very good example for boundary tests and condition coverage


    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self,row,col):
        result = "" + str(row) + "," + str(col)
        return result
    
        # HINT: this method is used as primary key in a lookup table
    
    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        pass


    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]
    def heuristic(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        # HINT: a good heuristic could be the distance between to grid elements aGrid and bGrid
        pass

    # Generates the resulting path as string from the came_from list
    def generateResultPath(self,came_from):
        endpoint = self.gridElementToString(self.setEndRow, self.setEndCol)
        solutionPath = [[self.setEndRow, self.setEndCol]]
        
        if endpoint in came_from:
            current = endpoint

            while came_from[current] != None:
                solutionPath.append(came_from[current])
                current = self.gridElementToString(came_from[current][0],came_from[current][1])

        else:  
            print("no solution!")

        return solutionPath

    #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
    #############################
    def myMazeSolver(self):
        start = [self.setStartRow, self.setStartCol]
        frontier = queue.Queue()        
        frontier.put(start)             #legt Anfangskoordinaten in die Queue
        startKey = self.gridElementToString(self.setStartRow, self.setStartCol) 
                                        #Key für Dictionary

        came_from = {}                  #Speichert, wo man schon war: ["aktuelle Koordinaten", Koordinaten "wo man schon war"]
        came_from[startKey] = None      #Startwert hat keine vorigen Neighbours

        while not frontier.empty():
            current = frontier.get()    #firstINfirstOUT nimmt die nächste Position und löscht sie

            for next in self.getNeighbours(current[0], current[1]):
                                        #IN operator (mächtig) wandert alle Variablen der funktion ab (getNeighbours wird nur einma aufgerufen)
                                        #in next werden die ERSTEN Nachbarkoordinaten gespeichert
                nextKey = self.gridElementToString(next[0], next[1])
                if nextKey not in came_from:        #sucht in Key in der Dictionary, ob wir dort schon waren
                    frontier.put(next)              #legt neue Nachbarkoordinaten in frontierQueue
                    came_from[nextKey] = current    #speichert die vorige Position ab
        
        result_path = self.generateResultPath(came_from)

        return result_path


    def myMazeSolverA(self):
        pass
        


    # Command for starting the solving procedure
    def solveMaze(self):
        return self.myMazeSolver()


if __name__ == '__main__':
    mg = MazeSolverAlgoTemplate()


    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    mg.loadMaze("\\Users\\Elke\\Documents\\CodeCamp\\MazeRunner\\MazeExamples\\Maze1.txt")
    mg.printMaze()

    neighbours = mg.getNeighbours(0,0)
    print(neighbours)
    #print(mg.gridElementToString(mg.setStartRow,mg.setStartCol))
    solutionString = mg.solveMaze()
    print(solutionString)
   

## File:    project2.py
# Author:  Jake Horvers
# Date:    12/5/2014
# Section: 7
# E-mail:  horvers1@umbc.edu 
# Description:
# Reads in a maze and solves it using recursion
import sys
#Description: Calls the necessary functions to run the maze
#Input: None
#Output: Solution to the maze if possible, error messages if invalid parameters
#and no solution if it isn't solvable
def main():
    #Greets user and reads in maze file/associated arguments
    printGreeting()
    processed=[]
    processed=processCommandLineArgs()
    #Throws errors based on the problem the user is causing
    if(processed==(None,None,None)):
        print("Invalid number of parameters you silly billy")
        return
    try:
        textFileName=processed[0]
        file1=open(textFileName,"r")
    except:
        print("Invalid parameters my friend, try again!")
        return
    #At this point, the file must be readable so it reads in the file
    #and the parameters for the maze
    mazeHere=readMazeFile(textFileName)
    path=searchMaze(mazeHere,processed[1],processed[2])
    #Prints the path if it's solvable
    if(path==False):
        print("No solutions found")
    else:
        print('Solution Found!')
        print()
        printPath(path)
#Description: Greets the user
#Input:None
#Output:A greeting to the program
def printGreeting():
    print("This program will solve mazes using a recursive search.")
    print("Running maze search...")
    print("Results: ",end="")
#Desciption:
#Input:command line arguments for reading the file
#Output: The arguments if valid, None if not valid
def processCommandLineArgs():
    arguments=sys.argv
    #Try to read the file, return none if it is invalid amount
    try:
        textFile=arguments[1]
        start=int(arguments[2]),int(arguments[3])
        end=int(arguments[4]),int(arguments[5])
    except:
        return None,None,None
    #Try to read the file, return none if the name is invalid
    try:
        file1=open(textFile,"r")
    except:
        return None
    #Since the file is valid, open it and get the maze size
    file1=open(textFile,"r")
    mazeParameters=file1.readline().strip()
    numRows=int(mazeParameters[0])
    numCols=int(mazeParameters[2])
    file1.close()
    #Check to make sure the given parameters are within the maze
    if((start[0]<numRows and end[0]<numRows) and (start[1]<numCols and end[1]<numCols) and start[0]>=0 and start[1]>=0 and end[0]>=0 and end[1]>=0):
        return textFile,start,end
    else:
        return None
#Description: Reads the maze file
#Input: The name of the text file
#Output: the maze as a 2d list
def readMazeFile(filename):
    file1=open(filename,"r")
    rows=file1.readline().strip()
    #Grabs the amount of rows and columns
    numRows=int(rows[0])
    numCols=int(rows[2])
    #Generates the rows and columns
    maze=[[0 for x in range(numCols)]for x in range(numRows)]
    for i in range (numRows):
        for j in range(numCols):
            #Fills each (row,column) value with the squares from each line of the text file
            square= file1.readline().strip()
            maze[i][j]=square 
    return(maze)

#Description: Searches the maze for a solution and returns the solution if possible
#Input: The maze to solve, the start location and the end location
#Output: The list of the solution if it's possible
def searchMaze(maze,start_pos,finish_pos):
    #Creates a temp list to store the solution in
    vagueList=[]
    vagueList.append(start_pos)
    #Creates a list to see if the values have been popped
    emptyPopped=[]
    #Calls searchMazeRecurse to solve the maze using recursion or False if it's not possible
    if(searchMazeRecurse(maze,vagueList,finish_pos,emptyPopped)==True):
        return vagueList
    else:
        return False
#Description: Uses recursion to solve the maze
#Input: Maze to solve, the path taken so far, the end position, and the list of failed paths
#Output: True if the Maze can be solved
def searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped):
    #Checks to see if the current position is the end position
    if(path_so_far[-1]==finish_pos):
        return True
    else:
        #Sets the current row and column
        row=path_so_far[-1][0]
        col=path_so_far[-1][1]
        #Total amount of rows and columns
        rowAmount=len(maze)-1
        colAmount=len(maze[0])-1
        #Loops through to check each wall for openness
        for i in range(0,7,2):
            #Checcks if the wall is open, within the bounds, and isn't a failed path
            if(int(maze[row][col][i])==0):
                #Checks right wall to see if it's a valid move
                if(i==0 and (row,col+1) not in hasBeenPopped and (row,col+1)not in path_so_far and (col+1<=colAmount)):
                        path_so_far.append((row,(col+1)))
                        return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
                #Checks bottom wall to see if it's a valid move
                elif(i==2 and (row+1,col)not in hasBeenPopped and (row+1,col)not in path_so_far and (row+1<=rowAmount)):
                        path_so_far.append(((row+1),col))
                        return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
                #Checks left wall to see if it's a valid move
                elif(i==4 and (row,col-1) not in hasBeenPopped and (row,col-1)not in path_so_far and (col-1>=0)):
                        path_so_far.append((row,(col-1)))
                        return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
                #Checks top wall to see if it's a valid move
                elif(i==6 and (row-1,col) not in hasBeenPopped and (row-1,col)not in path_so_far and (row-1>=0)):
                        path_so_far.append(((row-1),col))
                        return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
        #Pops the last value if all other paths are unavailable
        else:
            hasBeenPopped.append(path_so_far.pop())
            return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
#Desctiption: Prints the path if the maze is solvable
#Input:The winning path
#Output:The winning path
def printPath(path):
    for i in range (len(path)):
        print(path[i])

main()

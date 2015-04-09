import sys
def main():
    printGreeting()
    processed=[]
    processed=processCommandLineArgs()
    textFileName=processed[0]
    file1=open(textFileName,"r")
    mazeHere=readMazeFile(textFileName)    
    path=searchMaze(mazeHere,processed[1],processed[2])
    if(path==False):
        print("No solutions found")
    else:
        print('Solution Found!')
        print()
        printPath(path)
def printGreeting():
    print("This program will solve mazes using a recursive search.")
    print("Running maze search...")
    print("Results: ",end="")
def processCommandLineArgs():
    arguments=sys.argv
    textFile=arguments[1]
    start=int(arguments[2]),int(arguments[3])
    end=int(arguments[4]),int(arguments[5])
    return textFile,start,end
def readMazeFile(filename):
    file1=open(filename,"r")
    rows=file1.readline().strip()
    numRows=int(rows[0])
    numCols=int(rows[2])
    maze=[[0 for x in range(numCols)]for x in range(numRows)]
    for i in range (numRows):
        for j in range(numCols):
            square= file1.readline().strip()
            maze[i][j]=square 
    return(maze)

def searchMaze(maze,start_pos,finish_pos):
    vagueList=[]
    vagueList.append(start_pos)
    emptyPopped=[]
    if(searchMazeRecurse(maze,vagueList,finish_pos,emptyPopped)==True):
        return vagueList
    else:
        return False
def searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped):
    if(path_so_far[-1]==finish_pos):
        return True
    else:
        row=path_so_far[-1][0]
        col=path_so_far[-1][1]
        rowAmount=len(maze)-1
        colAmount=len(maze[0])-1
        for i in range(0,7,2):
            if(int(maze[row][col][i])==0):
                if(i==0 and (row,col+1) not in hasBeenPopped and (row,col+1)not in path_so_far and (col+1<=colAmount)):
                        path_so_far.append((row,(col+1)))
                        return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
                elif(i==2 and (row+1,col)not in hasBeenPopped and (row+1,col)not in path_so_far and (row+1<=rowAmount)):
                        path_so_far.append(((row+1),col))
                        return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
                elif(i==4 and (row,col-1) not in hasBeenPopped and (row,col-1)not in path_so_far and (col-1>=0)):
                        path_so_far.append((row,(col-1)))
                        return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
                elif(i==6 and (row-1,col) not in hasBeenPopped and (row-1,col)not in path_so_far and (row-1>=0)):
                        path_so_far.append(((row-1),col))
                        return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
        else:
            hasBeenPopped.append(path_so_far.pop())
            return(searchMazeRecurse(maze,path_so_far,finish_pos,hasBeenPopped))
def printPath(path):
    for i in range (len(path)):
        print(path[i])

main()

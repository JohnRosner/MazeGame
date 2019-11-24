from random import *

class cell:
    def __init__(self):
        self.leftNeighbor = False
        self.rightNeighbor = False
        self.upNeighbor = False
        self.downNeighbor = False
        self.neighbor = False
        self.inMaze = False
    
    def up(self):
        self.upNeighbor = True
    def left(self):
        self.leftNeighbor = True
    def right(self):
        self.rightNeighbor = True
    def down(self):
        self.downNeighbor = True
        
    def becomeNeighbor(self):
        self.neighbor = True
    def maze(self):
        self.neighbor = False
        self.inMaze = True
        
    def getMaze(self):
        return self.inMaze
    def isNeighbor(self):
        return self.neighbor
        
    def getConnections(self):
        connections = [self.upNeighbor, self.downNeighbor, self.leftNeighbor, self.rightNeighbor]
        return connections

maze = [[]]
neighbors = []

def joinMaze(x, y):
    maze[x][y].maze()
    if x < len(maze) - 1:
        if not maze[x+1][y].getMaze() and not maze[x+1][y].isNeighbor():
            maze[x+1][y].becomeNeighbor()
            neighbors.append((x+1, y))
    if y < len(maze[0]) - 1:
        if not maze[x][y+1].getMaze() and not maze[x][y+1].isNeighbor():
            maze[x][y+1].becomeNeighbor()
            neighbors.append((x, y+1))
    if x > 0:
        if not maze[x-1][y].getMaze() and not maze[x-1][y].isNeighbor():
            maze[x-1][y].becomeNeighbor()
            neighbors.append((x-1, y))
    if y > 0:
        if not maze[x][y-1].getMaze() and not maze[x][y-1].isNeighbor():
            maze[x][y-1].becomeNeighbor()
            neighbors.append((x, y-1))
    return

#Add a cell to the maze
#First picks a random neighbor cell
#Finds and picks a random cell in the maze to connect to
#Establish said connection
#Add the neighbor cell to the maze
#Add new neighboring cells to neighbors
def nextMaze():
    randNeighbor = randint(0, len(neighbors) - 1)
    
    neighborX = neighbors[randNeighbor][0]
    neighborY = neighbors[randNeighbor][1]
    
    connections = []
    if neighborX > 0:
        if maze[neighborX - 1][neighborY].getMaze():
            connections.append(1)
    if neighborX < len(maze) - 1:
        if maze[neighborX + 1][neighborY].getMaze():
            connections.append(2)
    if neighborY > 0:
        if maze[neighborX][neighborY - 1].getMaze():
            connections.append(3)
    if neighborY < len(maze[0]) - 1:
        if maze[neighborX][neighborY + 1].getMaze():
            connections.append(4)

    randConnection = randint(0, len(connections) - 1)
    #print(connections)
    #print(randConnection)
    if connections[randConnection] == 1:
        maze[neighborX][neighborY].left()
    if connections[randConnection] == 2:
        maze[neighborX][neighborY].right()
    if connections[randConnection] == 3:
        maze[neighborX][neighborY].down()
    if connections[randConnection] == 4:
        maze[neighborX][neighborY].up()
    
    joinMaze(neighborX, neighborY)
    del neighbors[randNeighbor]
    
    return


def generateMaze(width, height):

    for i in range(width):
        for j in range(height):
            maze[i].append(cell())
        if i < width - 1:
            maze.append([])
        
    joinMaze(int(width / 2), int(height / 2))
    
    while len(neighbors) > 0:
        nextMaze()
        
    boolMaze = [[]]
    
    for i in range(2*width+1):
        for j in range(2*height+1):
            boolMaze[i].append(False)
        boolMaze.append([])
    
    for i in range (0, width):
        for j in range (0, height):
            boolMaze[2 * i + 1][2 * j + 1] = True
            cellConnections = maze[i][j].getConnections()
            if cellConnections[0]: #Up
                boolMaze[2 * i + 1][2 * j + 1 + 1] = True
            if cellConnections[1]: #Down
                boolMaze[2 * i + 1][2 * j - 1 + 1] = True
            if cellConnections[2]: #Left
                boolMaze[2 * i - 1 + 1][2 * j + 1] = True
            if cellConnections[3]: #Right
                boolMaze[2 * i + 1 + 1][2 * j + 1] = True
                
    return boolMaze          

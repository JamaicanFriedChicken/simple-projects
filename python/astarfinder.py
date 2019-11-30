'''
A standard implementation of A* pathfinding algorithm in python

Pseudocode:

A* (star) Pathfinding // Initialize both open and closed list
let the openList equal empty list of nodes
let the closedList equal empty list of nodes// Add the start node
put the startNode on the openList (leave it's f at zero)// Loop until you find the end
while the openList is not empty    // Get the current node
    let the currentNode equal the node with the least f value
    remove the currentNode from the openList
    add the currentNode to the closedList    // Found the goal
    if currentNode is the goal
        Congratulations! You've found the end! Backtrack to get path    // Generate children
    let the children of the currentNode equal the adjacent nodes

    for each child in the children        // Child is on the closedList
        if child is in the closedList
            continue to beginning of for loop        // Create the f, g, and h values
        child.g = currentNode.g + distance between child and current
        child.h = distance from child to end
        child.f = child.g + child.h        // Child is already in openList
        if child.position is in the openList's nodes positions
            if the child.g is higher than the openList node's g
                continue to beginning of for loop        // Add the child to the openList
        add the child to the openList
'''


class Node():
    """
    A class Node for A* pathfinding algorithm
    """
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.f = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):

    # Create start and end node
    startNode = Node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0

    # Initialize open list and closed list for algorithm
    openList = []
    closedList = []
    openList.append(startNode)

    # Loops until the it arrives at destination
    while len(openList) > 0:

        # Fetches the current node
        currentNode = openList[0]
        currentIndex = 0
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex= index

        # Shifts current index from open list and adds current node to closed list
        openList.pop(currentIndex)
        closedList.append(currentNode)

        # Finds the goal
        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # returns path it took to reach to destination

        # Generates children
        children = []
        for newPosition in [(0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (-1, 1), (1, -1), (1, 1)]:

            # Gets node's position
            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            # Ensures it is within range
            if  nodePosition[0] > (len(maze) - 1) or nodePosition[0] < 0 or  \
                nodePosition[1] > (len(maze[len(maze) - 1]) - 1) or \
                nodePosition[1] < 0:
                continue

            # Ensures path is accessible within maze
            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            # Creates new node
            newNode = Node(currentNode, nodePosition)

            children.append(newNode)

            for child in children:
                for closedChild in closedList:
                    if child == closedChild:
                        continue

            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + \
                      ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    continue

            openList.append(child)

def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (10, 8)

    astar(maze, start, end)


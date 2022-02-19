# steepest ascent hill climbing
import random

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def pathLength(tsp, solution):
    pathLength = 0
    for i in range(len(solution)):
        pathLength += tsp[solution[i-1]][solution[i]]
    return pathLength

def getNeighbours(solution):
    neighbors = []
    #swap and find neighbour
    for i in range(len(solution)):
        for j in range(i+1,len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)
    return neighbors

def getBestNeighbour(tsp, neighbours):

    #assume first neighbour is best
    bestPathLength = pathLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    #find best
    for neighbour in neighbours[1:]:
        currentPathLength = pathLength(tsp, neighbour)
        if currentPathLength<bestPathLength:
            bestPathLength = currentPathLength
            bestNeighbour = neighbour
    return bestNeighbour, bestPathLength

def hillClimb(tsp):
    #generate random solution
    currentSolution = randomSolution(tsp)
    currentPathLength = pathLength(tsp, currentSolution)
    # print(currentSolution)
    # print(currentPathLength)

    #find neighbours
    neighbours = getNeighbours(currentSolution)
    # print(neighbours)

    #find best neighbour
    bestNeighbour, bestNeighbourPathLength = getBestNeighbour(tsp, neighbours)

    #search in tree and update current solution huristically
    #while best solution is possible go 
    while bestNeighbourPathLength < currentPathLength:
        currentSolution = bestNeighbour
        currentPathLength = bestNeighbourPathLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourPathLength = getBestNeighbour(tsp, neighbours)
    
    #final solution
    return currentSolution, currentPathLength

if __name__ == "__main__":

    # distance array
    tsp = [[0,400,500,300],[400,0,300,500],[300,500,0,400],[300,500,400,0]]

    print(hillClimb(tsp))
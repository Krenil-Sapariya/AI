# hill climbing
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

def hillClimb(tsp):
    visited = []
    #generate random solution
    currentSolution = randomSolution(tsp)
    currentPathLength = pathLength(tsp, currentSolution)
    # print(currentSolution)
    # print(currentPathLength)

    #find neighbours
    neighbours = getNeighbours(currentSolution)
    # print(neighbours)

    while neighbours:
        neighbour = neighbours.pop(0)
        if neighbour not in visited:
            visited.append(neighbour)
            # print("neigh",neighbour)
            
            neighbourPathLength = pathLength(tsp, neighbour)
            if neighbourPathLength < currentPathLength:
                currentSolution = neighbour
                currentPathLength = neighbourPathLength
            neighbours.extend(getNeighbours(currentSolution))

    #final solution
    return currentSolution, currentPathLength

if __name__ == "__main__":

    # distance array
    tsp = [[0,400,500,300],[400,0,300,500],[300,500,0,400],[300,500,400,0]]

    print(hillClimb(tsp))
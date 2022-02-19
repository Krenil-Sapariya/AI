import random
cities = ['Boston', 'New York', 'Miami', 'Dellas', 'San Francisco']
matrix = [[0, 250, 1450, 1700, 3000],
          [250, 0, 1200, 1500, 2900],
          [1450, 1200, 0, 1600, 3300],
          [1700, 1500, 1600, 0, 1700],
          [3000, 2900, 3300, 1700, 0]]
route = []
min_dist = 0
initial_state = 2
current_state = initial_state
temp = 0
while(len(route) < len(cities)):
    temp = matrix[current_state].index(max(matrix[current_state]))
    for i in range(len(matrix[current_state])):
        if((i not in route) and matrix[current_state][i] <= matrix[current_state][temp]):
            temp = i
            min_dist += (matrix[current_state][temp])
            current_state = temp
            route.append(temp)
            min_dist += matrix[initial_state][current_state]
            route.append(initial_state)
print("Shortest route by distance : ")
print(route)
print(min_dist)
final = route.copy()
temp_route = route.copy()
final_dist = min_dist
iteration = 1000
mutation_rate = 0.01
print("Final_Route : ", final)
for x in range(0, iteration):
    for i in range(1, len(temp_route)-1):
        if(random.random() < mutation_rate):
            j = int(random.random()*(len(temp_route)-2))+1
            temp_route[i], temp_route[j] = temp_route[j], temp_route[i]
            temp = 0
        for k in range(len(temp_route)-1):
            temp += matrix[temp_route[k]][temp_route[k+1]]
            if(temp <= final_dist):
                #print("If entered")
                final_dist = temp
                final = temp_route.copy()
#print("Final route : ",final)
#print("Final dist : ",final_dist)
            else:
                temp_route = final.copy()
print("Final route ")
for i in final:
    print(cities[i], end="->")
    print("\n")

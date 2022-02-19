from collections import deque

def bfs(jug1, jug2, goal):
	
	#to store visited states
	visited = {}
	isSolvable = False
	path = []
	
	#queue to maintain states
	q = deque()
	
	#initialing with initial state
	q.append((0, 0))

	while (len(q) > 0):
		u = q.popleft()
		#if state is already visited
		if ((u[0], u[1]) in visited):
			continue

		if ((u[0] > jug1 or u[1] > jug2 or
			u[0] < 0 or u[1] < 0)):
			continue

		path.append([u[0], u[1]])

		#state visited
		visited[(u[0], u[1])] = 1

		#check if problem solved?
		if (u[0] == goal or u[1] == goal):
			isSolvable = True
			
			if (u[0] == goal):
				if (u[1] != 0):
					
					#final state
					path.append([u[0], 0])
			else:
				if (u[0] != 0):

					#final state
					path.append([0, u[1]])

			#print the solution path
			sz = len(path)
			print("\njug-1 , jug-2")
			for i in range(sz):
				print(path[i][0], "  ,  ",path[i][1])
			break

        #fill jug2
		q.append([u[0], jug2]) 
        #fill jug1
		q.append([jug1, u[1]]) 

		for ap in range(max(jug1, jug2) + 1):

			#empty jug2 into jug1
			c = u[0] + ap
			d = u[1] - ap

			if (c == jug1 or (d == 0 and d >= 0)):
				q.append([c, d])

			# empty jug1 into jug2
			c = u[0] - ap
			d = u[1] + ap

			if ((c == 0 and c >= 0) or d == jug2):
				q.append([c, d])
		
		#empty jug2
		q.append([jug1, 0])
		
		#empty jug1
		q.append([0, jug2])

	# No, solution exists if ans=0
	if (not isSolvable):
		print ("No solution possible!")

# Driver code
if __name__ == '__main__':
	
	jug1, jug2, goal = 4, 3, 2
	print(" Jug-1 capacity: {}\n Jug-2 capacity: {}\n Goal-> Fill Jug-2 with {} liters of water".format(jug1, jug2, goal))
	
	bfs(jug1, jug2, goal)
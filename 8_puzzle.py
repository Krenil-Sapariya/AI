import sys
import numpy as np


class Node:
    #Node structure
	def __init__(self, state, parent, move):
		self.state = state
		self.parent = parent
		self.move = move


class stack:
	def __init__(self):
		self.block = []

    #add block
	def add(self, node):
		self.block.append(node)

	def contains_state(self, state):
		return any((node.state[0] == state[0]).all() for node in self.block)
	
	def empty(self):
		return len(self.block) == 0
	
	def remove(self):
		if self.empty():
			raise Exception("Empty block")
		else:
			node = self.block[-1]
			self.block = self.block[:-1]
			return node


class queue(stack):
    #remove from queue for further exploration
	def remove(self):
		if self.empty():
			raise Exception("Empty block")
		else:
			node = self.block[0]
			self.block = self.block[1:]
			return node


class Puzzle:
	def __init__(self, start, startIndex, goal, goalIndex):
		self.start = [start, startIndex]
		self.goal = [goal, goalIndex] 
		self.solution = None

	def neighbors(self, state):
		mat, (row, col) = state
		results = []
		
        #decide moves for 3x3 matrix
		if row > 0:
			mat1 = np.copy(mat)
			mat1[row][col] = mat1[row - 1][col]
			mat1[row - 1][col] = 0
			results.append(('up', [mat1, (row - 1, col)]))
		if col > 0:
			mat1 = np.copy(mat)
			mat1[row][col] = mat1[row][col - 1]
			mat1[row][col - 1] = 0
			results.append(('left', [mat1, (row, col - 1)]))
		if row < 2:
			mat1 = np.copy(mat)
			mat1[row][col] = mat1[row + 1][col]
			mat1[row + 1][col] = 0
			results.append(('down', [mat1, (row + 1, col)]))
		if col < 2:
			mat1 = np.copy(mat)
			mat1[row][col] = mat1[row][col + 1]
			mat1[row][col + 1] = 0
			results.append(('right', [mat1, (row, col + 1)]))

		return results

	def print(self):
		solution = self.solution if self.solution is not None else None
		print("Start State:\n", self.start[0], "\n")
		print("Goal State:\n",  self.goal[0], "\n")
		print("\nStates visited: ", self.num_explored, "\n")
		print("Solution:\n ")
		for move, cell in zip(solution[0], solution[1]):
			print("move: ", move, "\n", cell[0], "\n")
		print("goal state reached!!")

	def does_not_contain_state(self, state):
		for st in self.visited:
			if (st[0] == state[0]).all():
				return False
		return True
	
    #main function
	def solve(self):
		self.num_explored = 0

		start = Node(state=self.start, parent=None, move=None)
		block = queue()
		block.add(start)

		self.visited = [] 

		while True:

            #for no solution
			if block.empty():
				raise Exception("No solution possible!")

			node = block.remove()
			self.num_explored += 1

			if (node.state[0] == self.goal[0]).all():
				actions = []
				cells = []

                #search
				while node.parent is not None:
					actions.append(node.move)
					cells.append(node.state)
					node = node.parent
				actions.reverse()
				cells.reverse()
				self.solution = (actions,  cells)
				return

            #add to visited
			self.visited.append(node.state)

            #for neighbours
			for move, state in self.neighbors(node.state):
				if not block.contains_state(state) and self.does_not_contain_state(state):
					child = Node(state=state, parent=node, move=move)
					block.add(child)


start = np.array([[1, 2, 3], [4, 0, 5], [7, 8, 6]])
goal = np.array([[1,2,3],[4,5,6],[0,7,8]])

#index of empty block at starting and at goal state
startIndex = (1, 1)
goalIndex = (2, 2)


p = Puzzle(start, startIndex, goal, goalIndex)
p.solve()
p.print()
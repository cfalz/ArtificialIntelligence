from Problem import *
import numpy as np

initial_state = np.array([[1,2,3],[4,8,0],[7,6,5]])
goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])

puzzle = PuzzleProblem(initial_state, goal_state, 8)
print(puzzle.size)
print(puzzle.initial_state)
print(puzzle.goal_state)
print(puzzle.operators)







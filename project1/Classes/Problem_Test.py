from Problem import *
from Node import *
import numpy as np


initial_state_8 = np.array([[1,2,3],[4,8,0],[7,6,5]])
goal_state_8 = np.array([[1,2,3],[4,5,6],[7,8,0]])

initial_state_15 = np.array([[1,2,3,10],[4,8,17,11],[7,6,5,12],[13,2,3,0]])
goal_state_15 = np.array([[1,2,3,10],[4,5,6,11],[7,8,0,12],[1,2,3,10]])

puzzle = PuzzleProblem(initial_state_8, goal_state_8, 8)

def test_size():
    print("The Puzzle Size Is:")
    print(puzzle.size)

def problem_states():
    print("The Puzzle initial_state Is:")
    print(puzzle.initial_state)

    print("The Puzzle goal_state Is:")
    print(puzzle.goal_state)

def evalute_test():
    new_state = puzzle.evaluate(puzzle.initial_state, "move_up")
    print new_state

def edges_test():
    print("The Puzzle operators are:")
    print(puzzle.get_operators(initial_state))
    print("The Puzzle edge lists are:")
    print("top_edge")
    print(puzzle.top_edge)
    print("bottom_edge")
    print(puzzle.bottom_edge)
    print("left_edge")
    print(puzzle.left_edge)
    print("right_edge")
    print(puzzle.right_edge)

def corners_test():
    print("The Puzzle Corner lists are:")
    for corner_indices in puzzle.corners:
        print corner_indices
        if (0,0) == corner_indices:
            print "YES"
        else:
            print "NO"
    if (0,0) in puzzle.corners:
        print "YES"
    else:
        print "NO"


n = Node(puzzle.initial_state, 0)

def node_child_test():
    print("Initial Node State: ")
    print n.state
    new_node= n.child(puzzle, "move_left")
    print("New Node Information: ")
    new_node.print_stats()

def node_explore_test():
    print("Initial Node State: ")
    print n.state
    print("[!] Exploring Nodes....")
    print("\n")
    children = n.explore(puzzle)
    for child in children:
        print("\n")
        print child
        child.print_stats()
        print("\n")
        
    
    

    
#node_child_test()
node_explore_test()





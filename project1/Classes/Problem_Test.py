from __future__ import print_function
from Problem import *
from Node import *
from Search import *
import numpy as np
import time


initial_state_8 = np.array([[1,2,3],[4,8,0],[7,6,5]])
goal_state_8 = np.array([[1,2,3],[4,5,6],[7,8,0]])

initial_state_15 = np.array([[1,2,3,10],[4,8,17,11],[7,6,5,12],[13,9,14,0]])
goal_state_15 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])

puzzle = PuzzleProblem(initial_state_8, goal_state_8)

def test_size():
    print("The Puzzle Size Is:")
    print(puzzle.size)

def problem_states():
    print("The Puzzle initial_state Is:")
    print(puzzle.initial_state)

    print("The Puzzle goal_state Is:")
    print(puzzle.goal_state)

def evaluate_test():
    up_state = puzzle.evaluate(puzzle.initial_state, "move_up")
    print("[!] Printing State After Moving Up.")
    print(up_state)
    down_state = puzzle.evaluate(puzzle.initial_state, "move_down")
    print("[!] Printing State After Moving Down.")
    print(down_state)
    left_state = puzzle.evaluate(puzzle.initial_state, "move_left")
    print("[!] Printing State After Moving Left.")
    print(left_state)
    right_state = puzzle.evaluate(puzzle.initial_state, "move_right")
    print("[!] Printing State After Moving Right.")
    print(right_state)

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
        print(corner_indices)
        if (0,0) == corner_indices:
            print("YES")
        else:
            print("NO")
    if (0,0) in puzzle.corners:
        print("YES")
    else:
        print("NO")


n = Node(puzzle.initial_state, 0)

def node_child_test():
    print("Initial Node State: ")
    print(n.state)
    new_node= n.make_move(puzzle, "move_left")
    print("New Node Information: ")
    new_node.print_stats()

def node_explore_test():
    print("Initial Node State: ")
    print(n.state)
    print("[!] Exploring Nodes....")
    print("\n")
    children = n.explore(puzzle)
    for child in children:
        #print("\n")
        #print child
        child.print_stats()
        print("\n")

def get_MT_cost_test():
    print("[!] The Puzzle Goal State is: ")
    print(puzzle.goal_state)
    print("[!] The Node State is: ")
    print(n.state)
    print("[!] Calculating Misplaced Tile Cost of Node....")
    print("[!] The Cost is: " , n.get_MT_cost())
        
def UniformCostSearch_test():
    start_time = time.time()
    searcher = UniformCostSearch(puzzle)
    print("[!] Searching For Solution Using Uniform Cost Search....")
    solution = searcher.search()
    print("[+] Found Solution in ", time.time() - start_time, 's')
    print("[+] Solution Was Found At Depth ", solution.path_cost)
    print("[+] Printing the Found Puzzle Solution...")
    print(solution.state)
    print("[+] Printing the Moves to get to the Solution...")
    print(solution.path)
    
def AstarMisplacedTileSearch_test():
    start_time = time.time()
    searcher = AstarMisplacedTileSearch(puzzle)
    print("[!] Searching For Solution Using A* Misplaced Tile Hueristic....")
    solution = searcher.search()
    print("[+] Found Solution in ", time.time() - start_time, 's')
    print("[+] Solution Was Found At Depth ", solution.path_cost)
    print("[+] Printing the Found Puzzle Solution...")
    print(solution.state)
    print("[+] Printing the Moves to get to the Solution...")
    print(solution.path)


    
#evaluate_test()
#node_child_test()
#node_explore_test()
#get_MT_cost_test()

problem_states()
UniformCostSearch_test()
AstarMisplacedTileSearch_test()




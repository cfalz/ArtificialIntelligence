from __future__ import print_function
from Problem import *
from Node import *
from Search import *
import numpy as np
import time
import random


""" Some initial 8 peice puzzles """
initial_state_8 = np.array([[1,2,3],[4,8,0],[7,6,5]])
worst_initial = np.array([[8,0,6],[5,4,7],[2,3,1]]) # 440 s - 27 moves
worst_initial2 = np.array([[8,6,7],[2,5,4],[3,0,1]])
worst_initial3 = np.array([[6,4,7],[8,5,0],[3,2,1]])
initial_state_8_test2 = np.array([[0,4,8],[6,3,1],[7,5,2]])
initial_state_8_test3 = np.array([[8,5,7],[6,3,4],[1,2,0]])
initial_state_8_test4 = np.array([[6,3,0],[5,8,4],[2,7,1]])

""" Goal State For an 8 Peice Puzzle. """
goal_state_8 = np.array([[1,2,3],[4,5,6],[7,8,0]])


initial_state_15 = np.array([[1,2,3,0],[5,6,7,4],[9,10,11,8],[13,14,15,12]])
goal_state_15 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])


#puzzle = PuzzleProblem(initial_state_8_test2, goal_state_8)

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


#n = Node(puzzle.initial_state, 0)
#n2 = Node(puzzle.goal_state, 0)

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
        print("\n")
        print(child)
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
    print(validate_initial_state(worst_initial2))
    for initial_state in random_puzzle():
        start_time = time.time()
        puzzle = PuzzleProblem(worst_initial2, goal_state_8)
        searcher = AstarMisplacedTileSearch(puzzle)
        print("[!] Searching For Solution Using A* Misplaced Tile Hueristic....")
        solution = searcher.search()
        print("[+] Found Solution in ", time.time() - start_time, 's')
        print("[+] Solution Was Found At Depth ", solution.path_cost)
        print("[+] Printing the Found Puzzle Solution...")
        print(solution.state)
        print("[+] Printing the Moves to get to the Solution...")
        print(solution.path)
        print("\n")
        print("\n")

def get_MD_cost_test():
    print("[!] The Puzzle Goal State is: ")
    print(puzzle.goal_state)
    print("[!] The Node State is: ")
    print(n.state)
    print("[!] Calculating Misplaced Tile Cost of Node....")
    print("[!] The Cost is: " , n.get_MD_cost(puzzle))

def AstarManhattanDistanceSearch_test():
    print(validate_initial_state(worst_initial2))
    puzzle = PuzzleProblem(worst_initial2, goal_state_8)
    #mutation_of_worst_initial2 = np.array([[3,2,0],[1,5,6],[4,8,7]])
    #print(validate_initial_state(mutation_of_worst_initial2))
    #puzzle = PuzzleProblem(mutation_of_worst_initial2, goal_state_8)
    searcher = AstarManhattanDistanceSearch(puzzle)
    start_time = time.time()
    print("[!] Searching For Solution Using A* Manhattan Distance Hueristic....")
    solution = searcher.search()
    print("[+] Found Solution in ", time.time() - start_time, 's')
    print("[+] Solution Was Found At Depth ", solution.path_cost)
    print("[+] Printing the Found Puzzle Solution...")
    print(solution.state)
    print("[+] Printing the Moves to get to the Solution...")
    print(solution.path)
    
def in_container_test():
    searcher = AstarMisplacedTileSearch(puzzle)
    searcher.container.append(n)
    print("[!] The container has: ")
    for node in searcher.container:
        print(node.state)
    print("[!] Testing to see if \n", puzzle.initial_state , "\n is in the container. \n") 
    print(searcher.in_container(puzzle.initial_state))
    print("[!] Testing to see if \n", puzzle.goal_state , "\n is in the container. \n") 
    print(searcher.in_container(puzzle.goal_state))


def not_in_explored_test():
    searcher = AstarMisplacedTileSearch(puzzle)
    searcher.explored.append(n.state)
    print("[!] The explored list has: ")
    for state in searcher.explored:
        print(state)
    print("[!] Testing to see if \n", puzzle.initial_state , "\n is not in the explored list. \n") 
    print(searcher.not_in_explored(puzzle.initial_state))
    print("[!] Testing to see if \n", puzzle.goal_state , "\n is not in the explored list. \n") 
    print(searcher.not_in_explored(puzzle.goal_state))

def random_puzzle():
    puzzle = PuzzleProblem(goal_state_8, goal_state_8)
    state = goal_state_8
    statelist = []
    for moves in range(0,1):
        valid_moves = puzzle.get_operators(state)
        state = puzzle.evaluate(state, random.choice(valid_moves))
        statelist.append(state)
    return statelist


def Test_Searches():
    for initial_state in random_puzzle():

        """ A* MT """
        start_time = time.time()
        puzzle = PuzzleProblem(initial_state, goal_state_8)
        searcher = AstarMisplacedTileSearch(puzzle)
        print("[!] Searching For Solution Using A* Misplaced Tile Hueristic....")
        solution = searcher.search()
        print("[+] Found Solution in ", time.time() - start_time, 's')
        print("[+] Solution Was Found At Depth ", solution.path_cost)
        print("[+] Printing the Moves to get to the Solution...")
        print(solution.path)
        print("\n")
        print("\n")


        """ A* MD """
        start_time = time.time()
        puzzle = PuzzleProblem(initial_state, goal_state_8)
        searcher = AstarManhattanDistanceSearch(puzzle)
        print("[!] Searching For Solution Using A* Manhattan Distance Hueristic....")
        solution = searcher.search()
        print("[+] Found Solution in ", time.time() - start_time, 's')
        print("[+] Solution Was Found At Depth ", solution.path_cost)
        print("[+] Printing the Moves to get to the Solution...")
        print(solution.path)
        print("\n")
        print("\n")
        raw_input()




def inversions(state):
    puzzle = state.flatten().tolist()
    inversions = 0
    for peice in puzzle:
        if peice is not 0:
            index = puzzle.index(peice)
            for latter_peice in puzzle[index:]:
                if peice > latter_peice and latter_peice is not 0:
                    inversions += 1
    return inversions


def validate_initial_state(state):
    return state.size%2 != inversions(state)%2

def validate_test():
    for initial_state in random_puzzle():
        print('[!] Verifing The Puzzle: \n', initial_state, '\n')
        print('[!] The amount of inversions: ', inversions(initial_state))
        print('[!] The Puzzle size is: ', initial_state.size)
        print(validate_initial_state(initial_state))
        print('=================================================================')
        print("\n")
        print("\n")
        raw_input()

def insort_test():
        new_node = Node(initial_state8,0,1,2,None)
        new_node1 = Node(initial_state8,1,3,5,None)
        new_node2 = Node(initial_state8,5,7,2,None)
        l = []
        bisect.insort_left(l, new_node)
        bisect.insort_left(l, new_node1)
        bisect.insort_left(l, new_node2)
        for node in l:
            node.print_stats()
            raw_input()
    
#insort_test()
#evaluate_test()
#node_child_test()
#node_explore_test()
#get_MT_cost_test()
#problem_states()
#UniformCostSearch_test()
#AstarMisplacedTileSearch_test()
#get_MD_cost_test()
AstarManhattanDistanceSearch_test()
#in_container_test()
#not_in_explored_test()
#Test_Searches()
#validate_initial(initial_state_8) 
#validate_test()


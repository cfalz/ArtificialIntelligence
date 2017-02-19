from __future__ import print_function
from Problem import *
from Node import *
from Search import *
import time
import numpy as np


def greeting():
    print("Welcome to Cody Falzone's (SID: 860929046) Puzzle Solver.")

def puzzle_choice():
    choice = 0
    print("Enter Your Choice for a Puzzle.")
    print("1. Use a default puzzle.")
    print("2. Enter a puzzle.")

    while(True):
        choice = raw_input()
        if (str(choice) == 'q' or str(choice) == 'Q'):
            print("[!] Quitting the Program.")
            raise SystemExit
        elif int(choice) in range(1,3):
            return int(choice)
        else:
            print("[-] Invalid Selection, ", choice , " is not a choice, please try again.") 

def algorithm_choice():
    print("Enter Your Choice of Algorithm.")
    print("1. Uniform Cost Search")
    print("2. A* with Misplaced Tile heuristic")
    print("3. A* with Manhattan Distance heuristic")

    choice = 0
    while(True):
        choice = raw_input()
        if (str(choice) == 'q' or str(choice) == 'Q'):
            print("[!] Quitting the Program.")
            raise SystemExit
        elif int(choice) in range(1,4):
            return int(choice)
        else:
            print("[-] Invalid Selection, ", choice , " is not a choice, please try again.") 


def UniformCostSearchDriver(puzzle):
    start_time = time.time()
    searcher = UniformCostSearch(puzzle)
    print("[!] Searching For Solution Using Uniform Cost Search....")
    solution = searcher.search()
    print("[+] Found Solution in ", time.time() - start_time, 's')
    print("[+] Solution Was Found At Depth ", solution.path_cost)
    print("[+] Max Number of Nodes in the Frontier was " , searcher.maxfrontiersize)
    print("[+] Number of States Expanded was " , len(searcher.explored))
    print("[+] Printing the Found Puzzle Solution...")
    print(solution.state)
    print("[+] Printing the Moves to get to the Solution...")
    print(solution.path)
    print("\n")
    
def AstarMisplacedTileSearchDriver(puzzle):
    start_time = time.time()
    searcher = AstarMisplacedTileSearch(puzzle)
    print("[!] Searching For Solution Using A* Misplaced Tile Hueristic....")
    solution = searcher.search()
    print("[+] Found Solution in ", time.time() - start_time, 's')
    print("[+] Solution Was Found At Depth ", solution.path_cost)
    print("[+] Max Number of Nodes in the Frontier was " , searcher.maxfrontiersize)
    print("[+] Number of States Expanded was " , len(searcher.explored))
    print("[+] Printing the Found Puzzle Solution...")
    print(solution.state)
    print("[+] Printing the Moves to get to the Solution...")
    print(solution.path)
    print("\n")

def AstarManhattanDistanceSearchDriver(puzzle):
    searcher = AstarManhattanDistanceSearch(puzzle)
    start_time = time.time()
    print("[!] Searching For Solution Using A* Manhattan Distance Hueristic....")
    solution = searcher.search()
    print("[+] Found Solution in ", time.time() - start_time, 's')
    print("[+] Solution Was Found At Depth ", solution.path_cost)
    print("[+] Max Number of Nodes in the Frontier was " , searcher.maxfrontiersize)
    print("[+] Number of States Expanded was " , len(searcher.explored))
    print("[+] Printing the Found Puzzle Solution...")
    print(solution.state)
    print("[+] Printing the Moves to get to the Solution...")
    print(solution.path)
    print("\n")
    

def driver():
    greeting()
    pc = puzzle_choice() 

    """ Goal State For an 8 Peice Puzzle. """
    goal_state_8 = np.array([[1,2,3],[4,5,6],[7,8,0]])

    if pc is 1:
        """ Random Initial State for 8 Peice Puzzle. """
        initial_state_8 = np.array([[1,2,3],[4,8,0],[7,6,5]])

    if pc is 2:
        print("Enter the puzzle, Use a Zero to represent the blank.")
        print("Enter the First, Use a Space between numbers.")
        row1 = raw_input()
        row1 = "".join(row1.split())
        list1 = [ int(i) for i in row1 ]
        print("Enter the Second, Use a Space between numbers.")
        row2 = raw_input()
        row2 = "".join(row2.split())
        list2 = [ int(i) for i in row2 ]
        print("Enter the Third, Use a Space between numbers.")
        row3 = raw_input()
        row3 = "".join(row3.split())
        list3 = [ int(i) for i in row3 ]
        initial_state_8 = np.array([list1,list2,list3])
        print(initial_state_8)

    puzzle = PuzzleProblem(initial_state_8, goal_state_8)
    if not puzzle.validate_initial_state(puzzle.initial_state):
        print("[-] This puzzle is Not a Solvable (by the amount of inversions...).")
        print("[-] Exiting.....")
        raise SystemExit

    algorithm = algorithm_choice()

    if algorithm is 1:
        UniformCostSearchDriver(puzzle)
    elif algorithm is 2:
        AstarMisplacedTileSearchDriver(puzzle)
    elif algorithm is 3:
        AstarManhattanDistanceSearchDriver(puzzle)


driver()



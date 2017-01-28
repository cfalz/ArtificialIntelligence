""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Author: Cody Falzone
#SID: 860929046
#CS170 Winter 17
#Project 1 - A* Search

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

############################################################################
#
#    Abstract Base Class for a problem. 
#    Input: initial_state : The initial state of the problem. 
#           goal_state : The goal state of the problem.
#
############################################################################

class Problem(object):
    
    def __init__( self, initial_state, goal_state ):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def operators( self, state ):
        raise NotImplementedError

    def evaluate( self, state, operator ):
        raise NotImplementedError

    def is_goal( self, state ):
        return state == self.goal_state

""" Sliding Puzzle Problem that allows a specified size to be passed in. """
class PuzzleProblem(Problem):
    
    """ This is the defualt constructor for the Puzzle Problem.://github.com/cfalz/AI.git 
     It allows you to choose and size and the operators are in reference
     to moving the blank in the puzzle. """

    def __init__( self, initial_state, goal_state, size ):
            super(PuzzleProblem, self).__init__(initial_state, goal_state)
            self.size = size
            self.operators = ["move_left", "move_right", "move_up", "move_down"]

    def operators( self, state = None ):
        possible_moves = []
        blank_index = state.unravel_index(0, state.shape)
        if(blank_index in corners)
            if(blank_index == top_left_corner):
                possible_moves.append(self.operators[3])
                possible_moves.append(self.operators[1])
                return possible_moves
            if(blank_index == top_right_corner):
                possible_moves.append(self.operators[3])
                possible_moves.append(self.operators[0])
                return possible_moves
            if(blank_index == bottom_left_corner):
                possible_moves.append(self.operators[2])
                possible_moves.append(self.operators[1])
                return possible_moves
            if(blank_index == bottom_right_corner):
                possible_moves.append(self.operators[2])
                possible_moves.append(self.operators[0])
                return possible_moves
        if(blank_index.on_top_edge()):
        elif(blank_index.on_left_edge()):
        elif(blank_index.on_right_edge()):
        elif(blank_index.on_bottom_edge()):
        else:
        return self.operators 

    """ Accessor for the puzzle's size. """
    def size(self):
        return self.size


































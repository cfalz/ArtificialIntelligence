""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Author: Cody Falzone
#SID: 860929046
#CS170 Winter 17
#Project 1 - A* Search

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import numpy as np

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
    
    """ This is the defualt constructor for the Puzzle Problem.
     It allows you to choose and size and the operators are in reference
     to moving the blank in the puzzle. """

    def __init__( self, initial_state, goal_state, size ):
            super(PuzzleProblem, self).__init__(initial_state, goal_state)
            self.size = size
            self.operators = ["move_left", "move_right", "move_up", "move_down"]

            self.rows = len(initial_state)
            self.columns = len(initial_state[0])

            """Corner Indexes"""
            self.top_left_corner = (0,0)
            self.top_right_corner = (0,self.columns-1)
            self.bottom_left_corner = (self.rows-1,0)
            self.bottom_right_corner = (self.rows-1,self.columns-1)

            """Edge Lists"""
            self.bottom_edge = []
            self.right_edge = []
            self.left_edge = []
            self.top_edge = []
            for i in range(0,self.columns):
                self.top_edge.append((0,i))
                self.bottom_edge.append((self.rows-1,i))
                self.left_edge.append((i,0))
                self.right_edge.append((i,self.columns-1))

            
            self.edges = [self.bottom_edge, self.top_edge, self.left_edge, self.right_edge]
                
            self.corners = [self.top_left_corner, self.top_right_corner, self.bottom_left_corner, self.bottom_right_corner]

            for edge in self.edges:
                for corner in self.corners:
                    if corner in edge:
                        edge.remove(corner)


    def get_operators( self, state ):
        possible_moves = []
        blank_index = np.where(state == 0)
        if(self.is_a_corner(blank_index)):
            if(blank_index == self.top_left_corner):
                possible_moves.append(self.operators[3])
                possible_moves.append(self.operators[1])
            elif(blank_index == self.top_right_corner):
                possible_moves.append(self.operators[3])
                possible_moves.append(self.operators[0])
            elif(blank_index == self.bottom_left_corner):
                possible_moves.append(self.operators[2])
                possible_moves.append(self.operators[1])
            else:
                possible_moves.append(self.operators[2])
                possible_moves.append(self.operators[0])
        elif(self.on_an_edge(blank_index)):
            if(blank_index in self.top_edge):
                possible_moves = self.operators
                possible_moves.remove("move_up")
            elif(blank_index in self.left_edge):
                possible_moves = self.operators
                possible_moves.remove("move_left")
            elif(blank_index in self.right_edge):
                possible_moves = self.operators
                possible_moves.remove("move_right")
            else:
                possible_moves = self.operators
                possible_moves.remove("move_down")
        else:
            possible_moves = self.operators 

        return possible_moves
    
    """ Determine the state that results from a given operator. """
    def evaluate(self, state, operator):
        i,j = np.where(state == 0)
        m = state
        if(operator == self.operators[0]):
            swap_value = m[i,j-1]
            m[i,j -1] = 0
            m[i,j] = swap_value 
        elif(operator == self.operators[1]):
            swap_value = m[i,j+1]
            m[i,j+1] = 0
            m[i,j] = swap_value 
        elif(operator == self.operators[2]):
            swap_value = m[i-1,j]
            m[i-1,j] = 0
            m[i,j] = swap_value 
        elif(operator == self.operators[3]):
            swap_value = m[i+1,j]
            m[i+1,j] = 0
            m[i,j] = swap_value 

        return m



    """ Accessor for the puzzle's size. """
    def size(self):
        return self.size

    def on_an_edge(self, blank_index):
        for edge_list in self.edges:
            if blank_index in edge_list:
                return True
        return False

    def is_a_corner(self, blank_index):
        return blank_index in self.corners
            
        











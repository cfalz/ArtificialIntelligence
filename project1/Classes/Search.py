"""
    Author: Cody Falzone
    SID: 860929046
    CS170 Winter 17
    Project 1 - A* Search

"""
import numpy as np
from Node import *
#from Problem import *

############################################################################
#                                                                          #
#    Classes for a Search Algorithms.                                      # 
#    Input: initial_state : The initial state of the problem.              #
#           goal_state : The goal state of the problem.                    #
#                                                                          #
############################################################################


class Search(object):

    def __init__( self, problem):
        self.problem = problem
        self.container = [] 
        self.explored = []

    def search(self):
        raise NotImplementedError

    def get_node(self, state):
        for node in container:
            if node.state == state:
                return node

    def not_in_container(self,state):
        for node in self.container:
            if np.array_equal(state,node.state):
                return False
        return True

    def not_in_explored(self,state):
        for explored_state in self.explored:
            if np.array_equal(explored_state,state):
                return False
        return True


class UniformCostSearch(Search):
    
    """ This is the defualt constructor for the Search. """
    def __init__(self, problem):
            super(UniformCostSearch, self).__init__(problem)

    def get_path_cost(self, node):
        return node.path_cost

    def search(self):
        node = Node(self.problem.initial_state, 0) 
        self.container.append(node)
        while self.container:
            self.container = sorted(self.container, key = self.get_path_cost)
            current_node = self.container.pop(0)
            if np.array_equal(current_node.state,self.problem.goal_state):
                return current_node
            self.explored.append(current_node.state)
            new_nodes = current_node.explore(self.problem)
            for new_node in new_nodes:
                if self.not_in_container(new_node.state) and self.not_in_explored(new_node.state): 
                    self.container.append(new_node)
                elif not self.not_in_container(new_node) and new_node.path_cost < self.get_node(new_node.state).path_cost:
                    self.container.remove(self.get_node(new_node.state))
                    self.container.append(new_node)


class AstarMisplacedTileSearch(Search):
    
    def __init__( self, problem):
            super(AstarMisplacedTileSearch, self).__init__(problem)


    def get_total_cost(self, node):
        return node.total_cost_MT

    def search(self):
        node = Node(self.problem.initial_state, 0) 
        self.container.append(node)
        while self.container:
            self.container = sorted(self.container, key = self.get_total_cost)
            current_node = self.container.pop(0)
            if np.array_equal(current_node.state,self.problem.goal_state):
                return current_node
            self.explored.append(current_node.state)
            new_nodes = current_node.explore(self.problem)
            for new_node in new_nodes:
                if self.not_in_container(new_node.state) and self.not_in_explored(new_node.state): 
                    self.container.append(new_node)
                elif not self.not_in_container(new_node) and new_node.total_cost_MT < self.get_node(new_node.state).total_cost_MT:
                    self.container.remove(self.get_node(new_node.state))
                    self.container.append(new_node)


class AstarManhattanDistanceSearch(Search):

    def __init__( self, problem ):
            super(AstarManhattanDistanceSearch, self).__init__(problem)

    def get_node(self, state):
        for node in container:
            if node.state == state:
                return node

    def get_total_cost(self, node):
        return node.total_cost_MT

    def search(self):
        node = Node(self.problem.initial_state, 0) 
        self.container.append(node)
        while self.container:
            self.container = sorted(self.container, key = self.get_total_cost)
            current_node = self.container.pop(0)
            if np.array_equal(current_node.state,self.problem.goal_state):
                return current_node
            self.explored.append(current_node.state)
            new_nodes = current_node.explore(self.problem)
            for new_node in new_nodes:
                if self.not_in_container(new_node.state) and self.not_in_explored(new_node.state): 
                    self.container.append(new_node)
                elif not self.not_in_container(new_node) and new_node.total_cost_MD < self.get_node(new_node.state).total_cost_MD:
                    self.container.remove(self.get_node(new_node.state))
                    self.container.append(new_node)





"""
    Author: Cody Falzone
    SID: 860929046
    CS170 Winter 17
    Project 1 - A* Search

"""
import numpy as np
import bisect
from Node import *

############################################################################
#                                                                          #
#    Classes for a Search Algorithms.                                      # 
#    Input: initial_state : The initial state of the problem.              #
#           goal_state : The goal state of the problem.                    #
#                                                                          #
############################################################################

PRINTDEBUG = 0

class Search(object):

    """ This is the defualt constructor for the Search. """
    def __init__( self, problem):
        self.problem = problem
        self.container = [] 
        self.explored = []
        self.maxfrontiersize = 0;

    """ The function that is called to start the search. """
    def search(self):
        raise NotImplementedError

    def get_node(self, state):
        for node in self.container:
            if np.array_equal(node.state,state):
                return node
        raise ValueError('State, ', state , 'not found in container.')

    def not_in_container(self,state):
        for node in self.container:
            if np.array_equal(state,node.state):
                return False
        return True

    def in_container(self,state):
        for node in self.container:
            if np.array_equal(state,node.state):
                return True
        return False

    """ Inserts a node into the frontier in the proper place maintaining minimum values first based on the cost function f(n). """ 
    def node_insert(self, x, lo=0, hi=None):
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(self.container)
        while lo < hi:
            mid = (lo+hi)//2
            if self.get_total_cost(self.container[mid]) < self.get_total_cost(x): 
                lo = mid+1
            else: hi = mid
        self.container.insert(lo,x)

    def not_in_explored(self,state):
        for explored_state in self.explored:
            if np.array_equal(explored_state,state):
                return False
        return True

    def in_explored(self,state):
        for explored_state in self.explored:
            if np.array_equal(explored_state,state):
                return True
        return False




class UniformCostSearch(Search):
    
    def __init__(self, problem):
            super(UniformCostSearch, self).__init__(problem)

    def get_total_cost(self, node):
        return node.path_cost

    def search(self):
        node = Node(self.problem.initial_state, 0) 
        self.node_insert(node)
        while self.container:
            if len(self.container) > self.maxfrontiersize:
                self.maxfrontiersize = len(self.container)
            current_node = self.container.pop(0)
            if PRINTDEBUG:
                print "Expanding Node \n" , current_node.state , "\n At Depth ", current_node.path_cost, "With a g(n) " , current_node.path_cost
                print "The Amount Of Nodes Explored: ", len(self.explored)
                print "The Amount Of Nodes In Frontier: ", len(self.container)
                print "\n"
            if self.problem.is_goal(current_node.state):
                return current_node
            self.explored.append(current_node.state)
            new_nodes = current_node.explore(self.problem)
            for new_node in new_nodes:
                if PRINTDEBUG:
                    print "The New Node Is: \n", new_node.state , "At Depth : ", current_node.path_cost
                if self.not_in_container(new_node.state) and self.not_in_explored(new_node.state): 
                    if PRINTDEBUG:
                        print "Its not in the container and we have not explored this state, Appending to Container." 
                        print "\n"
                    self.node_insert(new_node)
                elif self.in_container(new_node) and new_node.path_cost < self.get_node(new_node.state).path_cost:
                    if PRINTDEBUG:
                        print "Its in the container and has a cheaper cost! Removing the other one and Appending to Container." 
                        print "\n"
                    self.container.remove(self.get_node(new_node.state))
                    self.node_insert(new_node)
                


class AstarMisplacedTileSearch(Search):
    
    def __init__( self, problem):
            super(AstarMisplacedTileSearch, self).__init__(problem)

    def get_total_cost(self, node):
        return node.total_cost_MT

    def print_costs(self):
        print [node.total_cost_MT for node in self.container]

    def search(self):
        node = Node(self.problem.initial_state, 0) 
        self.node_insert(node)
        while self.container:
            if len(self.container) > self.maxfrontiersize:
                self.maxfrontiersize = len(self.container)
            if PRINTDEBUG:
                print "Printing the Cost List: ", self.print_costs()
            current_node = self.container.pop(0)
            if PRINTDEBUG:
                print "The Current Node Is: \n", current_node.state , "\n At Depth : ", current_node.path_cost, "With a cost ", self.get_total_cost(current_node)
                print "The Amount Of Nodes Explored: ", len(self.explored)
                print "The Amount Of Nodes In Frontier: ", len(self.container)
                print "\n"

            if self.problem.is_goal(current_node.state):
                return current_node
            self.explored.append(current_node.state)
            new_nodes = current_node.explore(self.problem)
            for new_node in new_nodes:
                if PRINTDEBUG:
                    print "Printing New Node with a cost of: ", self.get_total_cost(new_node) ,"\n"
                    print "Printing New Node with a MT cost of: ", new_node.cost_to_goal_MT ,"\n"
                    print new_node.state , "\n"

                if (self.not_in_container(new_node.state) and (self.not_in_explored(new_node.state))): 
                    if PRINTDEBUG:
                        print "Its not in the container and we have not explored this state, Appending to Container." 
                        print "\n"
                    self.node_insert(new_node)
                elif (self.in_container(new_node.state) and (self.get_total_cost(new_node) < self.get_total_cost(self.get_node(new_node.state)))):
                    if PRINTDEBUG:
                        print "Its in the container and has a cheaper cost! Removing the other one and Appending to Container." 
                        print "\n"
                    self.container.remove(self.get_node(new_node.state))
                    self.node_insert(new_node)


class AstarManhattanDistanceSearch(Search):

    def __init__( self, problem ):
            super(AstarManhattanDistanceSearch, self).__init__(problem)

    def get_total_cost(self, node):
        return int(node.total_cost_MD)

    def print_costs(self):
        print [node.total_cost_MD for node in self.container]


    def search(self):
        node = Node(self.problem.initial_state, 0) 
        self.node_insert(node)
        while self.container:
            current_node = self.container.pop(0)
            if len(self.container) > self.maxfrontiersize:
                self.maxfrontiersize = len(self.container)

            if PRINTDEBUG:
                print "The Current Node Is: \n", current_node.state , "\n At Depth : ", current_node.path_cost , " And Cost: ", self.get_total_cost(current_node)
                print "The Amount Of Nodes Explored: ", len(self.explored)
                print "The Amount Of Nodes In Frontier: ", len(self.container)
                print "\n"

            if self.problem.is_goal(current_node.state):
                return current_node
            self.explored.append(current_node.state)
            new_nodes = current_node.explore(self.problem)
            for new_node in new_nodes:
                if PRINTDEBUG:
                    print "The New Node Is: \n", new_node.state , "\n With Cost : ", self.get_total_cost(new_node)
                    print "MD Cost: " , new_node.cost_to_goal_MD
                    print "Path Cost: " , new_node.path_cost
                if self.not_in_container(new_node.state) and self.not_in_explored(new_node.state): 
                    if PRINTDEBUG:
                        print "Its not in the container and we have not explored this state, Appending to Container." 
                        print "\n"
                    self.node_insert(new_node)
                elif (self.in_container(new_node.state) and (self.get_total_cost(new_node) < self.get_node(new_node.state).total_cost_MD)):
                    if PRINTDEBUG:
                        print "Its in the container and has a cheaper cost! Removing the other one and Appending to Container." 
                        print "\n"
                        n = self.get_node(new_node.state)
                        print "Removing \n" , n.state ," \n With Cost: ", self.get_total_cost(n)
                    self.container.remove(self.get_node(new_node.state))
                    if PRINTDEBUG:
                        print "Length Of Container after removal is: " , len(self.container)
                    self.node_insert(new_node)
                else:
                    if PRINTDEBUG:
                        if self.in_container(new_node.state):
                            print "Its already in the container, this has a higher cost of ", self.get_total_cost(new_node), "." 
                            print "Cost of identical state \n", self.get_node(new_node.state), "\n in container: " , self.get_node(new_node.state).total_cost_MD 
                        else:
                            print "It Appears This Node has already been Explored. Checking if in the explored list....." , self.in_explored(new_node.state)


                if PRINTDEBUG:
                    "\n"
                    print"Size of Container: ", len(self.container)
                    print"Size of Explored: ", len(self.explored)
                    raw_input()




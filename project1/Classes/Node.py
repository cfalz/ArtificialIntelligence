import copy

""" This is a Node in the Tree that holds information about a specific State of a puzzle; 
        Including the path cost to the state, the state which it came from (parent node), 
        and the current state of the puzzle (where the peices are on the board.)"""

class Node:

    def __init__(self, state, path_cost, cost_to_goal_MT = 0, parent = None):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.cost_to_goal_MT = cost_to_goal_MT 
        self.total_cost_MT = path_cost + cost_to_goal_MT
        self.path = []

    """ Create a new node in the tree given the current state of the puzzle and a move(operator). 
        First we get the new state by calling the problem's evaluate function. Then we create a
        new Node by giving it the new information. """
    def make_move(self, problem, operator):
       new_state = problem.evaluate(self.state,operator)
       new_path_cost = self.path_cost + problem.step_cost
       new_cost_to_goal_MT = self.get_MT_cost() 
       new_node = Node(new_state,new_path_cost,new_cost_to_goal_MT,self)
       new_node.path = copy.deepcopy(self.path)
       new_node.path.append(operator)
       return new_node

    """ Given a state of the puzzle, create all new nodes that result from all possible moves. """
    def explore(self, problem):
        children = []
        for operator in problem.get_operators(self.state):
            children.append(self.make_move(problem,operator))
        return children

    def get_path_cost(self):
        return self.path_cost

    def get_MT_cost(self):
        tile_number = 1
        cost = 0
        for row in self.state:
            for column in row:
                if column != tile_number and column != 0:
                    cost+=1
                tile_number += 1
                if tile_number == self.state.size:
                    tile_number = 0

        return cost
        
    def get_MD_cost(self):
        return 0

    def print_stats(self):
        print "I Am: ", self , "Greetings from Memory!"
        print "My State: "
        print self.state
        print "My Parent Is: ", self.parent
        print "My Path_Cost Is: ", self.path_cost





class Node:

    def __init__(self, state, cost, parent = None):
        self.state = state
        self.parent = parent
        self.path_cost = cost

    def child(self, problem, operator):
       new_state = problem.evaluate(self.state,operator)
       return Node(new_state,self.path_cost+1,self)

    def explore(self, problem):
        children = []
        for operator in problem.get_operators(self.state):
            print operator
            print("Adding, ", self.child(problem,operator).state , "to the Children.")
            children.append(self.child(problem,operator))
        return children


    def print_stats(self):
        print "State: "
        print self.state
        print "Parent: ", self.parent
        print "Path_Cost: ", self.path_cost


#monte carlo tree search for checkers ai
# good pseudocode here: https://www.geeksforgeeks.org/ml-monte-carlo-tree-search-mcts/
#algorithm:
# 1. tree traversal to a leaf node.  go to child that maximizes UCB1(Si) 
# 2. node expansion.  add more nodes to the tree using possible game actions
# 3. rollout.  random simulation of the game to a terminal state.  get some resulting value (here probably just 1 or 0?)
# 4. backpropagation. add the rollout value to it's parent nodes up to root
# 
# after x time or number of iterations, take the action that results in a higher average value
# UCB1(Si) = v/ni + c * sqrt(ln(n0)/ni) = avg score at that state + exploration parameter (probably just 2) * sqrt((ln(total number of simulations)/number of rollouts for this state)

#imports
import math

#state node class
class Node:
    def __init__(self):
        self.move = None #2 element array holding the move that leads to this state
        self.t = 0 #total score
        self.n = 0 #number of times visited
        self.parent = None
        self.children = []

#main loop (currently pseudocode)
def mcts(root):
    simulation_limit = 10
    while(simulation_limit >= 0):
        leaf = traverse(root)
        #expansion happens in traverse.  easier to manage when to expand
        simulation = rollout(leaf) #returns result of simulation
        backpropagate(leaf, simulation)
        simulation_limit -= 1
        
#traverse to a leaf using ubc1
def traverse(current):
    while(len(current.children) != 0):
        current = next_child(current)
    
    #if the node has been visited, expand
    if(current.n != 0):
        current = expand(current)
    
    return current

#expansion.  get possible actions from game.  create new child nodes with resulting states.  return first new child node
def expand(current):
    return current


#rollout.  simulate a random game.  stop at a terminal node.  return result of terminal node
def rollout(current):
    return current

#backpropagation.  
def backpropagate(current, value):
    return value

#find child with the highest ubc1
def next_child(parent):
    #should not hit this if statement.  add better error checking
    if(len(parent.children) == 0):
        return None
    highest = -1
    next_child = None
    for n in parent.children:
        n_val = ubc1(n.t, n.n, root.n)
        if ( n_val > highest):
            highest = n_val
            next_child = n
    return n

# basic ubc1 implementation
def ubc1(v, ni, n0):
    avg_score = v/ni
    expl_constant = 2
    if(ni == 0):
        result = 100000 #avoiding division by zero
    else: 
        result = avg_score + expl_constant * math.sqrt((math.log(n0)/ni))
    return result

#create root
root = Node()
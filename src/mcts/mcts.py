#monte carlo tree search for checkers ai
# good pseudocode here: https://www.geeksforgeeks.org/ml-monte-carlo-tree-search-mcts/
#algorithm:
# 1. tree traversal to a leaf node.  go to child that maximizes UCB1(Si) 
# 2. node expansion.  add more nodes to the tree using possible game actions
# 3. rollout.  random simulation of the game to a terminal state.  get some resulting value (here probably just 1 or 0?)
# 4. backpropagation. add the rollout value to it's parent nodes up to root
# 
# after x time or number of iterations, take the action that results in a higher average value
# UCB1(Si) = v/ni + c * sqrt(ln(n0)/ni) = avg score at that state + exploration parameter (probably just 2) * sqrt((ln(total number of rollouts)/number of rollouts for this state)

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


# basic ubc1 implementation
def ubc1(v, ni, n0):
    avg_score = v/ni
    expl_constant = 2
    result = avg_score + expl_constant * math.sqrt((math.log(n0)/ni))
    return result

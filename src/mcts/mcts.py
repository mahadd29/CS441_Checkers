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
from checkers.board import Board

#state node class
class MCTSNode:
    def __init__(self, board, action):
        self.action = action # 2 element array holding the move that leads to this state
        self.board = board # A board representing the current state before applying action
        self.t = 0 #total score
        self.n = 0 #number of times visited
        self.parent = None
        self.children = []

# main loop (currently pseudocode)
def mcts(root):
    simulation_limit = 10
    while(simulation_limit >= 0):
        leaf = traverse(root)
        if leaf.n != 0:
            leaf = expand(leaf)
        simulation_result = rollout(leaf)            
        backpropagate(leaf, simulation_result)
        simulation_limit -= 1

#find child with the highest ubc1
def next_child(parent):
    #should not hit this if statement.  add better error checking
    if(len(parent.children) == 0):
        return None
    highest = -1
    next_child = None
    for n in parent.children:
        n_val = ucb1(n)
        if ( n_val > highest):
            highest = n_val
            next_child = n
    return next_child

# Traverse to a leaf using ubc1
# Parameters:
#   state - a current state to traverse from
# Return values:
#   state - returns the current node if it has no children to traverse to
#   best child - returns the child with the highest UCB1 score
def traverse(state):
    while(len(state.children) != 0):
        state = next_child(state)
    return state

def apply_action(state, action):
    return 

# Expansion
# Steps:
#   - Get possible actions from game
#   - Create new child nodes with resulting states.  return first new child node
# Parameters:
#   s - the state to expand
# Return values:
#   child - the first child generated from possible actions taken by the agent
def expand(state):
    possible_moves = state.board.get_possible_moves()
    for move in possible_moves:
        result_board = state.board.create_new_board_from_move(move)
        child = MCTSNode(result_board, move)
        child.parent = state
        state.children.append(child)
    return state.children[0] if len(state.children) > 0 else None

# Rollout
# Steps:
#   - Simulate a random game
#   - Stop at a terminal node
#   - Return result of terminal node
# Parameters:
#   state - the current game state
# Return value:
#   state - state after applying the rollout
def rollout(state):
    return 1

#backpropagation. traverse back up the tree.  increment times visited.  add rollout result to total result 
def backpropagate(state, value):
    parent = state.parent
    state.n += 1
    while(parent): #make sure this is correct and can get to root
        parent.n += 1
        parent.t += value
        parent = parent.parent
    return value

# Basic ucb1 implementation
# Parameters:
#   s - A game state to be evaluated
# Return values:
#   result - the UCB1 score for the state s
def ucb1(s):
    if s.n == 0:
        return float("inf")
    
    total_simulations = mcts_root.n if mcts_root.n > 0 else 1
    num_visited = s.n
    avg_score = s.t / num_visited
    expl_constant = 2
    
    result = avg_score + expl_constant * math.sqrt((math.log(total_simulations)/num_visited))
    return result

# create root and start
mcts_root = MCTSNode(Board(), None)
#monte carlo tree search for checkers ai

#algorithm:
# 1. tree traversal to a leaf node.  go to child that maximizes UCB1(Si) 
# 2. node expansion.  add more nodes to the tree using possible game actions
# 3. rollout.  random simulation of the game to a terminal state.  get some resulting value (here probably just 1 or 0?)
# 4. backpropagation. add the rollout value to it's parent nodes up to root
# 
# after x time or number of iterations, take the action that results in a higher average value
# UCB1(Si) = v/ni + c * sqrt(ln(n0)/ni) = avg score at that state + exploration parameter (probably just 2) * sqrt((ln(total number of rollouts)/number of rollouts for this state)
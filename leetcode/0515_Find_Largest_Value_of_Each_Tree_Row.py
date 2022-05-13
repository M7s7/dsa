# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

import collections
from math import inf

# Approach: BFS. Every loop through a level, we store the maximum value (initiating the variable at -inf at the start).
    # Time Complexity: O(N) // Space Complexity: O(N)
def largestValues(self, root):
    queue = collections.deque()
    queue.append(root)
    
    ans = []
    
    while queue:
        # Create a variable to store the max value - initiate at -inf so no false positives
        biggest = -inf
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if node:
                # If valid node, check if it is the largest value in the level
                biggest = max(biggest, node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        # If there are no valid nodes (eg. If the level only has Nones), do not append the max. Otherwise, append
        if biggest != -inf:
            ans.append(biggest)
        
    return ans
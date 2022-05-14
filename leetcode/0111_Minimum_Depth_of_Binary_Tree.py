# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

import collections

# APPROACH 1: BFS
    # Standard way - using for-loop to scan each level. Keep a counter of what level we are on.
# Time Complexity: O(N) // Space Complexity: O(N)

def minDepth(self, root):
    # Return 0 if there are no nodes
    if not root: 
        return 0
    
    queue = collections.deque()
    queue.append(root)
    level = 0
    
    while queue:
        # Add one level per loop
        level += 1
        level_size = len(queue)          
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # Check if the node is a leaf. If so, return our level
            if node: 
                if not node.left and not node.right:
                    return level
                
                queue.append(node.left)
                queue.append(node.right)

    
    # Using Tuples: 
    ## No need for for-loop - instead, each entry in the queue stores a NODE and the LEVEL that the node is on
def minDepth(self, root):
    if not root: 
        return 0
    
    queue = collections.deque()
    # Our queue holds TUPLES instead of just a node. It has the node and the level.
    queue.append([root, 1])
    
    # Notice that there is no for-loop or len(queue) - not needed because we are storing the level of each node. 
    while queue: 
        # Remember to store both variables seperately from the tuple. 
        node, level = queue.popleft()
        if node: 
            if not node.left and not node.right:
                return level

            # When appending a new node, remember to append it as a tuple (with an increasing level)
            queue.append([node.left, level+1])
            queue.append([node.right, level+1])
        
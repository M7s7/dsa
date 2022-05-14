# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

import collections

# Approach 1: BFS Solution
    # Time Complexity: O(N) // Space Complexity: O(N)

    # Standard approach - check both nodes for existence
def maxDepth(self, root):
    if not root:
        return 0
    
    queue = collections.deque()
    queue.append(root)
    level = 0
    
    while queue:
        level += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return level

    # Tuple approach to store level
def maxDepth(self, root):
    if not root:
        return 0
    
    queue = collections.deque()
    queue.append([root, 1])
    max_level = 0
    
    while queue:
        node, level = queue.popleft()
        
        if node:
            max_level = max(max_level, level)
            
            queue.append([node.left, level+1])
            queue.append([node.right, level+1])
    
    return max_level
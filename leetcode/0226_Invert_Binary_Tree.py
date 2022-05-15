# Given the root of a binary tree, invert the tree, and return its root.

# BFS: Simply go through each node of the tree, swapping the left branch with the right one. 
    # Time Complexity: O(N) // Space Complexity: O(N)
import collections

def invertTree(self, root):
    if not root:
        return root
    
    queue = collections.deque()
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        
        if node:
            temp = node.left
            node.left = node.right
            node.right = temp
        
            queue.append(node.left)
            queue.append(node.right)
    return root
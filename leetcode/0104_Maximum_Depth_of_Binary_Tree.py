# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

import collections
# Approach 1: BFS Solution - store level variable and return it
    # Time Complexity: O(N)
    # Space Complexity: O(N)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
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

# Alternatively (and preferred) BFS: Tuple approach to store level
    # Time Complexity: O(N)
    # Space Complexity: O(N) - max queue size is width of tree (N/2)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque()
        depth = 1
        queue.append((root, depth))
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):     
                node, depth = queue.popleft()
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))
        
        return depth 


# DFS solution - return local depth of each node. 
    # Time Complexity: O(N)
    # Space Complexity: O(N) - max depth of the tree (if it is just a linked list)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
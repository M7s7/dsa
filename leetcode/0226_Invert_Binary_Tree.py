# Given the root of a binary tree, invert the tree, and return its root.

# BFS: Simply go through each node of the tree, swapping the left branch with the right one. 
    # Time Complexity: O(N) 
    # Space Complexity: O(N)
import collections

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                node.right, node.left = node.left, node.right
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return root


# DFS implementation.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Go to leaf node (leaf nodes can still swap their none nodes)
        if not root:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        
        return root
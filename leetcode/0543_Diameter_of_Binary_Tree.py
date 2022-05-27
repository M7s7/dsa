# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Approach: DFS recursively - when calling each node, we:
    # 1: Determine the longest path for the parent node
    # 2: Determine the local maximum diameter
    # Time Complexity: O(N), touching each node once // Space Complexity: O(N) for recursive stack
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        # Class level variable
        self.diameter = 0
        
        # If the node does not exist, then there is no pathlength to return for the next node.
        def dfs(node):
            if not node:
                return 0
            
            # If we are at a local root node, we should return the longest right and left nodes)
            longestLeft = dfs(node.left)
            longestRight = dfs(node.right)
            
            # Check current node and its diameter - if bigger than current max, we should store it
            self.diameter = max(self.diameter, longestLeft + longestRight)
            
            # For each node, we finally want to return the longest root-to-node path. The parent node will consider this length when choosing a max. 
            # We add 1 to the returned path, as this will count the parent to current node path length
            return 1 + max(longestLeft, longestRight)
        
        dfs(root)
        
        return self.diameter


# Approach modified, where we return the height. 
    # This approach is exactly the same, except we accurately return the 'height' of each node 
    # Note that the longest path of a given node is the 'height' of the node from the 
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0
        
        def dfs(node):
            # The height of an empty tree is -1; the height of a single node is 0. 
            if not node:
                return -1
            
            longestLeft = dfs(node.left)
            longestRight = dfs(node.right)
            
            # Add the two heights of the longest children paths. +2 for the left and right path from the current node. 
            self.diameter = max(self.diameter, longestLeft + longestRight + 2)
            
            return 1 + max(longestLeft, longestRight)
        
        dfs(root)
        
        return self.diameter
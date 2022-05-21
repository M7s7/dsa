# Given the root of a binary tree and an integer targetSum, return true if:
##  the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Approach: Recursive DFS
    # Time Complexity: O(N) // Space Complexity: O(N) (height of tree)
def hasPathSum(self, root, targetSum): 
    # Helper function - runs DFS through every node in the tree
    def dfs(node, curSum):
        # Handles cases where we call dfs on non-existent nodes (eg. if node.left does not exist)
        if not node:
            return False
        
        # Add the node to the currentSum
        curSum += node.val            
    
        # Base case is if we are at a leaf node
        if not node.left and not node.right:
            # Return true if they equal; return false if not, culling the path
            return curSum == targetSum
        
        # Recursive case: Call dfs on BOTH the left and right children nodes, passing through the current sum
            # We use or because if either of them equal targetSum, we want to return true
        return dfs(node.left, curSum) or dfs(node.right, curSum) 
    
    return dfs(root, 0)
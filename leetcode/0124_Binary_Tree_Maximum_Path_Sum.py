# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# Note that the path does not need to go through the root.
import math

# Approach 1: 'Gains' of each node
    # Travel to each node and find:
        # 1. The largest pathsum through the node (by adding the max gains of each path, plus the current node)
        # 2. The max gain that we can get through this node. 
    # Time complexity: O(N) // Space Complexity: O(N)
class Solution:
    def maxPathSum(self, root) -> int:
        self.maxSum = -math.inf
        
        def dfs(node):
            # Basecase: 0 gain if the parent node is a leaf node (child is null)
            if not node:
                return 0
            
            # At each node, calculate the maximum left and right gains from every descendant  path. If the paths are negative only, return 0
            leftGain = max(dfs(node.left), 0)
            rightGain = max(dfs(node.right), 0)
            
            # Calculating maxPath. Remember to add the node.val to our gains.
            self.maxSum = max(self.maxSum, leftGain + rightGain + node.val)
            
            # Returning the max-path to use for our parent node. Remember to attach our node.val
            return max(leftGain, rightGain) + node.val
        
        dfs(root)
        
        return self.maxSum


# Approach 2: My first implementation - Pathsum of each node 
    # We find the maximum pathsum for each node and return it for the next recursive call.
            # Travel to each node and find:
            # 1. The largest pathSum through the node
            # 2. The pathSum we should return to the parent node. 
    # if the path is negative, we will not want to return the sum (instead, we will return 0)
    # Time Complexity: O(N) // Space Complexity: O(N) height of tree
class Solution:
    def maxPathSum(self, root) -> int:
        # Class level variable - initated in negative inf, not 0 (so no false positives)
        self.maxSum = -math.inf

        def dfs(node, pathSum):
            # Basecase: If we are past a leaf node, return 0 for the leaf-node to initiate its pathSum
            if not node:
                return 0
            
            # Call dfs on each left and right node recursively
            leftSum = dfs(node.left, pathSum)
            rightSum = dfs(node.right, pathSum)
            
            # Updating answer - store the old maxSum or the new maxSum (highest paths + current node value)
            self.maxSum = max(self.maxSum, leftSum + rightSum + node.val)
            
            # To the parent node's dfs call, return the longest path. If both paths are negative, return 0
                # Return 0 to indicate we cut off both paths as they are negative
            return max(max(leftSum, rightSum) + node.val, 0)
        
        dfs(root, 0)
        
        return self.maxSum
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
# Each path should be returned as a list of the node values, not node references.

# Approach: recursive DFS, using MANIPULATION OF THE ORIGINAL PATH.
    # Since the original path is being manipulated, we need to 'de-manipulate' it after the branches are searched by backtracking.
    # Time Complexity: O(N^2) at worst. O(N) for the DFS * O(N) to copy the list of node values // Space Complexity: O(N) for height (excluding the answer output)
def pathSum(self, root, targetSum):
    # Helper function
    def dfs(node, currentSum, path):
        if not node:
            return None
        
        # Add new node to the path, and add to running total
        path.append(node.val)
        currentSum += node.val
        
        # Base case - leaf node (because root-to-leaf paths)
        if not node.left and not node.right:
            if currentSum == targetSum:
                # A copy of the path must be appended. This is because 'path' is passed in as a reference, and will be modified by path.pop()
                ans.append(path.copy())
        
        # Recursive Case
        else:
            dfs(node.left, currentSum, path)
            dfs(node.right, currentSum, path)
            
        # Backtracking: pop off all the nodes as the recursive calls resolve, preventing nodes from different branches being counted
        # Note that since the path.pop is at the end, we will only backtrack AFTER all the deeper paths have been explored (ie. the recursive cases have been resolved)
        path.pop()

    ans = []    
    dfs(root, 0, [])
    return ans


# Approach: recursive DFS, by CREATING NEW PATHS
    # Less efficient, as creating new paths are costly operations. However, no need to backtrack. 
    # Time Complexity: O(N^2) at worst. O(N) for the DFS * O(N) to copy the list of node values // Space Complexity: O(N) for height (excluding the answer output)
def pathSum(self, root, targetSum):
    def dfs(node, currentSum, path):
    if not node:
        return None
    
    # Add new node to the path, and add to running total
    currentSum += node.val
    
    # Base case - leaf node (because root-to-leaf paths)
    if not node.left and not node.right:
        if currentSum == targetSum:
            # New path is created and appended, and the old reference path is not modified. 
            ans.append(path + [node.val])
    
    # Recursive Case
    else:
        dfs(node.left, currentSum, path + [node.val])
        dfs(node.right, currentSum, path + [node.val])
    
    ans = []
    dfs(root, 0, [])
    return ans
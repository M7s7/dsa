# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Memoization Approach: DFS with caching. 
    # We cache the value of the above paths to our current node. 
    # Notice that by subtracting our old paths from our current pathsum, we get additional path sums which do not originate from the root node.
    # Thus, if we find a current sum that subtracts with one of our old paths to give us the target, we have found a valid path
    # Time Complexity: O(N) given a single traversal// Space Complexity: O(N), N for hashmap + N for recursive call
class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        # Only one dfs needed to be called. 
        def dfs(node, currSum, cache):
            if not node:
                return  
            
            # Add to our current path sum
            currSum += node.val
            
            # We get obtain new pathsums that do not originate from the node: currSum - oldPath will return a new non-root pathsum of the nodes between the ends of these paths. If this new pathsum is equal to the targetSum, we have a valid new path.
            ## Thus, if we find an oldPathSum which fulfils these conditions, we will have found a valid path. 
            oldPathSum = currSum - targetSum
            
            # Check our hashmap to see if we have such a pathsum (or several). If so, we have new paths equal to the number of old pathsums - add the frequency of all the pathsums to our answer.
                # Note that the .get method will return how many such subpaths we have (if none, it will return 0)
            self.ans += cache.get(oldPathSum, 0)
            
            # Now, we store our currSum and store it as an oldPathSum for the next node. 
            cache[currSum] = cache.get(currSum, 0) + 1

            # DFS recursive call: Call the DFS on every node until we reach our leaf nodes.
            dfs(node.left, currSum, cache)
            dfs(node.right, currSum, cache)
            
            # Backtracking - remove oldpathsums when we move onto different paths (as these pathsums are no longer relevant)
            cache[currSum] -= 1
            
        # Global variable
        self.ans = 0
        
        # Hashmap created to hold our old pathsums. 
            # Note that we initiate our hashmap with an old-path of 0 with a frequency of 1. This handles root-to-node paths which are valid (as the currSum - targetSum for a valid root-to-node path would be 0)
            # Alternatively, we could just check the currSum every time to see if it equals the targetSum. 
        cache = {0:1}
        
        # recursive to get result
        dfs(root, 0, cache)
        return self.ans


# Naive Approach: Nested DFS. Two loops of dfs: Outer loop travels to each node. Inner loop traverses all the paths which originate from that node and sums them.
    # Time Complexity: O(N^2) for nested dfs // Space Complexity: O(N) (height of tree) for call stack, up to O(2N) for both recursive stacks
class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        # Declare a global variable that we can reference to within our functions (the variable is an object)
        self.ans = 0
        
        # Inner DFS: For the current node, call dfs and find the sum of every path from this node. 
        def allPaths(node, currSum):
            if not node:
                return
            
            currSum += node.val
            
            if currSum == targetSum: 
                self.ans += 1
            
            allPaths(node.left, currSum)
            allPaths(node.right, currSum)
        
        # Outer DFS: Traverse the tree and touch each node
        def allNodes(node):
            if not node:
                return 
            
            # For this node, check all the paths
            allPaths(node, 0)
            
            # Travel to all nodes
            allNodes(node.left)
            allNodes(node.right)
        
        # Driver code
        allNodes(root)
        return self.ans
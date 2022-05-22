# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# Return the total sum of all root-to-leaf numbers. 

# Approach 1: Recursive DFS. We store the number of the path, and when we get to the end we return it.
    # Time Complexity: O(N) // Space Complexity: O(N) (height of tree for call stack)

def sumNumbers(self, root):
    # Recursive DFS
    def dfs(node, num):
        # Edgecases - if we call node.right or node.left and it doesn't exist
        if not node:
            return 0
        
        # Add values. To create the number, we want to multiply the current number by 10 (shifting the places)
        num = num * 10 + node.val
        
        # If leaf node, we want to return the number
        if not node.left and not node.right:
            return num
        
        # For every node, we will return the sum of all the left and right paths below it.
        # Thus, at the root node, this will call dfs on EVERY PATH to the left and right. 
        return dfs(node.left, num) + dfs(node.right, num)
    
    return dfs(root, 0)

    # To understand the solution:
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7

    # Initially, we call the recursive function on the ROOT NODE. 
    # Line 24 calls dfs recursively on every RIGHT and LEFT node, if they exist.
    # When we reach a leaf node, we reach our base case (line 19) where num is returned. 
        # Note that num has been storing the values of each node through lines 16 and 24.
    # After the base-case resolves for both the left and right leaves of a node, the node returns the value of the sum of these numbers
        # Then, this node resolves.
    # After this, the parent node resolves, adding the left and right consolidated nodes.
    # This continues until we reach our root, where all the left paths and right paths are consolidated and added. 
    
    # Eg. Node 4 returns num = 124, and Node 5 returns num = 125
    # Then, the parent node 2 returns num = 249. Similarly, node 3 returns its children nodes (num = 136 + 137)
    # After nodes 2 and 3 resolve, 1 can resolve by adding nodes 2 and 3. 
        # Notice that nodes 2 and 3 return the sum of nodes 4, 5, 6 and 7. 
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# The answer should be returned as a list of strings, with an arrow seperating each value. 

# Recursive DFS approach, using string concatenation:
def binaryTreePaths(self, root):
    def dfs(node, path):
        # Handles empty root, also handles if only left or right node exists
        if not node:
            return
        
        path += str(node.val)
        
        # Base-case: Node is a leaf-node; we will add our completed path
        if not node.left and not node.right:
            # Note: No need to append a copy, as the path does not affect our traversal, and strings do not have a .copy method
            ans.append(path)
        
        else:
            # Answer requires arrows between node values
            path += "->"
            # Pass a copy of the current path while searching the next node
            dfs(node.left, path)
            dfs(node.right, path)
    
    ans = []
    # Call the helper function, passing a string as the path
    dfs(root, "")
    return ans
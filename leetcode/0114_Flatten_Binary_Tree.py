# Given the root of a binary tree, flatten the tree into a "linked list":
    # The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    # The "linked list" should be in the same order as a pre-order traversal of the binary tree.


# RECURSION: All these recursive solutions are:
    # Time Complexity: O(N)
    # Space Complexity: O(N)

# Backwards - Reverse pre-order traversal - nodes are added in backwards.
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.back = TreeNode(0, None, None)
        def dfs(root):
            if not root:
                return None
            
            dfs(root.right)
            dfs(root.left)
            
            root.right = self.back.right
            root.left = None
            self.back.right = root
        
        dfs(root)



# My ugly implementation: Pre-order traversal, changing our root every time we reach a new node
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.pre_root = TreeNode(0, left = None, right = root)
        
        def dfs(node):
            if not node:
                return

            r = node.right
            l = node.left

            self.pre_root.left = None
            self.pre_root.right = node
            self.pre_root = self.pre_root.right
            
            dfs(l)
            dfs(r)
        
        dfs(root)


# Pre-order traversal. Flatten left and attach to right.
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root):
            if not root:
                return None
            
            left_tail = dfs(root.left)
            right_tail = dfs(root.right)
            
            # If we have a left subtree, insert its flattened form into the right tree
            if root.left:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            
            # Return our tail to our function. If right tail exists, it will have our last node. If it doesn't exist, left tail. If neither exist, we are at the 'tail'
            return right_tail or left_tail or root
        dfs(root)
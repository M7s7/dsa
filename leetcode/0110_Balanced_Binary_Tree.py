# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
    # a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


# DFS standard. Go down the tree and check each node to see if the nodes are unbalanced. To compare, we need to calculate the height of each branch.
    # Time Complexity: O(N)
    # Space Complexity: O(N) - height of tree (linked list worst case)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:  
        def nodeHeight(root):
            if not root:
                return 0
            
            left_height = 1 + nodeHeight(root.left)
            right_height = 1 + nodeHeight(root.right)
            # This condition means that either a node deeper down our left or right branch was -1 (unbalanced), so we can continue to return this result
            if left_height == 0 or right_height == 0:
                return -1
            # Current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            # The height of our current node will be the larger of the two paths
            return max(left_height, right_height)
        # Function will return -1 if any node is unbalanced
        return nodeHeight(root) != -1


# DFS using a class level variable
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def nodeHeight(root):
            if not root:
                return 0
            left_height = nodeHeight(root.left) + 1
            right_height = nodeHeight(root.right) + 1
    
            if abs(left_height - right_height) > 1:
                self.ans = False    
            return max(left_height, right_height)

        nodeHeight(root)
        return self.ans
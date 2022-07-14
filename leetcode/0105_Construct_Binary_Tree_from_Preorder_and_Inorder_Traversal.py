# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Approach: Two important concepts with pre-order and in-order traversals which guide our approach:
    # 1: The first value in a pre-order traversal will be the ROOT node of the entire tree.
    # 2: An in-order traversal's values are 'ordered' in the array. For any root node's value, the left numbers are nodes on its left branch and the right numbers are on its right branch.

# Implementation 1: Basic recursion. Passes through sliced strings, so somewhat inefficient. 
    # Time Complexity: O(N^2) - Go through N nodes. Copying lists 4N times. index is a linear method as well (N). Thus, somewhere between N^2 and 5N^2.
    # Space Complexity: O(N^2) - Since we are using array slicing, we copy lists 4N times each loop (N loops).
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Leaf nodes will not have any nodes on its left or right. 
        if not inorder:
            return None
        
        root = TreeNode(preorder[0]) # Fact 1: Root node is always the first value traversed in pre-order
        mid = inorder.index(root.val) # Find the index of the root. As per fact 2, the in-order traversal will allow us to see how many nodes are on the left and right branches of any given root node. 
        
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid]) # Arguments: Left 'half' of preorder and post-order
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) # Arguments: Right 'half' of preorder and post-order
        
        return root

    # Further notes:
        # To find value of root nodes: Root node is always the first value of pre-order. 
            # For the left child, this will be index 1 of pre-order (as the 0th index was used by the parent).
            # For the right child, we need to skip to the first element of the right branch nodes. We can find this index by finding the first element in in-order PAST the root value. 
        # After every recursive call, we need to appropriately shrink the in-order array. If we go left, we return the left branch (left side of array), and vice versa. 
            # The in-order array tells us if we are at a root node
            # It also tells us how many nodes are in a particular branch, allowing us to slice the pre-order array. 
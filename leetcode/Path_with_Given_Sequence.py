# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

# The naive approach is to call DFS on every single path in the tree and compare each root-to-leaf path with the sequence. I think this is O(N) but I am not completely sure. 
# A more efficient approach would be to check for EACH NODE if it is valid, comparing the node to the corresponding index in the subsequence.
    # For a sequence [1, 2, 3], the 0th index would correspond to the root node, the 1st index (2) would correspond to the 1st level of the tree, etc. 
    # Time Complexity: O(N) as we touch each node a maximum of one time // Space Complexity: O(N) for recursive calling (worst case is if the tree is a linked list) 
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def find_path(root, sequence):
    def dfs(node, index):
    # Base cases are defined here:
        # If the path does not exist (or we do not have a tree at all), return False
        if not node:
            return False

        # If we have iterated past the length of our sequence, it means that we have not found a root-to-leaf path. Thus, it is invalid
        if index >= len(sequence):
            return False
        
        # If the node value does not match the corresponding valid in the sequence, return False
        if sequence[index] != node.val:
            return False

        # BASE CASE: If we are at a leaf node and we have successfully checked an amount of nodes that is EQUAL to the length of the sequence, then we have a successful path (remember, index is zero indexed)
        if not node.left and not node.right and len(sequence) - 1 == index:
            return True

        # Recursive Case: If ANY root-to-leaf path in the tree is valid, then we will return True
        return dfs(node.left, index + 1) or dfs(node.right, index + 1)

    return dfs(root, 0)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print(find_path(root, [1, 1, 1]))

main()
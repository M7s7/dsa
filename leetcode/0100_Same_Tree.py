# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# DFS recursive: Pre-order search on both nodes at the same time. If they are not the same, return False. 
    # Time Complexity: O(N) - each node (of both trees) will be touched once maximum
    # Space Complexity: O(N) - height of the tree is O(logn) for balanced tree. Worst case is a linked list tree (O(N))
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both same if both null
        if not p and not q:
            return True
        # Both different if vals are different or only one is null
        if not p or not q or p.val != q.val:
            return False
        # If either branch has a false node, we will return false
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
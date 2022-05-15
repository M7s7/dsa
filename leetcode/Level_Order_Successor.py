# Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.

# Approach: Keep adding children until the key node is found. 
    # This can either be done using a flag (as seen below), or by appending the children first when the node is found and then returning the first element in the queue. 
    # Time Complexity: O(N) // Space Complexity: O(N)
import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def find_successor(root, key):
    if not root:
        return 
        
    queue = collections.deque()
    queue.append(root)

    flag = False

    while queue:
        node = queue.popleft()
        
        if node:
            if flag is True:
                return node
            if node.val is key:
                flag = True

            queue.append(node.left)
            queue.append(node.right)

    return None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)

    if result:
        print(result.val)

    result = find_successor(root, 9)
    if result:
        print(result.val)

main()
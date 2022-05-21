# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Approach - scan every level and store in queue. Trick is to PEEK AT THE RIGHT VALUE of the level. 
    # Time Complexity: O(N) // Space Complexity: O(N)
import collections

def rightSideView(self, root):
    # Base case handling: If no root, return
    if not root:
        return root
    
    ans = []
    # Create queue for BFS - level traversal search
    queue = collections.deque()
    # Initiate root node in queue
    queue.append(root)

    # Loop through queue until we have traversed every node
    while queue:
        # Peek at right node value of queue - append to the answers
        ans.append(queue[-1].val)

        # Obtain length of queue
        qLen = len(queue)

        # Iterate through level, adding left/right nodes
        for _ in range(qLen):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

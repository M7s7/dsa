# Right Node always - BFS

# Approach - scan every level and store in queue. 
import collections

def right(self, root):
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
        # Peek at right side of queue - append to the answers
        ans.append(queue[-1])

        # Obtain length of queue
        qLen = length(queue)

        # Iterate through level, adding left/right nodes
        for _ in range(qLen):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            

    return ans

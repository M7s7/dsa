# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Optimal Approach:
    # Two pointers: One to iterate through the nodes on the current level. 
        # Second pointer to point at the start of the next level, allowing us to traverse the next level.
    # All the nodes below the current node are linked together with the next pointer.
        # This means that every current node is also linked together (as we move downwards).
        # This allows us to reach right.next nodes (through taking the LEFT branch of the CURRENT.NEXT node)
    # Time Complexity: O(N) // Space Complexity: O(1) as we use pointers to nodes

def connect(self, root):
    # Handling basecases - no tree or just one node:
    if not root or not root.left:
        return root
    
    # Initiate two pointers: A current level pointer, and a pointer for the next level
    nxt = root.left
    curr = root
    
    while nxt:
        # For the level below, link the nodes
        curr.left.next = curr.right
        # If there is a left node on the right of the right node, we can link those together
        if curr.next:
            curr.right.next = curr.next.left
            # Now we can move the node across if possible, to swap the next two children:
            curr = curr.next
            
        # If we are at the end node:
        else: 
            # If current has been placed on a None node, then the loop will break on the next iteration
            curr = nxt
            nxt = nxt.left
            
    return root

# Approach 2: Naive approach with queue
    # We can do classic BFS traversal. 
    # In order to not link the last node of each level, we will only .next len(queue) - 1 nodes
    # Time Complexity: O(N) // Space Complexity: O(N) through queue
def connect(self, root):
    if not root:
        return root
    
    queue = collections.deque()
    queue.append(root)
    
    while queue:
        qLen = len(queue)
        
        for i in range(qLen):
            node = queue.popleft()
            
            if not node:
                return root
            if i < qLen - 1:
                node.next = queue[0]
        
            queue.append(node.left)
            queue.append(node.right)
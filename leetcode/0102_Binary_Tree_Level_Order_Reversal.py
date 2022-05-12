# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Approach: BFS with a queue. Initialise the queue with the root node and make note of the size of the queue - this is the size of the level.
    # Then, iterate 'length' nodes through the queue, making sure to add the child nodes to the queue.
    # Also, while popping off the length nodes, place them in the levels list. 
    # At the end of a loop, append the levels list (as long as it is not empty)
# Time complexity: O(N) - every node will only be visited once // Space complexity: O(N) due to the queue size (technically n/2 because that is max for a single level)

import collections

def levelOrder(self, root):
    # Can also implement with a normal list in python, but a deque is O(1) time in popping off items
    queue = collections.deque()
    ans = []
    
    # Add the head node to the queue
    queue.append(root)
    
    # Create a loop, continuing it until we reach no more nodes (happens when the queue is empty)
    while queue: 
        # Create a list to hold nodes of the current level
        level = []
        # Get length of the current queue (how many nodes): This should be equal to the amount of nodes on the current level
        length = len(queue)
        
        # Iterate over the queue, popping off 'length' elements and adding them to the temporary level list
        for i in range(length):
            # Pop off the current (left-most) node and add it to the level
            node = queue.popleft()

            # Check if node is None: If so, we should skip these operations
            if node:
                level.append(node.val)
                # Add its children to the list. If the child is none, that is OK because the if statement above will deal with it
                # Make sure to add the left node first, as we want the traversal to be in the correct order
                queue.append(node.left)
                queue.append(node.right)
            
        # After we finish the for loop (which iterates over the nodes on the current level), we should append the list to the answers
        if level:
            ans.append(level)
        
    return ans


# We can also implement the algorithm with a list instead of a deque - but this is has worse time complexity

def levelOrder(self, root):
    queue = []
    ans = []
    
    queue.append(root)
    
    while queue: 
        level = []
        length = len(queue)
        
        for i in range(length):
            node = queue.pop(0)

            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            
        if level:
            ans.append(level)
        
    return ans
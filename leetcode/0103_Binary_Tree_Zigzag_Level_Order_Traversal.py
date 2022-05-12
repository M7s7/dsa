# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# This is just BFS with a twist (again). 
# Since every second level needs to be reversed, we will create a Flag (reverseFlag) to let us know if we are going to reverse. This will take advantage of the deque's properties of being able to pop from the left or the right in O(1) time.
    # Time Complexity: O(N) // Space Complexity: O(N)

import collections

def zigzagLevelOrder(self, root):
    queue = collections.deque()
    queue.append(root)
    # Create a reverse flag - Initiate it as false as every second level will be reversed.
    reverseFlag = False
    ans = []
    
    while queue:
        levels = collections.deque()
        length = len(queue)
    
        for i in range(length):
        
            node = queue.popleft()
            
            if node:
                # Use appendleft (like a stack, to reverse the order of the level) or append (regular order) depending on whether we need to reverse the list
                if reverseFlag:
                    levels.appendleft(node.val)
                else: 
                    levels.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        # Alternate the reverseFlag for the next iteration
        reverseFlag = not reverseFlag
    
        if levels:
            ans.append(levels)

    return ans
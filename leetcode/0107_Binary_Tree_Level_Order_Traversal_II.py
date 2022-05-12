# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Very similar to "102 - Binary Tree - Level Order Reversal". Only difference is that that the output/result is in reversed order. 

import collections

# Approach 1: STACK 1 - Storing everything in a seperate stack, then appending it at the end to the answers list
def levelOrderBottom(self, root):
    queue = collections.deque()
    queue.append(root)
    
    # We will store our temporary answers in a stack.
    stack = collections.deque()
    ans = []
    
    while queue:
        levels = []
        length = len(queue)
        
        for i in range(length):
            node = queue.popleft()
            
            if node:
                levels.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        # Instead of appending to the ans, we append to the stack   
        if levels:
            stack.append(levels)
    
    # Pop elements off the stack (from the right) and append it to the left of our answer list, reversing the stack
    while stack:
        ans.append(stack.pop())

    return ans

# Approach 1.5: STACK 2 - The answers list itself is deque, and we can 'PUSH' elements on the top of it
def levelOrderBottom(self, root):
    queue = collections.deque()
    queue.append(root)
    
    # Ans is a deque, not a normal list
    ans = collections.deque()
    
    while queue:
        levels = []
        length = len(queue)
        
        for i in range(length):
            node = queue.popleft()
            
            if node:
                levels.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        # Appendleft is pushing on the top of the stack   
        if levels:
            ans.appendleft(levels)
            
    return ans


# Approach 2: REVERSE OUTPUT
def levelOrderBottom(self, root):
    queue = collections.deque()
    queue.append(root)
    
    ans = []
    
    while queue:
        levels = []
        length = len(queue)
        
        for i in range(length):
            node = queue.popleft()
            
            if node:
                levels.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                
        if levels:
            ans.append(levels)
    
    # Reverse the answer list. 
    return reversed(ans)

    # Alternate reverse method 1:
        # ans.reverse()
        # return ans
    # Alternate reverse method 2:
        # return ans[::-1]
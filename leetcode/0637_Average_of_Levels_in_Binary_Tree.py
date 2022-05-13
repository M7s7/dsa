# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted. 
# Appproach - BFS using a queue. Instead of storing the values of the level, we store the sum of the level. Then, after we go through a level, we take the average and append it to the answer.
    # Time Complexity: O(N) // Space Complexity: O(N) for queue

import collections

# BFS implementation 1: While iterating through the level, do not append the None nodes.
def averageOfLevels(self, root):
    queue = collections.deque()
    queue.append(root)
    
    ans = []
    
    while queue:
        avg = 0
        length = len(queue)
        
        for i in range(length):
            node = queue.popleft()
            avg += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        avg /= length
        ans.append(avg)
        
    return ans


# BFS implementation 2: While iterating through the level, append all nodes (including the None nodes). To get the true number of nodes per level, we will use a counter variable. 
def averageOfLevels(self, root):
    queue = collections.deque()
    queue.append(root)
    
    ans = []
    
    while queue:
        avg = 0
        length = len(queue)
        node_count = 0
        
        for i in range(length):
            node = queue.popleft()
            if node:
                avg += node.val
                node_count += 1
                
                queue.append(node.left)
                queue.append(node.right)
                
        if node_count > 0:
            avg /= node_count
            ans.append(avg)
        
    return ans

# There are also DFS implementations of this question.
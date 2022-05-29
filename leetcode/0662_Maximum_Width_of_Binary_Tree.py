# Given the root of a binary tree, return the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), including the null-nodes between the end-nodes.
# It is guaranteed that the answer will in the range of a 32-bit signed integer.

import collections
# Approach 1:
# BFS - Node indexing. Our max length on each level will be the difference between the smallest and largest indices. 
# If a node's index is n, the node.left index will be n * 2, and the node.right index will be n * 2 + 1. 
# By doing this, we can compare the left most node's index with the right most node's index for the current level - this will return the width of the tree.
    # Visualisation: We can see the node rule holds true. If we replace some nodes with null nodes, the indices of the remaining nodes will remain true.
    #          1
    #      2       3 
    #    4   5   6   7 
    # Time Complexity: O(N), iteration over the nodes // Space Complexity: O(N) for queue (nodes in a single level) - can be O(N) + N if using temp queue. Typically, it will be N/2.
class Solutions:
    # Implementation 1: Most efficient and clean
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        queue = collections.deque()
        # The queue will be a list of lists, with the node and its index. 
        queue.append([root, 1])
        width = 0
        
        # Iterate over the queue until we traverse the entire tree
        while queue:
            # Find the indices of the left-most and right-most in the queue. Remember that the current queue currently holds the entire previous level IN level order. Thus, we can quickly find the width of the tree
            leftIndex = queue[0][1]
            rightIndex = queue[-1][1]
            # Add one to width, as the outer nodes are inclusive to width
            width = max(width, rightIndex - leftIndex + 1)

            # Since we cannot modify our iterator (cannot add or pop off elements during iteration), we will use a temporary queue
                # Alternatively, we can take the length of the current queue and iterate through len(queue) - this may be more space efficient, but it looks uglier
            temp = collections.deque()
            
            # BFS through the current level. Remember to store the indices of each node for the next level
            for node, index in queue:             
                if node.left:
                    temp.append([node.left, index * 2])
                if node.right:
                    temp.append([node.right, index * 2 + 1])
            
            # Reset our queue to the temp queue
            queue = temp 
            
        return width

    # Modification 1: Similar to above, but different method of gaining width
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append([root, 1])
        width = 0
        
        while queue:
            leftIndex = queue[0][1]
            temp = collections.deque()
            
            # Instead of determining the node immediately through indexing into the last element in the queue, we will instead check width for each node on the level. Definitely less efficient
            for node, index in queue:             
                width = max(width, index - leftIndex + 1)
                
                if node.left:
                    temp.append([node.left, index * 2])
                if node.right:
                    temp.append([node.right, index * 2 + 1])
            
            queue = temp 
            
        return width

    # Modification 2: Instead of using a temporary deque to store our level, we iterate through the list with O(1) extra space by using the length of the queue
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append([root, 1])
        width = 0
        
        while queue:
            leftIndex = queue[0][1]
            rightIndex = queue[-1][1]
            width = max(width, rightIndex - leftIndex + 1)

            # Iterate using the length of the queue. Although more space efficient, indexing is trickier as we cannot iterate through both list variables
            for _ in range(len(queue)):
                # Need to pop off nodes if iterating this way
                node = queue.popleft()

                # Since 'node' technically is a list: [node, index], we need to index into the node element
                if node[0].left:
                    queue.append([node[0].left, node[1] * 2])
                
                if node[0].right:
                    queue.append([node[0].right, node[1] * 2 + 1])
        
        return width


# Approach 2: Brute force. Add each node, including the null nodes. Then, before counting nodes, remove the left and right null nodes. When a middle null node is encountered, we will add two null dummy nodes to our queue. 
    # Time Complexity: Bigger than O(N) as dummy nodes are added - we traverse more nodes than normal // Space Complexity: Potentially than O(N) as dummy nodes are added
        # Note, this solution gave me TLE (like 90/120 tests passed) 
def widthOfBinaryTree(self, root):
    if not root:
        return 0
    
    queue = collections.deque()
    queue.append(root)
    width = 0
    
    while queue: 
        # Pop off null nodes from the side of the queue
        while queue and queue[-1] is None:
            queue.pop()
        
        while queue and queue[0] is None:
            queue.popleft()
            
        if not queue:
            return width
        
        levelSize = len(queue)
        width = max(width, levelSize)
    
        for i in range(levelSize):
            node = queue.popleft()
            
            if node:
                queue.append(node.left)
                queue.append(node.right)
            
            if not node:
                queue.append(None)
                queue.append(None)
    
    return width
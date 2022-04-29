# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# We can use FLOYD's CYCLE DETECTION ALGORITHM
# Initiate two pointers as NODES. One will be fast (going through two nodes each loop) and one will be slow (going through one node each loop)
# If there is an ending to the linked-list, then the while loop will terminate and we will return False.
# Else, the loop will iterate until fast and slow converge. Once the fast pointer cycles behind the slow pointer in the list, they will ALWAYS touch. 
## Remember, the fast pointer does not SKIP nodes. It simply visits TWO nodes every loop. 
# Time complexity is O(N) where N is the number of nodes in the list. Space complexity is O(1).

def hasCycle(self, head):
    # Initiate fast and slow pointers to the start of the linked list. Now, both pointers have access to the nodes to the linked list
    fast, slow = head, head
    
    # While loop: Continue pushing the pointers unless we find an ending to the linked list - This means that there are no cycles. 
    while fast is not None and fast.next is not None:
        # Slow pointer will move through the linked list one at a time
        slow = slow.next
        # Fast pointer will move through the linked list two at a time, going through two nodes
        fast = fast.next.next
        # If the fast pointer equals the slow pointer, it means that the fast pointer went through a cycle and ended up behind the slow pointer
        if slow == fast:
            return True
    # Loop is broken, meaning that the end was reached and there were no cycles - return False
    return False
    
# Alternate, less efficient solution:
# Iterate one pointer through the node list. Have a hashtable storing every visited NODE (not value of node, but the node object itself). Check if the current node is in the hash table - if so, there is a cycle. 
# Time complexity is O(N), space complexity is O(N)

def hasCycle(self, head):
    # Create a hashtable that flags nodes that we have visited before
    visited = {}

    # Initiate a pointer (node) that traverses the linked list
    search = head

    # While loop terminates if the linked-list has no cycles at the end
    while search is not None and search.next is not None:
        if search in visited:
            return True
        # Mark visited nodes as True
        visited[search] = True
        # Move to the next node
        search = search.next
    # If loop is broken, it means that there is an ending of the linked-list
    return False
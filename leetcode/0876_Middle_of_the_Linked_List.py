# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# This problem is easily solved using a fast and slow pointer. When the fast pointer reaches the end, the slow pointer is on the middle node.
# Time complexity: O(N) (1/2 N * 2 pointers) // Space complexity: O(1)

def middleNode(self, head):
    # Initiate fast and slow pointers
    fast = slow = head
    
    # While the fast pointer is not at the end of the linked list
    while fast is not None and fast.next is not None:
        # Move the fast pointer twice the speed of the slow pointer
        fast = fast.next.next
        # Move the slow pointer
        slow = slow.next
    
    # Once the condition is met, the slow pointer is in the middle of the linked list
    # Contingency is there is only ONE NODE (the head node)
    if slow is None:
        return head
    return slow


# ALTERNATE SOLUTIONS:  
# The naive, brute force solution is to use a slow pointer to count how many nodes there are.
## Then, traverse the list 1/2 the distance of the count. 
## Time complexity is O(N) (plus 1/2N), space complexity is O(1)

# Another naive solution is storing each node in an array, then returning the middle element of the array.
## Time complexity is O(N), space complexity is O(N)

# You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# METHOD 1: FAST AND SLOW POINTERS - FLOYDS ALGO. Then merge in place. 
# Time complexity: O(N) // Space complexity: O(1)
def reorderList(self, head):
    """
    Do not return anything, modify head in-place instead.
    """
    # FIND MIDDLE NODE through Floyd's algo
    slow = fast = head
    
    while fast and fast.next: 
        fast = fast.next.next
        slow = slow.next
    
    # REVERSE THE LIST for the second part of the list, starting from the middle node (current is middle node)
    previous, current = None, slow
    
    while current: 
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    

    # MERGE THE LISTS
    # Make sure we STORE the next element from both lists so we do not orphan the sublists when changing pointers
    
    # To simplify, I will create new pointers with more appropriate names
    reverse = previous # Reverse list nodes. Remember that previous is the last element of the node, as current and nxt are on None. 
    start = head # Start list nodes
    middle = slow # The middle node is the slow pointer
    
    # Create left and right temporary variables to store next values
    while start:
        # Before modifying any variables, check if we are at the end of the list (which is the middle node). When we reach it, point it at NONE
        if start is middle:
            start.next = None
            return
        
        left_temp = start.next
        right_temp = reverse.next
        
        start.next = reverse
        reverse.next = left_temp
                    
        start = left_temp
        reverse = right_temp


# METHOD 2: USE AN ARRAY
# We can use an array to store the actual node objects. We can then point towards these
# Cannot be bothered coding this part, but it is about O(N) in space and time complexity
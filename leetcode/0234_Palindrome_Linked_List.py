# Given the head of a singly linked list, return true if it is a palindrome.

# METHOD 1: Fast and slow pointer to find middle node (Floyd). Then reverse second half of list. Compare the two lists through node.values at each point. 
# If you want, you can also reverse the list again to make it the same as the original. 
# Time complexity: O(N) (n for step 1, n for step 2, n also for step 3 (technically 3N)) // Space complexity: O(1) because the list is reversed IN PLACE (only the next pointers are changed)

def isPalindrome(self, head):
    # FIRST - FIND MIDDLE NODE
    # Initiate fast and slow pointers
    fast = slow = head
    # While loop - moving fast pointer until it reaches the end, moving slow pointer at same time
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # SECOND: REVERSE THE SECOND HALF OF THE LIST
    # Initiate current and previous nodes, next node can be initialised in while loop
    current = slow
    previous = None
    
    # While current node is not None:
    while current: 
        # First, store a pointer to the next node
        Next = current.next
        # Point the current node to the previous node. This will remove current's pointer to Next, but we already have the node stored in our variables
        current.next = previous
        # Now, move all the pointers up a spot, taking care not to orphan any. Remember, the previous node does not need to be pointed at anymore, so that should move first
        previous = current
        current = Next     
        # Now, on the next loop while current is still a valid node, we will point our CURRENT NODE towards previous, reversing the list. 
        
    # THIRD: COMPARE THE LIST AND REVERSED LIST TO SEE IF THEY ARE IDENTICAL IN VALUE
    # From the loop above, 'previous' is sitting on the last element of the list (with current and Next sitting on None.)
    # We can initialise another node from the beginning and compare (Note that is is not required. We could just use head instead, but I think it looks neater this way)
    start = head
    # Note, loop has to use the PREVIOUS node as the conditional, not the START node. It won't work from START because the last node in the non-reversed list still points to the middle node (it does not terminate). 
    while previous is not None:
        # NOTE: We can also reverse the list during this process to make the linked list after checking the nodes - see the lines to reverse below
        if start.val != previous.val:
            return False
        start = start.next
        current = previous # Line 1 to reverse
        previous = previous.next
        current.next = Next # Line 2 to reverse (now that previous has moved, we can freely move that node to point to Next)
        Next = current # Line 3 to reverse (now that Next is already pointed to, we can move it to current)
    return True
###


# METHOD 2: Store values in array and use two pointers to search. Less space efficient than in-place reversal
# Time complexity: O(N) // Space complexity: O(N)
def isPalindrome(self, head):
    # Array solution: Store value of nodes in a list. Then go back in list and compare
    values = []
    start = head
    
    # Traverse the list and store values in list
    while start is not None:
        values.append(start.val)
        start = start.next
    
    # Now we have a list of values - place pointer from left and right of list and compare
    left = 0
    right = len(values) - 1
    
    while left < right: 
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1
    return True


## There is also a recursive solution (seen on Leetcode) but I will not go over it. 
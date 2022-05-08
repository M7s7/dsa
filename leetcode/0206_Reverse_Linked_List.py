# Given the head of a singly linked list, reverse the list, and return the reversed list.

# ITERATION:
# Time complexity: O(N) // Space complexity: O(1) as it is in place
def reverseList(self, head):
    # Reverse the list from the head node
    prev = None
    
    # Reverse the list. Notice that the assignor becomes the assignee the next line.
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    
    # Return the new head node - this is prev, as our head node is now on 'None' at the end of the while loop
    return prev




# RECURSION:
# Time complexity: O(N) // Space complexity: O(N) due to call stack
def reverseList(self, head):
    # This is NOT a basecase - instead, this returns none if there is no linked list - handles edgecases
    if not head:
        return None

    # newHead is the node we return at the end of each call. 
    # Note that newHead is initially set to the node we are currently on, but is ALTERED on every call (as it is reassigned during the newHead = recursive function)
    # Since the last node will not reassign the value, the node that newHead points to will REMAIN the last node. 
    newHead = head
    
    # Recursive case - if there is a valid next node.
        # Note that it also acts as our BASE CASE as when we are on the last node, we will skip straight to returning newHead (which would be equal to the last node)
    if head.next:
        # Recursion travelling to all the nodes until we hit the base case of having no next node
            # Note that every recursive call will be also changing the links between itself and the node to its right
        newHead = self.reverseList(head.next)
        # This REVERSES the link of the right node: eg. 1 -> 2 -> will become 1 -> <- 2
        head.next.next = head
        # This will complete the reversal: eg. 1 -> <- 2 will become 1 <- 2
        head.next = None
    
    # Since the base case is called LAST, head will be the at last node (which is what we want)
    # On recursive calls, newHead is going to be the node on the right (remember, we go from the base case to the head node)
    return newHead

    # Intuition behind the recursive solution
        # Imagine a linked list like this: 1 -> 2 -> 3 -> None
        # When we initially call reverse list (lets call it f), we call it on the head node, 1. Thus, the function can be called f(1).
        # During f(1), we assign newHead to node 1 but then it gets reassigned during the recursive call on line 39 to some indeterminate node. 
        # The recursive calls f(2) then f(3). Remember, at this point f(1) and f(2) are currently paused and are still on the stack.
        # F(3) happens to be our basecase as head.next for (3) is none. Thus, newHead is not reassigned for this call and instead newHead is returned as (3). 
        # Now f(2) can finish - newHead for f(2) is assigned to be the return value of f(3). Then, the link for node (3) is reversed to point to node (2).
            # Additionally, node (2)'s link to node (3) is broken and converted to None. 
        # Now f(1) can finish - newHead for f(1) was assigned as f(2)'s return value, which is still (3). F(1) finishes by reversing the links. 
    # Thus, after the initial call is finished, we have the return value carried over from the base case call (3) as the new head. 
    # Additionally, every recursion call has reversed the link between the current node and the node on the right. 
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
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            # Basecase
            if not curr:
                return prev
            
            next = curr.next
            curr.next = prev
            return reverse(next, curr)           
        
        return reverse(head, None)
        
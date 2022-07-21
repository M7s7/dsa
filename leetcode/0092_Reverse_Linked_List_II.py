# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
    
# APPROACH: Reverse the sublist. Then, reattach the left and right sublist to the right and left sides of the outer list.   

# This solution uses iterative reversing of a linked list
    # Time complexity: O(N) to reverse the nodes
    # Space complexity: O(1)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Dummy node, as we might be forced to alter the head. 
        dummy = ListNode(0, head)
        l = dummy
        
        # Set the left pointer
        for _ in range(left):
            # Store the left edge as our prev left pointer
            left_edge = l
            l = l.next
        
        # Set the right pointer
        r = l
        for _ in range(right - left):
            r = r.next
        # Store the right edge as our next right pointer
        right_edge = r.next
        
        # Traverse the sublist and reverse it
        curr = l
        prev = right_edge # Setting the first prev node as our right edge correctly links our left node
        
        while curr != right_edge:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt      
        
        # Link our right node with the left edge
        left_edge.next = r
        
        return dummy.next
       
    # Note that if our left node is our head node (l = 1), our dummy node is our left edge. 
    # Thus, when we reverse the list, our dummy node will be connected with the new head node, so that's why we can still return dummy.next.
        
        
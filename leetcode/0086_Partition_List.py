# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Approach: Create two seperate lists (with dummy nodes) to partition the lists (this will keep the lists in order).
    # After adding all the nodes, connect the lists - last node of less connected with head node of more
    # Then, make sure there is no cycle by pointing last node of more to NULL
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_less = ListNode()
        dummy_more = ListNode()
        # Pointer to the 'prev' node in the two lists
        less = dummy_less
        more = dummy_more
        # Partition the lists
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next
        # Set 
        more.next = None
        
        # Connect the two lists
        less.next = dummy_more.next
        return dummy_less.next
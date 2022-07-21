# You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# METHOD 1: FAST AND SLOW POINTERS/REVERSE LINKED LIST.
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find middle node (right biased)
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half of linked list
        prev = None # We want to point our middle pointer at nothing (as it is our last node in our final list)
        curr = end = slow # Slow pointer is sitting on mid pointer
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Join the lists together (we can treat the linked list as two seperate linked lists)
        curr = head
        nxt = prev # Prev pointer is on the start of our reversed list (head node of reversed list)
        while curr != end:
            temp = curr.next
            curr.next = nxt
            curr = nxt
            nxt = temp
        
        return head # No need for dummy variable as head does not change
        

# METHOD 2: USE AN ARRAY
# We can use an array to store the actual node objects. We can then point towards these
# Cannot be bothered coding this part, but it is about O(N) in space and time complexity
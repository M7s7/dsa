# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# One pass solution: Two pointers. Offset fast from slow by n nodes.
# Then, when fast reaches the end, slow will be on the node we want to remove. 
    # Time Complexity: O(N)
    # Space Complexity: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        # Offset fast pointer
        while n > 0:
            fast = fast.next
            n -= 1
        # Fast will get on NULL, slow will get on target node to remove
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        return dummy.next


# Two pass solution: Calculate number of nodes, then target node to remove.
    # Time Complexity: O(N) - or 2*N
    # Space Complexity: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nodes = {}
        nodes[0] = dummy
        
        size = 0
        curr = head
        while curr:
            size += 1
            nodes[size] = curr
            curr = curr.next
        
        index = size - n + 1
        nodes[size + 1] = None
        prev = nodes[index - 1]
        nxt = nodes[index + 1]
        
        prev.next = nxt
        return dummy.next


# One pass hashmap solution: Hard to code up and quite bad. Store every node we travel to in a node by its 'index'
    # Time Complexity: O(N)
    # Space Complexity: O(N)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nodes = {}
        nodes[0] = dummy
        
        size = 0
        curr = head
        while curr:
            size += 1
            nodes[size] = curr
            curr = curr.next
        
        # Size is 6 (as we are counting the null node)
        index = size - n + 1
        
        nodes[size + 1] = None
        prev = nodes[index - 1]
        nxt = nodes[index + 1]
        
        prev.next = nxt
        return dummy.next
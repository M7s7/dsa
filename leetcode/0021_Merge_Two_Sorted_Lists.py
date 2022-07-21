# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Compare both nodes and append the smaller one to the list. 
# Dummy node is created to have a node to add to.
    # Time Complexity: O(m + n) - length of both lists
    # Space Complexity: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1: 
            curr.next = list1
        if list2:
            curr.next = list2
            
        return dummy.next

# Less efficient (as loop terminates after both lists are exhausted, not just one), but more explicit. 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        
        curr = dummy
        while list1 or list2:
            if not list2:
                curr.next = list1
                list1 = list1.next
            elif not list1:
                curr.next = list2
                list2 = list2.next
            else:
                if list2.val < list1.val:
                    curr.next = list2
                    list2 = list2.next
                else:
                    curr.next = list1
                    list1 = list1.next
            curr = curr.next
        
        return dummy.next
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Approach: Travel linked list and store the mod 10 number for each node. Track carryover and add it onto the next. 
    # Time Complexity: O(max(N1, N2)) to travel linked lists
    # Space Complexity: O(max(N1, N2)) for new next linked list
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        head = ans = ListNode(None)
        
        curr_sum = 0
        
        while p1 or p2 or curr_sum:
            if p1:
                curr_sum += p1.val
                p1 = p1.next
            if p2:
                curr_sum += p2.val
                p2 = p2.next

            # Transfer value to node
            ans.next = ListNode(curr_sum % 10, None)
            ans = ans.next
            
            if curr_sum >= 10:
                curr_sum = 1
            else:
                curr_sum = 0
        
        return head.next

# My implementation - messier
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        ans = ListNode(None)
        head = ListNode(None, ans)
        carry = 0
        
        while p1 or p2:
            val1, val2 = 0, 0
            if p1:
                val1 = p1.val
                p1 = p1.next
            if p2:
                val2 = p2.val
                p2 = p2.next
            curr_sum = carry + val1 + val2
            # Transfer value to node
            ans.val = curr_sum % 10
            ans.next = ListNode(None)
            prev = ans
            ans = ans.next
            
            if curr_sum >= 10:
                carry = 1
            else:
                carry = 0
        
        if carry >= 1:
            ans.val = carry
        else:
            prev.next = None
        
        return head.next
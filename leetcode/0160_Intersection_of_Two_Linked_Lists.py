# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Approach 1 (and my intuition): Difference of two lists. We will offset our longer list by the difference of the two lists, then use two pointers to find the right list. 
    # Time Complexity: O(N + M) (iteration through both lists)
    # Space Complexity: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Get the sizes of both lists and their end nodes
        endA, sizeA = self.listSize(headA)
        endA, sizeB = self.listSize(headB)
        
        # If there is no intersection, return None
        if endA != endB:
            return None
        
        # Offset the longer list
            # The difference of the length of lists
        offset = abs(sizeA - sizeB)

        while offset > 0:
            if sizeA > sizeB:
                headA = headA.next
            else:
                headB = headB.next
            offset -= 1
        
        # After our longer list is offset properly, iterate both pointers until we find a match
        while headA != headB:
            headA = headA.next
            headB = headB.next
        # Return intersection
        return headA  

    # Helper function - return endNodes and list sizes   
    def listSize(self, node):
        size = 1
        while node.next: 
            size += 1
            node = node.next
        return node, size


# Approach 2: Two pointers. Instead of manually calculating the length, we can just run through each list.
    # When we get to a null node, we instead will jump to the other list to nullify the size difference.
    # After one swap, we will guaranteed get a match if there is an intersection. If there is no intersection, the NULL NODES will still coincide instead. 
        # Because of this, we will let our nodes null at points before swapping lists.  
    # Same time and space complexity as above
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA, nodeB = headA, headB

        # Maximum of two cycles before we exit the loop
        while nodeA != nodeB:
            # Keep going to the next node
            if nodeA:
                nodeA = nodeA.next
            # If we are on a null node, go to the start of the other list. 
            else:
                nodeA = headB
            
            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA
                  
        return nodeA
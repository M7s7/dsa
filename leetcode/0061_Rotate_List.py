# Given the head of a linked list, rotate the list to the right by k places.

# Approach: Measure the length of the list.
    # A rotation of the list would make the new tail of the list equal to the length - kth node (if we start from the dummy node)
    # When we reach the target node, we take the next node as the START and then sever the connection.
# Time complexity: O(N) (pass through the list at most twice) // Space complexity: O(1)

def rotateRight(self, head, k): 
    dummy = ListNode(0, head)
    
    # Edgecase: empty list
    if not head:
        return dummy.next
    
    # Pass through the list to see how long the list is
    counter = 0
    
    tail = dummy
    while tail.next:
        counter += 1
        tail = tail.next
        
    # Edgecase: k larger than length of list
    # Mod k by the size of the list, just in case k is larger than the size of the list
    k = k % counter
        
    # Create a circular list - node sits on the tail node - link it with the start node
    tail.next = head
    
    # Now, rotate through the list and find the target node that will serve as the new end of our linked list
    target_length = counter - k
    
    newTail = dummy
    # We can start from the dummy (newTail) node and iterate towards the target node.  
    for i in range(target_length):
        newTail = newTail.next
        
    # At this point, the dummy node is on our new end node
    # Before modifying the new end, set the NEXT node to the start of our new list
    newHead = newTail.next
    
    # Now, we can sever the connection and make it truly the end node
    newTail.next = None
    
    return newHead
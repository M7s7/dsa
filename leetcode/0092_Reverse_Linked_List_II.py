# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
    
# APPROACH: We can simply reverse the list between the left and right nodes, then re-attach the edges. 
    # Intuition is that we reverse the list from the left node. We do this until we reach our right node. 
    # We must record our left and right nodes in order to link them with the outside nodes
        # For easy understanding, consider this linked list: o -> (L_prev) -> L -> o -> R -> (R_next) -> o
            # Eventually, we want to convert is such that L_prev -> R and L -> R_next: o -> (L_prev) -> R -> o -> L -> (R_next) -> o
        # We have to store four different nodes - L_prev, L, R and R_next - then, we reverse from L to R
        # Then, we connect L_prev to R, and then we connect L to R_next. 
    

# This solution uses iterative reversing of a linked list
    # Time complexity: O(N) to reverse the nodes // Space complexity: O(1)

def reverseBetween(self, head, left, right): 
    # Step 1: Starting from the head node (which is in position 1), get to the left node. 
    # Our dummy node will ALWAYS point towards the head node. More information about why the head node is important is below:
    dummy = ListNode(0, head)
    # L_prev is initiated on the node BEFORE head.
    L, L_prev = head, dummy

    # Iterate left - 1 times (which is what we want because we are already, by default, on position 1 (the head node))
    for i in range(left - 1): 
        # Again, same thing as saying L_prev, L = L_prev.next, L.next
        L_prev, L = L, L.next

    # Step 2: Reverse the list from L to R. This involves reversing the links in EACH NODE between R and L. In the example above, a difference of 2 positions (2, 4) is actually 3 nodes - so we can use len formula to get elements between two points (r - l + 1)
    # Initialise our pointers to reverse the list
    prev = L_prev
    current = L
    
    # Traverse to the R pointer and reverse all the nodes in between
    for i in range(right - left + 1):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        # Note that when we get to the R element, we actually iterate the current node PAST it (as the current node goes to the current.nxt node after the loop). However, prev is on the R node. 

    # Step 3: Connect the nodes.   
    # For clarity, let's rename some of the nodes so we know what they are
    R_next = current
    R = prev

    # Let's combine the nodes together: L to RR and LL to R
    L.next = R_next
    L_prev.next = R
    
    # Step 4: Return the head node using the dummy node
    return dummy.next

##### WHY IS THE DUMMY NODE IMPORTANT?
    # The dummy node is important as it allows us to have a valid pointer always pointing at the head node. Scenarios where this is useful include:
        # Linked lists with only ONE node. Initialising L_prev to 'None' instead of 'dummy' results in an error on line 47, as a NoneType object does not have a 'next' attribute
        # Linked lists with TWO nodes. If there are two nodes, the head node is the one that is being reversed. 
            # The nodes look like this: (1) <- (2). However, (1) is still the head node, meaning that if we return it, we would get a linked list that BEGINS from 1 instead of the proper 2. 
            # Compare this with having a dummy node. Remember that with TWO NODES, L_prev is the dummy node (as L is the head node). 
                # If the head node is reversed, it is no problem as we REASSIGN what the dummy node points to: on line 47, we point the dummy node to R (or node 2). Thus, we get 2 -> 1 as a list if we return the dummy node. 


# There is also a RECURSIVE solution but I have not coded it. 

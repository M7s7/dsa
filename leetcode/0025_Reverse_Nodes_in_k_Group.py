# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# INTUITION: Difficult question. Basically, it comes down to multiple pointers that you have to store that have multiple functions:
    # The groupPrev pointer - at the start of the loop, it points to the node DIRECTLY BEFORE the current k-group. At the end of the current loop (and for use on the next loop), we want to set the variable to the ORIGINAL START NODE OF THE CURRENT GROUP. 
        # Note that before reassignment, groupPrev.next is the ORIGINAL START NODE of the current k-group. GroupPrev.next becomes groupPrev, and the .next gets linked with the current kth node. 
    # The kth pointer - this node should travel k steps from the groupPrev node to reach the kth node. This node is used in several ways:
        # As a conditional to stop the reversing of the list - once this node is reached, we should stop reversing
        # After reversal, the kth pointer becomes the NEW START OF THE CURRENT GROUP. Thus, we want to link GROUPPREV.NEXT to the KTH POINTER. 
    # Time Complexity: O(N) // Space Complexity: O(1)

def reverseKGroup(self, head, k):
    # Need a node to point to the 'new' head node after the initial reversal
    dummy = ListNode(0, head)
    
    # GroupPrev is the node that stores the FIRST node in the original order of the k-group. 
    groupPrev = dummy
    
    # Kth will be the pointer which will find the kth node
    kth = dummy
    
    # We want to iterate through our linked list. Every loop will reverse the next k-Group until there are no more k Groups.
    while True:
        # Find the k_node. We start from the node JUST BEFORE our group starts - doing k jumps from this point will bring us to the k Node
        kth = self.kNode(groupPrev, k) 
        
        # Stop if we don't have a kth Node (kth = none)
        if not kth:
            break
        
        # Store kth.next before reversing the list - this node will be the start node for the next group (in its original order)
        groupNext = kth.next
    
        # Reverse the linked list, reversing each node until we reach the k node
        # Usually we set prev to None. However, we set it to kth.next initially in this case because we want a SINGULAR list. If we set it to None, all the k groups do not link to each other
        prev, current = kth.next, groupPrev.next
        
        while current != groupNext:
            nxt = current.next
            # Notice that on our first loop per group, our original start node POINTS AT the start of the next k-group instead of None. This keeps the group as a single linked list
            current.next = prev
            prev = current
            current = nxt             
        
        # After reversal of the list, we want to set the current kNode as the START of our group.
        # Note that the original start node of the kgroup has become the LAST node of our group. We should store this variable before groupPrev is changed. 
        temp = groupPrev.next # Was the original starting node (previous end node pointed towards original starting ndoe)
        
        # Now we can set groupPrev was the node RIGHT BEFORE our current k-group. Thus, we can link that node with the kNode.
        # Notice that THIS fixes the pointer from the previous loop, from groupPrev -> start node TO groupPrev -> kth node
        groupPrev.next = kth # Now, previous end node points towards k - our NEW starting node
        
        # Set groupPrev to the end of the current k-node group. This is set-up for our next loop, where we use groupPrev to determine the next k-pointer.
        groupPrev = temp # For the next loop, we update the previous group node as the END of our new k-node group - the start of our old list becomes the end of our new list. 
    
    return dummy.next


def kNode(self, node, k):
    while k > 0 and node:
        node = node.next
        k -= 1
    return node
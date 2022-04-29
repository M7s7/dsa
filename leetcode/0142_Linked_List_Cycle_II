# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. Do not modify the list. 

# METHOD 1: FLOYD'S ALGORITHM. 
# Initialise a slow and fast pointer at the root node and find the intersection point (if there is a cycle in the linked list). 
# Once found, initialise a new pointer at the root node again. Increment a node at the intersection point (I chose slow but it doesn't matter) and the new node.
# Where they intersect is the beginning cycle node. 
# Time complexity: O(N) // Space complexity: O(1)

def detectCycle(self, head):
    slow, fast = head, head
    # Find if the linked list has a cycle or not:
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        
        # Break loop if we have found an intersection point within a cycle in the loop
        if fast == slow:
            break
    # If there is no cycle, exit      
    if fast is None or fast.next is None:
        return None    
    
    # Part II of Floyd's algorithm: the distance from the start node to the first cycle node is EQUAL to n cycle distances + x, where x is the distance between the intersection point and the first cycle node. 
    start = head
    
    while start != slow:
        start = start.next
        slow = slow.next
    
    return start


# METHOD 2: Hashmap solution where we return the first node that is visited twice. Much easier but less space efficient.
# Time complexity: O(N) // Space complexity: O(N)

def detectCycle(self, head):
    # Create hashmap with visited notes
    visited = {}
    # Create pointer node to iterate through the array
    search = head
    
    # While loop checking if the linked list has no cycle
    while search is not None and search.next is not None:
        # Return node on the first repeater node (as that is the beginning of the cycle)
        if search in visited: 
            return search
        # Else, store the node in the dictionary and move to the next node
        visited[search] = True
        search = search.next
    # Return null if no cycle
    return None


#### MATHS EXPLANATION OF SECOND PART OF FLOYD'S CYCLE ALGO:
#                          _____
#                         /     \ cycle distance = c
#        head_____p______E       \
#                   x--> \       /
#                         I_____/  
# Imagine a linked-list with a cycle like this, travelling clockwise through the linked list cycle. 
# Let p be the distance between root node (head) and the cycle entry node (E). 
# Let x be the distance between the intersection (I) of the fast and slow pointers and E. 
# Let c be the distance of one full cycle. 
# EQ 1: The fast pointer travels twice as fast as the slow pointer. Thus, when they meet at the intersection: fast_distance = 2(slow_distance)
# EQ 2: We know that the slow pointer travels p + c - x. It cannot travel a full cycle because the fast pointer is already in the cycle and will catch up before it completes a full cycle. 
# EQ 3: The fast pointer will travel p + Nc - (c - x); N means the amount of cycles it does before the slow pointer catches up and reaches the cycle. 
# Since N is an arbitrary number, we can simplify the right side to p + Nc - x. 
# EQ 4: Subsituting EQ3 and EQ2 in EQ1, we get 2(p + c - x) = p + Nc - x
# EQ 4a: Expanding the equation gives us 2p + 2c - 2x = p + Nc - x
# EQ 5: Simplifying the equation gives us p = Nc + x (remember, since N is an arbitrary number, we can just remove the 2c out of the equation)
# This means that the distance between p = x + an unspecified number of cycles. 
# Since cycles bring us back to the same point, if we start at a point x distance away from the start node, we will stop on it at the same time as a node travelling p distance will. 
# Thus, we can determine where the entry cycle node is through the intersection of a node travelling p distance and one travelling x + Nc.
# Conveniently, our I nodes are placed x distance away, so we can reuse them for our algo. 
## NOTE: Neetcode video 287 has an excellent video explaining Floyd's algo. 
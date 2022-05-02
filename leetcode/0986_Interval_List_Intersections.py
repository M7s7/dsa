# You are given two lists of closed intervals, A and B, where A[i] = [starti, endi] and B[j] = [startj, endj]. 
# Each list of intervals is pairwise disjoint (no pair is the exact same as the other) and in sorted order.
# Return the intersection of these two interval lists.


# To iterate through both lists, we initiate  TWO POINTERS. Create a while loop, making sure that these indexes are valid.
# We compare one interval from each list. To check for overlapping intervals, we can see if they CROSS LOCK: ie. the start of one is smaller than the end of the other for BOTH intervals. 
# If they cross-lock, we return the INTERSECTION - MAX of both starts, MIN of both ends. 
# After every iteration, we want to get another interval to compare. We keep the interval with a BIGGER END, iterating up the other list. The interval with the smaller end is no longer of use as it cannot overlap with any future intervals from the other list. 
# Time complexity: O(N + M), where N is the amount of intervals in A and M in B // Space complexity: O(N + M), as we have to store intersectionss. 

def intervalIntersection(self, A, B):
    # Initiate two pointers. These pointers will iterate through the lists A and B. 
    i = 0
    j = 0
    
    # Create a list to store the output
    ans = []
    
    # Iterate through both of the lists until we get to the end of both of them. 
    while i < len(A) and j < len(B): # Notice that BOTH lists have to be finished before we stop iterating
        
        # To make the code neater, we will express our start and end pointers for the current intervals here
        start_A, end_A = A[i]
        start_B, end_B = B[j]
        
        # Create our condition of when lists A and B have an overlap. The condition is the SAME regardless of if start1 or start2 is lower
        ## This occurs when there is a CROSS LOCK where start1 and start2 are EQUAL or SMALLER than end2 and end1 respectively. 
        if start_A <= end_B and start_B <= end_A:
            # The OVERLAPPING SECTION is the opposite of a merge: it is the smallest END and the largest START from the two. 
            ans.append([max(start_A, start_B), min(end_A, end_B)])
            
        # We need to get a new interval. We keep the interval with the BIGGER endpoint, as the one with the SMALLER endpoint can never again overlap with the other list (as the list is in sorted order, all subsequent list2 STARTS are larger than the current list2 END)
        if end_A > end_B:
            j += 1 # Push list B as the current interval B is never interacting again
        
        else:
            i += 1 # Push the other list instead
    return ans

# Note: There is a situation where end_A == end_B and A is at its last interval, meaning that we have pushed i beyond a valid index.
## However, we can disregard this edgecase because reaching the end of the list with both intervals ending at the same time means that there are NO MORE OVERLAPS anyways.
## Thus, even though list B has not been fully explored, all the startB's in future intervals are LARGER than the LARGEST ENDPOINT in list A - thus, no overlaps anyways.
## Additionally, the 'index out of range' issue is taken care of by our while loop condition. 
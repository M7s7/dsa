# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. (eg. [1, 2, 3, 3, 4])
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.


# METHOD 1: FLOYD'S CYCLE DETECTION ALGO
    # We can treat the nums array as a linked linked list, where:
        # node.value = i
        # node.next = nums[i]
    # Since the range of numbers is from 1 to n, we can guarantee that index 0 is the head of the linked list (as no node.nexts will be pointing to it)
    # If there were no duplicates, we would never point to the same index and the linked list would eventually terminate. 
    # However, since there are duplicates, there is GUARANTEED to be a cycle as an index will be pointed to twice
    # Thus, we can use FLOYD'S CYCLE DETECTING ALGORITHM and find the duplicate number. 
    # Time Complexity: O(N) // Space Complexity: O(1)

def findDuplicate(self, nums):
    # Initiate pointers
    fast = slow = 0 # Remember, the zero index is our 'head node'
    
    # Find the intersection between the fast and slow pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]] # This is equivalent of node.next.next
        
        if slow == fast:
            break
            
    # The cycle entrance will be the duplicate number, as this is the number that multiple other numbers are pointing to. 
    # Now that the intersection is found, we need to find the CYCLE ENTRANCE. Move a node from the intersection and a head node until they touch - this will be at the entrance. 
    start = 0 
    
    while start != slow:
        slow = nums[slow]
        start = nums[start]
    
    # When they equal, we can return that number
    return start
    

# METHOD 2: BINARY SEARCH
    # BINARY SEARCH, SEARCHING RANGE IN INDICES INSTEAD OF VALUES. The indices range from [0, n] while the values range from [1, n]. 
    # Comparing indices and values, the index has a 0 while the values have a duplicate of one of the numbers in the range. 
    # We do not have to sort the array, as we are using the INDICES (which are already sorted)
    # Time complexity: O(N log N) (log N for binary search, N times for counting through the array every time) // Space complexity: O(1)

def findDuplicate(self, nums):
    # Create pointers to the range to search the index space
    low = 1 # Range of numbers is 1 to N
    high = len(nums) - 1 # The list is zero-indexed, so len(nums) is N + 1
    
    # Binary search - compare count lower or equal values to the mid index
    while low < high:
        mid = low + (high-low) // 2
        count = 0
        
        # We count how many NUMBERS in the array are lower than the index value of 'mid'.  
        for values in nums:
            if values <= mid:
                count += 1
        
        # If the count of numbers is lower or equal than mid, the duplicate cannot be in the range of numbers between 1 and mid as we can assign each index with a unique number in the list.  
        if count <= mid:
            low = mid + 1
        
        # However, if the count of numbers is higher than mid, it means that there count of numbers which are lower or equal to mid CANNOT fit between the range 1 and mid - there is not enough space without the zero index. Thus, the duplicate number must sit here. 
        else:
            high = mid
    return low
    
    # intuition:
    ## INDICES 0[1 2 3 4 5]--> 1 2 3 4 5
    ## VALUES  5 5 4 2 3 1 --> 1 2 3 4 55
    # An easy way to think about this question is to remove the 0 index but keep all the values. Now, we assign a value equal to each index. Since there is a duplicate, there will be two values that will be forced to share the same index. 
        # In this example, 5 is the duplicate. Implementing binary search, we are using the indices as our search space for the answer. Each index (besides 0) can be thought as being mapped to one number, except the duplicate. 
        # Mid is currently 3 - we count the VALUES of how many numbers are lower than mid or equal to mid (answer is 3). 
        # As we can see, in the range of numbers below and including 3 (1, 2 and 3), there are 3 UNIQUE numbers that we can slot our answer into. Thus, the duplicate is not here. 
        # On the other hand, there are 3 values larger than 3, but only two unique numbers in that range (4 and 5). Thus, because of the PIGEONHOLE THEOREM, the duplicate must be one of those numbers. 
        # Thus, let's 'shrink' our array by moving our searchspace:
    ## INDICES/0/1 2 3[4 5]
    ## VALUES  5 1 2 3 4 5  <-- visualised this way, we can see that the duplicated number NEEDS to sit on a zero indice outside of the range [1, n], otherwise it won't fit
        # Now, mid is 4. We still count through the whole list of values - there are 4 numbers equal or smaller than 4, which we can accomodate (1, 2, 3 and 4)
        # However, there are 6 numbers equal or smaller than 5. We cannot accomodate this as we only have 5 slots to put the numbers in. Thus, we move the low pointer up to 5. 
        ## INDICES/0/ 1 2 3 4[5]
    # Now, we have converged on the duplicated number. We can return this index. 



# METHOD 3: CYCLIC SORTING to values by 1 indexed position; if we find duplicate numbers while swapping, we will return that number.
# Time complexity: O(N) // Space complexity: O(1). HOWEVER, this solution ALTERS THE INPUT ARRAY, so it does not satisfy all the conditions. 

def findDuplicate(self, nums):
    # For valid numbers, indices should equal value - 1.
    n = len(nums)
    i = 0
    
    # We want to loop through the whole number array
    while i < n:
        # J is the indice where the number should be
        j = nums[i] - 1
        
        # Check if the number is in the wrong position (aka if i == j, then its in the right spot)
        if i != j:
            # Swap nums[i] to where it belongs (the j index). However, if they are find a duplicate of the number while swapping, we will return this number
            if nums[i] == nums[j]:
                return nums[i]
            
            # Else, keep swapping numbers to the right indices until nums[i] is in the right spot
            else:
                nums[i], nums[j] = nums[j], nums[i]
        
        # If the number is in the right spot, we will go to the next index
        else:
            i += 1

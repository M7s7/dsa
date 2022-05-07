# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Find the kth positive integer that is missing from this array.


# METHOD 1: BINARY SEARCH (OPTIMAL)
# We can take advantage of the fact that the array is sorted, because at each point we can keep track of how many numbers are missing from the left of the array:
    # INDICES: 0 1 2 3 4  5
    # IDEAL:   1 2 3 4 5  6
    # VALUES:  2 3 4 7 11 12
    # MISSING: 1 1 1 3 6  6
# Comparing the actual values to what is ideal, we can see that the difference between the two gives us how many values are missing at each index. 
# We can be sure of how many numbers are missing because all the numbers are UNIQUE - there are no repeats because the list is in STRICTLY INCREASING ORDER. 
# Thus, our approach will be finding the FIRST ELEMENT that has a 'missing' value equal or greater than K. 
# Time Complexity: O(log N) // Space Complexity: O(1)

def findKthPositive(self, arr, k):
    # Note that the end pointer actually points to an index OUTSIDE our valid indices (normally, the end pointer would be len(arr) - 1)
        # This is to account for situations where there are no elements with more or equal to k missing numbers. 
        # Note: We should never get out of range errors as we never actually index into the end index. 
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        # Finding how many numbers are missing: value - ideal == value - (index + 1) == value - index - 1
        if arr[mid] - mid - 1 < k:
            # If middle number has too little missing numbers, move the low pointer up
            start = mid + 1
        # Else, if the middle number has too many missing numbers, move the high pointer down
        else:
            end = mid
    
    # After this process, the end pointer will lay on the first element over the 'missing value'. What does this mean?
        # The element sitting on 'end' is the first invalid one. Thus, all the elements before 'end' are 'not missing' and count towards our array.
        # The number of elements this is happens to be equal to end (remember, there are 'end' number of elements before the end index because of zero-indexing)
            # Eg. In the example above, at index 4, there are 4 elements before it (0, 1, 2, 3). 
        # Thus, we know we have 4 elements currently and we can 'fill in' the gaps by adding k to that total. 
    return end + k


# METHOD 2: HASHMAP PASS/ARRAY PASS/ SET PASS
# From 1, keep counting up and checking if the numbers are in the original array. Stop when we reach k values and return the number. 
# We can use some data structure (hashset, set, dictionary) or we can use the existing array to check the values. 
    # Time complexity: O(N + k) // Space complexity: O(N) or O(1) depending on the method (if a new data structure is created, O(N))
class Solutions: 
    # Using dictionary - Time complexity is O(N+k) + N for the hashmap // Space complexity is O(N)
    def findKthPositive(self, arr):
        nums = {}
        
        for num in arr:
            nums[num] = True

        # How many numbers do we have to iterate through?
        # We could have no missing numbers, sorted from 1 to N - this will be equal to len(arr). 
            # Then, we would have to account for k numbers past the range - that is now len(arr) + k. 
            # Finally, we have to account for range automatically - 1 on our number. We compensate with + 1.
        max_numbers = len(arr) + k + 1

        for i in range(1, max_numbers):
            if i not in nums:
                k -= 1
            
            if k == 0:
                return i
            
        return i

    # Same solution, just converting to a set
    # Time complexity is O(N+k) + N for the set conversion // Space complexity is O(N)
    def findKthPositive(self, arr):
        arr = set(arr)
        # Alternatively, we can remove this and we would have higher time complexity (N * (len(arr) + k)) due to searching the array, but we would also have O(1) space complexity
        
        max_numbers = len(arr) + k + 1
        
        for i in range(1, max_numbers):
            if i not in arr:
                k -= 1
                
            if k == 0:
                return i
            
        return i
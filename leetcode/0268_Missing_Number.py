


# 1: CYCLIC SORT: 1 indexed, 0 as a substitute for the missing number. Cyclic sort is one-pass, in-place sorting. 
# Time complexity: O(N) (total 3N - 1, while loop + swapping (max n - 1) + checking for where zero is)// Space complexity: O(1)
def missingNumber(self, nums):
    # Implement a cyclic sort. We will place every number in its ONE-INDEXED position (eg. [1, 2, 3, 4, 5, etc]) BESIDES 0.
    pos, i = 0, 0
    
    while i < len(nums):
        # The index of where nums[i] is meant to go is given by its value - 1 (eg. we want 1 in the 0 index, 2 in the 1 index (2nd pos), etc). 
        j = nums[i] - 1
        
        # If the number is in the wrong position
        if i != j: 
            # Check if the number is a zero. If it is, make note of which number SHOULD have been there (with i + 1 = pos)
            if nums[i] == 0:
                pos = i + 1
                i += 1
                continue
            # Swap numbers if its not equal to zero
            nums[i], nums[j] = nums[j], nums[i]
        else: 
            i += 1
    return pos


# 2: CYCLIC SORT 2: 0 indexed, n as a substitute for the missing number
# Time complexity: O(N) (total 3N - 1, while loop + swapping (max n - 1) + checking for where n is)// Space complexity: O(1)
def missingNumber(self, nums):
    # Implement a cyclic sort. We will place every number in its ZERO-INDEXED position (eg. [0, 1, 2, 3, 4, etc]) BESIDES the number that equals LEN(NUMS) (as the array is zero indexed, there isn't enough room at the end)
    # Thus, we will NOT sort that number if it exists. Instead, len(nums) will sit where the missing number is meant to be. 
    n = len(nums)
    i = 0
    while i < n:
    # We want i and nums[i] to be equal. 
        j = nums[i]
        # If we sort numbers to their value indices, nums[n] will not fit in this array. Thus, we will skip it, and n will be placed on the MISSING NUMBER's INDEX
        if i != nums[i] and nums[i] < n:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    # Check for which number does not match its index. Alternatively, we could check which number equals n.
    # Time complexity: O(N) // Space complexity: O(1)
    for i, value in enumerate(nums):
        if value == len(nums):
            return i
    # If the whole array is sorted, this means that n itself is missing. 
    return len(nums)


# 3: XOR OPERATOR (exclusive/or operator compares BINARY between two objects; at each position, XOR returns 0 if the bits are the same and 1 if the bits are different (ie. 1 and 0))
    # A property of XOR is that x ^ x = 0, and that x ^ y = y ^ x, and x^(y^z) = (x^y)^z. 
    # Thus, if we XOR every index and number (where all included numbers should have a matching, equal index), we will find the INDEX of the missing number. 
    # Time complexity: O(N) // Space complexity: O(1)
def missingNumber(self, nums):
    # Variable to hold the result
    numxor = 0
    # What we are doing is iterating through all arrays, from 0 to len(nums) - thus, the index that is not included in nums will be the missing number.
    # Note that we are actually starting from index 1 and we iterate OVER the highest index in nums. That is because there might be a number equal to len(nums). Also, we don't have to go over XOR 0 as that just equals the original number. 
    for i, value in enumerate(nums):
        numxor ^= (i + 1) ^ value
    return numxor
        

# 4: GAUSSIAN SUM. Given a list of consecutive natural numbers (1, 2, 3, ... n - 1, n) we can determine the sum by the Gaussian sum formula: n * (n + 1) / 2
    # Thus, we can sum our expected range (1 to n) and then subtract our truncated nums list. Then, we will find our missing number. 

    def missingNumber(self, nums: List[int]) -> int:
        # Between 0 and n, there should be n natural numbers (as 0 is not a natural number). This will be the same size as len(nums) (as although nums is missing a number, it has a 0 in it, adding an extra length)
        # Use Gaussian sum to find sum of array
        n = len(nums)
        
        gSum = n * (n + 1) // 2
        
        for num in nums: 
            gSum -= num
        
        return gSum


# UNFINISHED: There are several other solutions with similar time and space complexity
    # Binary search
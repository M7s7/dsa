# There are several, asymptotic solutions to 4Sum: (all Time complexity O(N^3), Space Complexity O(N))

# METHOD 1 - FOR LOOP OVER THREESUM
# Basically, this is 3Sum but with an extra outerloop. Both index loops check for duplicates. Again, when it is initalised, the first instance of a duplicate IS OK on the j loop because nums i and j can be the same. 
# However, if, upon the next initalisation, the number is the same, then j and the previous j would have been the same, which is not allowed. Thus, we skip it. 
# The problem is reduced to a TwoSum eventually. 
def fourSum(nums, target):
    # Sort the array first
    nums.sort()
    # List of quads
    quads = []
    
    # Iterate over each number, leaving 3 spaces for the other numbers
    for i in range(len(nums) - 3):
        # Check for duplicates. For every number, the 3Sum will have calculated all possibilities for that particular index. Thus, duplicate indexes can be skipped.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Now, initiate threeSum. threeSum will be called for every viable index. The index pointer is one to the right of i.
        for j in range(i + 1, len(nums) - 2):
            # Checking for duplicates. First instance of nums[j] and nums[i] being duplicates is FINE. However, if nums[j] and a previous nums[j] is the same, then we will be counting duplicate quadruplets. 
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # Initialise pointers for the subarray beyond i and j pointers. 
            l = j + 1
            r = len(nums) - 1
            
            # TwoSum
            while l < r:
                fourSum = nums[i] + nums[j] + nums[l] + nums[r]
                
                if fourSum == target:
                    quads.append([nums[i], nums[j], nums[l], nums[r]])
                    # Move either pointer, checking if duplicate
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1                    
                # As mentioned in 3Sum, duplicates are automatically filtered out of inequalities   
                elif fourSum < target:
                    l += 1   
                else:
                    r -= 1                      
    return quads


# METHOD 2 - KSUM: RECURSIVE GENERIC SOLUTION
# Same as above, but generalised to the point for any size k subarrays. 
def fourSum(nums, target):
    # Sort the array first
    nums.sort()
    # Results are list of valid answers, quad is the current 4 pointers
    res, quad = [], []

    def kSum(k, start, target):
        # Recursive case. Thus, the function calls itself until k = 2 (where we can do 2Sum)
        if k != 2:
            # For the first pointer, i - we iterate over the array, leaving k - 1 space for the other pointers at the minimum
            for i in range(start, len(nums) - k + 1): 
                # Check for duplicates. If there is a duplicate of a previous index, continue
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Add the number to the temporary pointer list
                quad.append(nums[i])
                # Initially, kSum is called i times recursively. And in every i call, every j is called (still called i in the function, but the argument inserted is i = i + 1 (which is j) and so on for as many k layers until we have 2 pointers left.
                # For every i and j combination, once we simplify to 2Sum, then the function continues.
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()
        
        # Once the function is simplified, then we do 2Sum. For every i and j combination, we check for the target. Remember that the target changes depending on the value of the new pointer (j) - When kSum is called, target is updated to [target - nums[i]]. 
        else:
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                # When we find a combination in 2Sum, we append the two r and l pointers to the quad list (which is currently holding the fixed i and j we are using for this loop). Then, we append all k pointers to the results as a complete list. 
                else: 
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
    # Now that we have defined the function kSum, we have to call it. Since this is fourSum, we call 4. 0 is the index of i that we start with. Target is given. 
    kSum(4, 0, target)
    return res


# My KSum implementation
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        
        def kSum(k, index, target, temp):
            # Base Case
            if k == 2:
                left = index
                right = len(nums) - 1
                
                while left < right:
                    twoSum = nums[left] + nums[right]
                    if twoSum == target:
                        output.append(temp + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    
                    elif twoSum < target: 
                        left += 1
                    
                    else:
                        right -= 1
                return
             
        # Recursive case
            for i in range(index, len(nums) - 2):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i], temp)
                # Need backtracking
                temp.pop()       
        kSum(4, 0, target, [])
        
        return output

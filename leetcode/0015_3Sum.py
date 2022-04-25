# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Approach: Start on every index of the array. For the right side of that index, do two-sum to try to find a total sum of 0 between all three numbers.
# To prevent duplicate triplets, implement conditionals that skip duplicated numbers. Only included in index checking and when the sum == 0 (comments explain)
# Time complexity is O(N^2) (technically + O(nlogn) due to sorting) // Space complexity is O(N) due to sorting

def threeSum(nums):
    # Sorting is required for two-pointers
    nums.sort()
    triplets = []
    # Iterate over array, creating subarrays to two sum + this number
    for index in range(len(nums) - 2):
        # Check for duplicates
        if index > 0 and nums[index] == nums[index - 1]: 
            continue
        # Initialise pointers to search through the rest of the subarray to the right of index
        left = index + 1
        right = len(nums) - 1
        
        # Do two-sum over the numbers between left and right pointers (inclusive)
        while left < right: 
            threeSum = nums[index] + nums[left] + nums[right]
            if threeSum == 0: 
                triplets.append([nums[index], nums[left], nums[right]])
                # Solution has been found - move pointers
                left += 1
                right -= 1
                # Check pointers for duplicates. We can get away with only incrementing one pointer as we will create an inequality that will only change if the duplicate number changes. 
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            # As noted before, duplicate numbers that create an inequality are removed naturally through the two-pointer process
            elif threeSum < 0: 
                left += 1
            else: right -= 1
    return triplets

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Return k after placing the final result in the first k slots of nums.

def removeDuplicates(self, nums: List[int]) -> int:
    # Initiate pointers: next is the index where the next non-duplicate should go, index is the index currently being iterated over
    next, index = 0, 0
    # Loop over the array
    for index in range(len(nums)):
        # Condition - if arr[index] is not a duplicate of arr[k], place it contiguously in the new array. Since array is sorted, we can use an inequality
        if nums[index] > nums[next]:
            next += 1
            nums[next] = nums[index]
    # 'next' is the index position of the last item in the non-duplicate array. Since it is zero-indexed, add 1 to get length
    k = next + 1
    return k
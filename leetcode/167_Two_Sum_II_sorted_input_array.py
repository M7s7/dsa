# Given a 1-indexed array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target. Return the indices.
# Time complexity: O(N) // Space complexity: O(1)

def twoSum(numbers, target):
    # Create left and right pointers
    left = 0
    right = len(numbers) - 1
    
    # While loop, when pointers still have not iterated over the entire array:
    while right > left:
        # Track total Sum and create conditionals to move pointers
        totalSum = numbers[left] + numbers[right]
        if totalSum == target:
            return left + 1, right + 1
        if totalSum > target:
            right -= 1
        else: 
            left += 1
    return left + 1, right + 1
    
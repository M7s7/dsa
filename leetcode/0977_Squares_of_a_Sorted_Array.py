# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
# Pointers on opposite sides of the array, and keep taking the largest absolute value until the entire array is iterated through.
# Can do this multiple ways, but creating a dummy list instead of list reversal seems the most efficient as it is purely O(N).
# Time complexity is O(N) // Space complexity is O(N)

def sortedSquares(self, nums: List[int]) -> List[int]:
    # Create left and right pointers
    left = 0
    right = len(nums) - 1
    # Create insertion index in the square array
    index = len(nums) - 1

    # Create array of len(arr) with dummy values, replacing values in this array with final values
    square = [0 for i in range(len(nums))]

    # Move pointers until they converge, iterating over the entire array
    while left < right:
        # Place larger square in right-most index then move pointer
        if abs(nums[left]) > nums[right]:
            square[index] = nums[left]**2
            left += 1
        else: 
            square[index] = nums[right]**2
            right -= 1
        # Move the index down 1
        index -= 1
    return square
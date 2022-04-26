# Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.
# Same as equivalent in leetcode (713) but returns a list of combinations. I used string slicing and appending elements to add to the list. Apparently you can use a deque and a temp_list instead of string slicing. 
# Time complexty is O(N^3) (for loop * N^2 (apparently creating subarrays can take N^2 time). Space complexity is O(N)

def main():
    arr = [8, 2, 6, 5]
    target = 50
    print(find_subarray(arr, target))


def find_subarray(arr, target):
    # If k is 1, there are no solutions (as product can never be 0)
    if target <= 1: 
        return 0

    # List of answers
    ans = []
    product = 1
    left = 0
    
    # Increment over the array
    for right in range(len(arr)):
        product *= arr[right]

        # Make sure the window is valid
        while product >= target:
            # Remove the left element
            product /= arr[left]
            left += 1
        
        # Append the answers to the list
        if product < target:
            for i in range(right - left + 1):
                ans.append(arr[left + i: right + 1])
    return ans


main()

## DEQUE ANSWER FROM GROKKING
from collections import deque

def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left < len(arr)):
      product /= arr[left]
      left += 1
    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from lef to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
    temp_list = deque()
    for i in range(right, left-1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()

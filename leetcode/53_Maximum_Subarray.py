# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. This solution uses Kadane's algorithm. 
# Time: O(N) // Space: O(1)

def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maximum_subarray(arr))


def maximum_subarray(arr):
    # Initiate variables - max_sum might be negative so set it to a number in the array to be safe
    max_sum, current_sum = arr[0], 0
    
    # Iterate over the numbers in the array
    for num in arr:
        # Discard the previous current sum if it is negative (this will cull the left-most number if negative, and the whole subarray to the left if its total is negative)
        if current_sum < 0:
            current_sum = 0

        # Add new element to current sum
        current_sum += num

        # Find max, using the current sum
        max_sum = max(max_sum, current_sum)
    return max_sum
        

main()
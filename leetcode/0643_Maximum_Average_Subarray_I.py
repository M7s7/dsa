# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Time complexity: O(N) // Space complexity: O(1)
import math

def main():
    arr = [1,12,-5,-6,50,3]
    k = 4
    print(max_avg_subarray(arr, k))


def max_avg_subarray(arr, k):
    # Initialise variables - maxSum has to be negative inf to account for neg. maxSums
    i, windowSum, maxSum = 0, 0, float(-math.inf)
    # Create a loop to iterate over the array
    for j in range(len(arr)):
        windowSum += arr[j]

        # Condition check - if windowlength has reached k length 
        if j + 1 >= k:
            # Tracking max sum
            maxSum = max(maxSum, windowSum)
            # Remove left number
            windowSum -= arr[i]
            i += 1
    return maxSum / k

main()
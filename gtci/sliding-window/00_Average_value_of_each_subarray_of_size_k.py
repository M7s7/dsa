# Given an array and a positive number k, find the average value of each subarray of size k. 
# This uses a classic static size sliding window. By keeping a running windowSum, we can calculate each value by just adding the added element and subtracting the element directly left to windowStart. 
# Time complexity is O(N). Space complexity is, I think, O(N) (as you keep a store of averages which, when N is large, is just under N size).

def main():
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    print(find_averages_of_subarrays(k, arr))


def find_averages_of_subarrays(k, arr):
    # Initialise variables
    windowSum, windowStart = 0, 0
    # Create list of averages
    avg = []
    # Go through the entire array
    for windowEnd in range(len(arr)):
        # Add each element to the sum
        windowSum += arr[windowEnd]

        # Check if condition is reached (when windowEnd is indexed at K-1, it means that the window is at K length)
        if windowEnd >= k - 1: 
            # Calculate average of window, and then add it to the list
            windowAvg = windowSum / k
            avg.append(windowAvg)
            # If condition is reached, the windowStart element must be removed (as an element is added every iteration)
            windowSum -= arr[windowStart]
            # Move the windowStart element up one
            windowStart += 1
    # Return the list
    return avg

main()
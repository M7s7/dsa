# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
# This is my personal implementation of the solution, tracking the location of where the 1s are to efficiently move windowStart when shrinking the window. However, this solution is suboptimal as it does it slightly faster without all the confusion.
# In other words, the windowStart does not really matter, as long as it maintains the window size or stays the same. 
def main():
    arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3
    print(length_of_longest_substring(arr, k))


def length_of_longest_substring(arr, k):
    # Initiate variables
    windowSum, windowStart, i, max_length = 0, 0, 0, 0
    # Dictionary to store locations of 1s in array
    location = []
    # Loop to iterate over the array
    for windowEnd in range(len(arr)):
        # Implement running sum to count how many times 1 has appeared in the array
        windowSum += arr[windowEnd]
        # If the location is a 1, record where the location is in a list
        location.append(windowEnd)
        # Check the condition: If window size is greater than windowSum + k, then the window is invalid
        if windowEnd - windowStart + 1 > windowSum + k:
            # Removing the first variable from windowStart
            windowSum -= arr[windowStart]
            # Shrink the window maximally by moving windowSum to the next location
            if windowStart == windowEnd: 
                windowStart += 1
            else:
                windowStart = location[i]
                i += 1
    
        max_length = max(max_length, windowEnd - windowStart + 1)
    return max_length
        

main()
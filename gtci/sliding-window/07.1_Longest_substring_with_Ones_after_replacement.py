# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
# The solution will have 1s + k 0s. Thus, we can keep adding the right element and shrinking the window if the size is larger than # of 1s + k. If the condition is not met, then the window grows; otherwise it simply shifts to the right. 
# Time complexity is O(N). Space complexity is O(1) (unlike 06, no hashmap is needed. The sum is equal to frequency)

def main():
    arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3
    print(length_of_longest_substring(arr, k))


def length_of_longest_substring(arr, k):
    # Initiate variables
    windowSum, windowStart = 0, 0
    # For loop to iterate over array, adding elements from the right
    for windowEnd in range(len(arr)):
        # Running sum is how many 1s are in the window
        windowSum += arr[windowEnd]

        # Conditional - when window size is larger than # of 1s + k, then the window is invalid. This means that the window has to shrink
        if windowEnd - windowStart + 1 > windowSum + k: 
            # Remove the first digit from the windowSum
            windowSum -= arr[windowStart]
            # Move window forward one
            windowStart += 1
    # again, since the window does not shrink (and only gets larger if more ones are added later), the length of the final window will be the maximum
    return windowEnd - windowStart + 1


main()
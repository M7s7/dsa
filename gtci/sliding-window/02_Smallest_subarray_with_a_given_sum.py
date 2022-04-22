# Given an array and a positive number S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S. Return 0 if no such subarray exists. 
# This function uses the 'sliding window' computational technique. Initialising windowStart at index zero, dynamically slide the windowEnd until the subarray >= S. Once this is found, the windowStart and check if this subarray > S. If it does, this is the minimum size at this array[windowStart + 1]. If not, slide the windowEnd until the subarray >=S. Continue until windowEnd is the array length. 
# Time complexity is O(N) (technically O(N+N) because of the while loop). Space complexity is O(1). 
def main():
    arr = [2, 1, 5, 2, 8]
    s = 7
    print(smallest_subarray_with_given_sum(s, arr))

def smallest_subarray_with_given_sum(s, arr):
    # Initialise variables (min_length should be initialised at a number greater than len(arr) so there are no false positives if there is no solution
    windowSum, windowStart, min_length = 0, 0, len(arr) + 1
    # Initialise windowEnd at index 0 and increment windowEnd over the array (indexed at 0)
    for windowEnd in range(len(arr)):
        # Continue adding the iterated window-end indexed array to the sum
        windowSum += arr[windowEnd]
        # While-loop conditional (when condition is reached)
        while windowSum >= s:
            # Find current minimum between: 1- length of window (which is just windowEnd - windowStart + 1) and 2- current min length (which is initialised at an impossible number just in case)
            min_length = min(windowEnd - windowStart + 1, min_length)
            # Remove first element from window (which is windowStart, and initialised at 0) from windowSum, and run the algo again
            windowSum -= arr[windowStart]
            # Move windowStart up one element because this is the new index for the subarray (as the first element has been removed)
            windowStart += 1
    # After the entire array has been gone over, return min_length. Make sure the emergency condition is checked
    if min_length > len(arr):
        return 0
    return min_length


main()
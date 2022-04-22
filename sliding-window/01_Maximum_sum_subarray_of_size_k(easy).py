# Given an array and a positive number K, find the maximum sum of any subarray of size K. // 
# This function uses the 'sliding window' computational technique. The window size is added until it reaches size K. After that, the first element is cut off. 
# Time complexity is O(N). Space complexity is O(1).
def main():
    k = 2
    arr = [2, 3, 4, 1, 5]
    print(max_sub_array_of_size_k(k, arr))


def max_sub_array_of_size_k(k, arr):
    # Initialise a running total for the window and max score
    windowSum, maxSum = 0, 0
    # The far-right of the window (aka windowEnd) will iterate over the entire array. 
    for windowEnd in range(len(arr)):
        # Extend windowEnd on every iteration, adding the next element to the windowSum. 
        windowSum += arr[windowEnd]       
        # Once windowEnd extends beyond k size (ie. when windowEnd = k (as it is +1 size due to zero indexing)) then we have to remove the leftmost number. 
        if windowEnd >= k: # Once windowEnd is k or larger, it means that the size of the window is k+1 or larger (again due to zero indexing). Thus, an element will have to be subtracted every iteration. 
            # Remove the first digit in the array. 
            windowSum -= arr[windowEnd - k]
        # Making sure to store the largest windowSum in max, and return it to main. 
        maxSum = max(maxSum, windowSum)
    return maxSum


main()

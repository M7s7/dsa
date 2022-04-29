# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# This question is the same concept as 'longest substring with k replacement'. However, we can use sum instead of calculating the frequency of characters (as it is only 1 and 0).
# There are multiple ways to implement this idea.
# These methods have: Time complexity: O(N) (N+N because left/right pointers can traverse the array) // Space complexity: O(1)

# METHOD 1: The largest sum of the valid window is also the largest window size. If condition is not met, shrink the left side until the window is valid again. 
def longestOnes(self, nums: List[int], k: int) -> int:
    # Variables
    windowSum = 0
    left = 0
    maxOnes = 0
    
    # Iterate through numbers array
    for right in range(len(nums)):       
        # Add new element to windowSum
        windowSum += nums[right]
        
        # If window is invalid, correct it until it is valid
        while windowSum + k < right - left + 1:
            # Note, this could be replaced by saying (if nums[left] = 1: windowSum -= 1).
            windowSum -= nums[left]
            left += 1 
        # No need for else condition because of reason below:
        # After the while loop, the window is 1) either valid or 2) there was no valid window (meaning the left pointer is len(nums + 1). Thus, maxOnes remains, correctly, at 0. 
        maxOnes = max(maxOnes, right - left + 1)
    return maxOnes

# METHOD 2: We can take the approach of never actually shrinking the window. 
# By changing the 'while' statement into an 'if' statement, the window will never shrink past the size of the last valid window as a new element will be added on the next forloop.
# Because the window never shrinks past the largest valid solution, the maximum window will be the same as the size of the window at the end of the function. 
def longestOnes(self, nums: List[int], k: int) -> int:
    # Variables
    windowSum = 0
    left = 0

    # Iterate through numbers array
    for right in range(len(nums)):
        # Add new element to windowSum
        windowSum += nums[right]

        # If window is invalid, shrink it until it is the size of largest valid window. Then, add another element and recheck if a bigger one is valid
        if windowSum + k < right - left + 1:
            if nums[left] == 1:
                windowSum -= 1
            left += 1
    return right - left + 1
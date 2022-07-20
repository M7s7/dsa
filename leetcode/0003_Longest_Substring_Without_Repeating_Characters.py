# Given a string s, find the length of the longest substring without repeating characters.
# The efficient methods use SLIDING WINDOW techniques.

# METHOD 1: Sliding window: Hashmap storing locations
# This is the optimal solution. Create a hashmap to store every letter's location, and when a duplicate is found, we can directly shrink the window, avoiding that letter.
# However, make sure that you aren't moving the pointer backwards by taking a MAX. 
# Time complexity: O(N)
# Space complexity: O(min(m, n)) where m is 26 and n is the string length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        indices = {}
        for i, char in enumerate(s): 
            if char in indices:
                l = max(l, indices[char] + 1)
            indices[char] = i       
            curr_length = i - l + 1
            max_length = max(max_length, curr_length)
        return max_length


# METHOD 2: Sliding window: Hashmap storing frequency
    # Create a hashmap of frequency
def lengthOfLongestSubstring(self, s: str):
    freq = {}
    left = 0
    max_length = 0
    
    # Iterate over the string
    for right, char in enumerate(s):
        # Shrink the left side of the window until the duplicate is removed
        while char in freq:
            if s[left] in freq:
                del freq[s[left]]
            # Keep moving the left pointer until a duplicate is found
            left += 1
        # In either case, store the frequency
        freq[char] = True
        max_length = max(max_length, right - left + 1)
    return max_length


## The other method is BRUTE FORCE by searching every substring. Time complexity is n^3.
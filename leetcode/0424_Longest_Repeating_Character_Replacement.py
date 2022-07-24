# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.


# Sliding window. We will keep our most frequent char in the window, and replace the others. 
    # Time Complexity: O(N)
    # Space Complexity: O(1) - max of 26 for the hashmap
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        for i, char in enumerate(s):
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
                
            # Check if invalid window. If invalid, slide left pointer. 
            window_size = i - l + 1
            if window_size > max(freq.values()) + k:
                freq[s[l]] -= 1
                l += 1
        # Our window never decreases, but will only increase if the window is valid. Thus, we can return the final window
        return i - l + 1
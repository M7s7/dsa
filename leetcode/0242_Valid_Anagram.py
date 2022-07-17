# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Approach 1: Frequency hashmap. We can get away with only using one hashmap.
    # Time Complexity: O(N) (2N for hashmap + string iteration)
    # Space Complexity: O(N) max 26
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Greedy check
        if len(s) != len(t):
            return False

        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        for char in t:
            if char in freq:
                freq[char] -= 1
                if freq[char] == 0:
                    del freq[char]
            else:
                return False

        if len(freq) == 0:
            return True
        return False

# Approach 2: Sorting. Instead, we can sort both strings, then compare. 
    # Time Complexity: O(N log N)
    # Space Complexity: O(N) for sorting
def isAnagram(self, s, t):
    # Strings do not have a .sort method. Instead, we use 'sorted' which works on iterable objects
    return sorted(s) == sorted(t)
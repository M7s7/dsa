# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Approach 1: Frequency hashmap. We can get away with only using one hashmap.
    # Time Complexity: O(N) (2N for hashmap + string iteration) // Space Complexity: O(N) max 26
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Frequency hashmap of string
        freq = {}
        
        # Iterate over string and record frequency
        for char in s:
            if char not in freq:
                freq[char] = 1
            
            else:
                freq[char] += 1
        
        # For the second string, iterate over each character and remove freq from the hashmap
        for char in t:
            if char in freq:
                freq[char] -= 1
                
                # If the char is empty, we have 'completed' the letter so delete it
                if freq[char] == 0:
                    del freq[char]
            
            # If the letter does not exist in the hashmap, return False
            else:
                return False
        
        # If the hashmap is empty, it means that we have a complete match of letter frequency
        if len(freq) == 0:
            return True
        
        # If there are still letters, it means that string s had more letters than t. Return False
        return False
    
    ### Alternatively, we can simplify the code by checking if the strings are the same length at the start:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Frequency hashmap of string
        freq = {}
        
        # Iterate over string and record frequency
        for char in s:
            if char not in freq:
                freq[char] = 1
            
            else:
                freq[char] += 1
        
        # For the second string, iterate over each character and remove freq from the hashmap
        for char in t:
            if char in freq:
                freq[char] -= 1
                
                # If the char is empty, we have 'completed' the letter so delete it
                if freq[char] == 0:
                    del freq[char]
            
            # If the letter does not exist in the hashmap, return False
            else:
                return False
        
        return True


# Approach 2: Sorting. Instead, we can sort both strings, then compare. 
    # Time Complexity: O(N log N) // Space Complexity: O(N) for sorting
def isAnagram(self, s, t):
    # Strings do not have a .sort method. Instead, we use 'sorted' which works on iterable objects
    return sorted(s) == sorted(t)
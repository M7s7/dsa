# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# Create a frequency hashmap and iterate over the string until matching == size of hashmap. Make sure to shrink window when it becomes larger than the anagram length.
# Time complexity: O(N + M) for both strings; Space complexity: O(N + min(26, M))

def findAnagrams(self, s: str, p: str):
    # Create list of answers
    index = []
    # Amount of matching letters
    match = 0
    # Starting pointer initiated at index = 0
    start = 0
    
    # Create a frequency hash-map. Store frequencies of pattern
    freq = {}
    for char in p:
        if char not in freq:
            freq[char] = 1
        else: freq[char] += 1
        
    # Iterate over the string - use a range loop as the index of the character is important.
    for i in range(len(s)):
        # Compare character to frequency in hashmap to see if it is part of the string. NB: Can use 's[i] in p' as a conditional instead
        if s[i] in freq:
            freq[s[i]] -= 1                
            if freq[s[i]] == 0:
                match += 1
                
        # Once the window is too large, start culling letters
        if i > len(p) - 1:
            # Cull first letter by moving a starting pointer forwards, updating the hashmap
            if s[start] in freq:
                if freq[s[start]] == 0: 
                    match -= 1
                freq[s[start]] += 1
            # Move pointer
            start += 1
                
        # Check for a match - must match all letters in hashtable. If matched, append starting index to list
        if match == len(freq):
            index.append(start)
    return index
        
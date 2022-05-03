# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Sliding window: Hashmap approach, storing frequency of pattern. 
# Time complexity: O(N) // Space complexity: O(N)
def checkInclusion(self, s1, s2):
    # We want a window of the size of the permutation, so get size k
    k = len(s1)
    # Start pointer (left pointer for window); match is a counter of how many letters are completely matched
    start = 0
    match = 0
    
    # Hashmap to store frequency of each letter in the pattern string
    freq = {}
    for char in s1:
        if char not in freq:
            freq[char] = 1
        else: freq[char] += 1
    
    # Iterate over the string and add element to the right. If found in hashmap, reduce freq value by 1
    for i, char in enumerate(s2):
        if char in freq:
            freq[char] -= 1
            # If completely matched, we can count 1 for fully matched
            if freq[char] == 0:
                match += 1
        
        # If window size is too big, we reduce it by removing an element from the left
        if i >= k:
            if s2[start] in freq:
                # If letter was already fully matched, remove a match counter (as we are removing the char from the left)
                if freq[s2[start]] == 0:
                    match -= 1
                freq[s2[start]] += 1
            # Remember to shrink the window and move the pointer
            start += 1
        
        if match == len(freq):
            return True   
    return False

## Note: there are other approaches:
    # Brute force (checking every permutation), sorting both strings then comparing, making hashmaps/arrays for equality
    # Another unwieldy way is to make 2 hashmaps for both strings, storing frequency of all letters.
        # Then slide the window to the size of the string and update that strings hashmap. Before we slide, compare the hashmaps.
        # The amount of matching keys is equal to the counter. If the counter == 26, we have a match
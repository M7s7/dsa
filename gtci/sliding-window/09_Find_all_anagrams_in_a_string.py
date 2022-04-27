# Given a string and a pattern, find all anagrams of the pattern in the given string. Return a list of starting indices of the anagramsof the pattern in the given string
# Basically same as permutation in a string - hashmap to store pattern frequency, then check for matching. If matching, then append windowStart to list.
# Time complexity is O(N + M). Space complexity is O(M) to store the pattern; also O(N) to store the results in the worst case. 

def main():
    string = "abab"
    pattern = "ab"
    print(find_string_anagrams(string, pattern))

def find_string_anagrams(str, pattern):
    # Initiate variables
    windowStart, matching = 0, 0
    # Create list to hold the starting indexes of successful matches
    index = []
    # Create hashmap to record frequency of pattern
    chars = {}
    for char in pattern: 
        if char not in chars:
            chars[char] = 1
        else: chars[char] += 1

    # Iterate over the string, adding elements one at a time
    for windowEnd in range(len(str)):
        # If the character in the pattern, update hashtable by removing freq. Also check if hashtable = 0 (indicates a match)
        if str[windowEnd] in pattern: 
            chars[str[windowEnd]] -= 1
            if chars[str[windowEnd]] == 0:
                matching += 1
        
        # Keep windowsize as size len(pattern) which will confirm that the pattern is contiguous in the substring. 
        if windowEnd >= len(pattern):
            # Removing first char: Check if element was in pattern
            if str[windowStart] in pattern:    
                # Then, if it was fully matched char, update matching
                if chars[str[windowStart]] == 0:
                    matching -= 1
                # Update frequency hashmap
                chars[str[windowStart]] += 1
            # Shrink the window
            windowStart += 1
        
        # Check if anagram is fully matched in substring. If so, append windowStart to the table
        if matching == len(chars):
            index.append(windowStart)
    return index


main()
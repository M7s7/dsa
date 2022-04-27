# Given a string and a pattern, find out if the string contains any permutation of the pattern, and print True if true. 
# Static window slides out to len(pattern). Hash table stores frequency of characters of pattern and changes depending on the characters in the window. Matching variable confirms that each unique character has been completely found in the window. 
# Time complexity is O(N + M) (two loops iterating through len of string (N) and pattern (M)). Space complexity is O(M) (storage of M items in chars dict)

def main():
    string = "eidboaoo"
    pattern = "ab"
    print(find_permuation(string, pattern))


def find_permuation(str, pattern):
    # Variables - Matching variable refers to how many letters have been matched 
    windowStart, matching = 0, 0
    # Store frequency of all characters in hashtable (aka the substring must meet these frequencies to be valid)
    chars = {}
    for char in pattern:
        if char not in chars:
            chars[char] = 1
        else: chars[char] += 1

    # Iterate over the string until desired window size is reached
    for windowEnd in range(len(str)):
        # Check to see if the added letter is in the pattern. If it is, subtract a frequency from the hashtable
        if str[windowEnd] in pattern: 
            chars[str[windowEnd]] -= 1
            # If the frequency of the character in the hashtable is 0, it means that the character appears the same times in the window as it does in the pattern. Thus, a preliminary match is found
            if chars[str[windowEnd]] == 0:
                matching += 1

        # Keep the windowsize equal to the patternsize. This will ensure that the letters of the pattern are contiguous in the substring when checking their presence. 
        if windowEnd >= len(pattern):
            # Remove the left character to maintain the size of the window, checking if it was a character in the pattern 
            if str[windowStart] in pattern: 
                # Check first if the character was matching. If so, subtract 1 from matching as the character is being removed.
                if chars[str[windowStart]] == 0:
                    matching -= 1
                # Add back the frequency to the talbe.
                chars[str[windowStart]] += 1
            # Shrink the window to maintain size of len(pattern)
            windowStart += 1
        
        # Check to see if the window has the entire permutation - If matching matches len(chars), it means that all the elements in the dictionary = 0 and everything is matching
        if matching == len(chars): 
            return True
    return False


main()

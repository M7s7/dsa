# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


# Backwards iteration through the array, checking if we touch a space
    # Time Complexity: O(N)
    # Space Complexity: O(1)
def lengthOfLastWord(self, s: str) -> int:
    length = 0
    for i in reversed(range(len(s))): # alternatively, can say 'range(len(s) -1, -1, -1)'
        # Don't count leading spaces
        if s[i] == ' ' and length != 0: 
            return length
        elif s[i] != ' ':
            length += 1
    
    return length
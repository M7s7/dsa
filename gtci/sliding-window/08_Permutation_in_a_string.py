# Given a string and a pattern, find out if the string contains any permutation of the pattern.
# Sliding window implementation: Slide out the window to a fixed length len(pattern) and keep it this long. Record any instances of the pattern in char_list while iterating. 
# BIG ISSUE IN THIS CODE: Since list length is used to determine if substring is in here, the function will return true if string = aa and pattern = ab.  

def main():
    string = "eidboaoo"
    pattern = "ab"
    print(find_permuation(string, pattern))


def find_permuation(str, pattern):
    # Initialise variables
    windowStart = 0
    # Create list of pattern characters - dictionary may not work if there are duplicate characters in the pattern
    char_list = []
    # Iterate over the string, creating a window the size of the pattern
    for windowEnd in range(len(str)):
        
        # Check if character is found in pattern
        if str[windowEnd] in pattern: 
            # Store the character in list
            char_list.append(str[windowEnd])
        
        # If the size of the window is longer than the pattern, then we want to remove a letter
        if windowEnd >= len(pattern):
            if str[windowStart] in char_list:
                char_list.remove(str[windowStart])
            # Move the window up one, locking the window size at len(pattern)
            windowStart += 1

        # Check list to see if three characters are in there
        if len(char_list) == len(pattern):
            return True
    return False

        
main()
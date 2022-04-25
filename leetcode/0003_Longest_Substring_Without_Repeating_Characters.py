def main():
    str = "abba"
    print(lengthOfLongestSubstring(str))


def lengthOfLongestSubstring(s):
    # Initiate variables
    i, max_length = 0, 0
    # Create hashmap to store location of variables
    index = {}
    # Increment over the loop
    for j in range(len(s)): 
        # If added character is not unique, move i to just beyond the old index 
        if s[j] in index:
            i = max(i, index[s[j]] + 1)
        # Regardless, store the character in a new location/initial location
        index[s[j]] = j
        # Record the maximum length
        max_length = max(max_length, j - i + 1) 
    return max_length


main()
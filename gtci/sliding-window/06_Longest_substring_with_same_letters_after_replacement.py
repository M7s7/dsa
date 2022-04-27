# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
# This solution uses a dynamic window and a frequency hashmap. The max string length is the most frequent letter + k (number of replacements). 
# This solution is LESS EFFICIENT because we need to go through the entire hashmap when checking for a new maximum. 
# Time complexity is O(N) (technically O(26N) due to searching the hashtable every loop). Space complexity is O(1) (it is O(26) at maximum to store every letter of the alphabet)

def main():
    string = "abccbbababa"
    k = 2
    print(length_of_longest_substring(string, k))


def length_of_longest_substring(str, k):
    # Initalise variables: windowStart, max_freq (tracking the most frequent letter)
    windowStart, max_freq, max_length = 0, 0, 0
    # Initialise frequency hashmap
    freq = {} 
    # Iterate over the array
    for windowEnd in range(len(str)):
        # Check the current character to see if its in the hashmap
        if str[windowEnd] not in freq:
            freq[str[windowEnd]] = 1
        else: freq[str[windowEnd]] += 1
        # After adding, check for frequency of maximum number by going through the hashtable. 
        max_freq = max(freq.values())

        # A window's maximum valid size is the maximum frequency of a letter PLUS the amount of letters you can replace. This condition checks for invalid windows
        if (windowEnd - windowStart + 1) > k + max_freq:
            # Remove left-most element and adjust frequency.
            # Adjust frequency in hashmap
            freq[str[windowStart]] -= 1
            # Shift window up by one. Doing this MAINTAINS the window size of the current max_length. If a new freq_max has been found, the window size will NOT shrink and a new max_length will return. 
            windowStart += 1
        
        # Track what the maximum is
        max_length = max(max_length, windowEnd - windowStart + 1)
    return max_length


main()
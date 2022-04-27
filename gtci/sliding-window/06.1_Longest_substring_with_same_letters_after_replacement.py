# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
# This solution uses a dynamic window and a frequency hashmap. The max string length is the most frequent letter + k (number of replacements). 
# This solution is MORE EFFICIENT because we NEVER have to increment over the hash map to decrement max_freq. Instead, max_freq is only updated if there is a more frequent letter in the window. 
# Also, this solution does not need to store max_length (can implement it in the less efficient solution too)
# Time complexity is O(N). Space complexity is O(1) (it is O(26) at maximum to store every letter of the alphabet)

def main():
    string = "abccbbababa"
    k = 2
    print(length_of_longest_substring(string, k))


def length_of_longest_substring(str, k):
    # Initalise variables: windowStart, max_freq (tracking the most frequent letter)
    windowStart, max_freq = 0, 0
    # Initialise frequency hashmap
    freq = {} 
    # Iterate over the array
    for windowEnd in range(len(str)):
        # Check the current character to see if its in the hashmap
        if str[windowEnd] not in freq:
            freq[str[windowEnd]] = 1
        else: freq[str[windowEnd]] += 1
        # After adding, check for frequency of maximum number. We check frequencies for every index and store if maximum. 
        max_freq = max(max_freq, freq[str[windowEnd]])

        # A window's maximum valid size is the maximum frequency of a letter PLUS the amount of letters you can replace. This condition checks for invalid windows
        if (windowEnd - windowStart + 1) > k + max_freq:
            # Remove left-most element and adjust frequency. IMPORTANT: There is no need to decrement max_freq because a more optimal solution will NEED to have a higher frequency. Thus, if a new solution is found, it will be reflected in line 24.
            # Adjusting frequency is especially important if max_freq is not decremented, as it prevents max_freq from incorrectly increasing for letters out of the window (for example, abbbaaac for k=3 won't incorrectly return A:4)
            freq[str[windowStart]] -= 1
            # Shift window up by one. Doing this MAINTAINS the window size of the current max_length. If a new freq_max has been found, the window size will NOT shrink and a new max_length will return. 
            windowStart += 1
    
    # The max length IS THE SIZE OF THE CURRENT WINDOW. There is no need to track max_length as SIZE OF THE WINDOW NEVER DECREASES. Thus, the window at the end will be the maximum window.
    #  Every loop, the window gets one larger (line 18). However, the window can only shrink one smaller CONDITIONALLY (line 32 in if statement). Thus, the window can only increase on iterations.
    return (windowEnd - windowStart + 1)
    


main()
# Given a string, find the length of the longest substring which has no repeating characters.
# This solution uses a sliding window with a hashmap keeping track of the frequency of each letter. It is not the most efficient solution. 
# Time complexity is O(N) (technically O(N+N) because windowEnd and windowStart both may iterate over the array). Space complexity is O(min(m, n)) where N is the string length and m is size 26 (the alphabet). 

def main():
    string = "abcdefabst"
    print(non_repeat_substring(string))


def non_repeat_substring(str):
    # Initialise variables
    windowStart, max_length = 0, 0
    # Create hashmap to store frequency of characters
    freq = {}
    # Iterate over the array
    for windowEnd in range(len(str)):
        # Add rightmost element to hashmap
        if str[windowEnd] not in freq:
            freq[str[windowEnd]] = 1
        else: freq[str[windowEnd]] += 1
        
        # Conditional while loop, checking to see if newest added character is unique
        while freq[str[windowEnd]] > 1:
            # Remove the first letter and recheck the condition
            freq[str[windowStart]] -= 1
            if freq[str[windowStart]] == 0: 
                del freq[str[windowStart]]
            # Shrink window by one and recheck the condition
            windowStart += 1

        # Update maximum length
        max_length = max(max_length, windowEnd - windowStart + 1)
    return max_length


main()
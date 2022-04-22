# Given a string and a positive number k, find the longest substring with, AT MOST, k distinct characters.   
# This problem uses a dynamic window to constantly slide the windowEnd, checking for the condition. Once the condition is found, the first element is cut and windowStart moves up a place, checking the conditional again (with the while loop). 
# Compared to 02, the trick in this problem is using a HASHMAP to track the conditional. 

def main():
    string = "cbbebi"
    k = 2
    print(longest_substring_with_k_distinct(string, k))


def longest_substring_with_k_distinct(str, k):
    # Initialise variables
    windowStart, max_length = 0, 0
    # Create hashmap to keep track of word frequency, checking whether or not they are in the current substring
    freq = {}

    # windowEnd will go over the entire string, adding a character on every iteration
    for windowEnd in range(len(str)):
        # If the character is not in the frequency hashmap yet, add it and initialise it with 1 frequency
        if str[windowEnd] not in freq:
            freq[str[windowEnd]] = 1
            # Otherwise, add one more to the frequency of the character
        else: freq[str[windowEnd]] += 1

        # While loop to check if k has been surpassed (If it hasn't been surpassed, you can pass it on to the max_length function)
        while len(freq) > k: 
            # For the first character of the substring, remove
            freq[str[windowStart]] -= 1
            # Remove the variable from the hashmap if it is 0
            if freq[str[windowStart]] == 0:
                del freq[str[windowStart]]
            # Move windowStart up one, just in case that k > 3
            windowStart += 1

        # The max length is either the current window OR previous max_length
        max_length = max(windowEnd - windowStart + 1, max_length)    
    return max_length


main()
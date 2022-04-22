# Given a string and a positive number k, find the longest substring with, AT MOST, k distinct characters.   
# This problem uses a dynamic window to constantly slide the windowEnd, checking for the condition. Once the condition is found, the first element is cut and windowStart moves up a place, checking the conditional again (with the while loop). 
# Compared to 02, the trick in this problem is using a HASHMAP to track the conditional. 
# Time complexity is O(N) (technically O(N+N) because of the inner while-loop). Space complexity is O(K + 1) (as the dictionary can only hold K + 1 variables before an element is removed)

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

        # While loop to check if k has been surpassed (If it hasn't been surpassed, you can pass it on to the max_length function). if k has been surpassed, we will be shrinking the table by removing the leftmost element and rechecking the loop. 
        while len(freq) > k: 
            # For the first character of the substring, remove a frequency from the dictionary
            freq[str[windowStart]] -= 1
            # Remove the variable from the hashmap if value = 0 (means that it no longer appears in the subwindow)
            if freq[str[windowStart]] == 0:
                del freq[str[windowStart]]
            # Move windowStart up one, shrinking the window. Then check the conditional again with the while loop
            windowStart += 1

        # The max length is either the current window OR previous max_length
        max_length = max(windowEnd - windowStart + 1, max_length)    
    return max_length


main()
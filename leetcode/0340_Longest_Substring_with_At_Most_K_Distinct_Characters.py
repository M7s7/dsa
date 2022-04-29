# Given a string S, find the length of the longest substring T that contains at most k distinct characters.
# Both methods use the same concept - store distinct characters in frequency hashmap. If window is invalid, delete left element and increment hashmap.
# If an element is deleted to 0 frequency, remove it from the hashmap.
# BOTH SOLUTIONS: Time complexity: O(N) (N + N technically) // Space complexity: O(1), but technically (min (26, k))

# METHOD 1: WHILE statement for invalid window. Every loop will return a valid window if it exists. Track what the maximum size seen is and return it. 
# Method 2 is more elegant, but this one is easier to conceptualise. 

def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
    # Create hashmap, where number of keys = distinct characters. We will delete characters if they have 0 frequency
    freq = {}
    # Initiate variables, including tracking the maximum length
    left = 0
    max_length = 0

    if len(s) == 0:
        return 0
    # Iterate over string
    for right in range(len(s)):
        # Add element to hashmap
        if s[right] not in freq:
            freq[s[right]] = 1
        else: freq[s[right]] += 1
    
        # Check condition - if not met, we can remove elements from the left until the window is valid again
        while len(freq) > k:
            freq[s[left]] -= 1
            # Delete the letter if it is no longer in the string
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        
        # Compare the current valid window to the last maximum one
        max_length = max(max_length, right - left + 1)
    
        # Return the maximum value
        return max_length


# METHOD 2: IF Statement for invalid window. This approach never shrinks the window, so we can return the size of the final window as the maximum.
# This method is cleaner in terms of code, but harder conceptually to reach. It is probably slightly faster too as max does not have to be checked

def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
    # Create hashmap, where number of keys = distinct characters. We will delete characters if they have 0 frequency
    freq = {}
    # Initiate variable
    left = 0
    # Fixes an edgecase where the string is empty
    if len(s) == 0:
        return 0
    # Iterate over string
    for right in range(len(s)):
        # Add element to hashmap
        if s[right] not in freq:
            freq[s[right]] = 1
        else: freq[s[right]] += 1
    
        # Check condition - if not met, we can slide the window across, subtracting left element here and adding one element on the next loop
        if len(freq) > k:
            freq[s[left]] -= 1
            # Delete the letter if it is no longer in the string
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

    # After the array has been passed through, we need to return the length of the string 
    # Remember, since every loop is at MAXIMUM +0 MINIMUM +1 in window size, the ending window size will always be the maximum.
    return right - left + 1  

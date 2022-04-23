# Given a string, find the length of the longest substring which has no repeating characters.
# For a more efficient solution, the hashmap will not be storing frequency of characters. Instead, we store the index of the location of the character in the string. 
# If a duplicate is found, the window is shrunk until the duplication is gone (and windowStart is stored). The substring length can be calculated using the start and end of the window. 
# Time complexity is O(N) (as each element is only touched once). Space complexity is O(min(m, n)) where n is the string length and m is size 26 (the alphabet). 
def main():
    string = "abcdefabst"
    print(non_repeat_substring(string))


def non_repeat_substring(str):
    # Initiate variables
    windowStart, max_length = 0, 0
    # Create hashmap to store indexes of characters
    location = {}
    # Iterate over each character in the string
    for windowEnd in range(len(str)):
        # Check if new character is in the hashmap (aka check if condition is breached)
        if str[windowEnd] in location:
            # If not a unique character, then move location just beyond the index of the first instance of the character
            windowStart = location[str[windowEnd]] + 1
            
        # Update the location of the variable in the hashmap (if character is unique, this just creates a new entry in the hashmap)
        location[str[windowEnd]] = windowEnd

        # Keep track of the maximum length of substring
        max_length = max(max_length, windowEnd - windowStart + 1)
    return max_length


main()
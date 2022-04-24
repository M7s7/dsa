# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
# First implementation - uses a hashmap to hold frequency of chars in pattern. Once pattern has been met (denoted by matching >= lens(chars)), the window will shrink from the left until it is no longer matching. The shortest valid window will be recorded.
# Uses a substring list to store what the shortest substring is at any given point of the iteration and returns it.
# Time complexity is O(N + M) aka O(len(string + pattern)). Space complexity is O(M + N) where M is maximum 26 and N is the space for holding the substring. 

def main():
    string = "aabdec"
    pattern = "abc"
    print(find_substring(string, pattern))

def find_substring(str, pattern):
    # Initialise variables - min_length is a placeholder function to make sure that the smallest length substring is being recorded as the substring
    windowStart, matching, min_length = 0, 0, len(str) + 1
    # Create hashmap, recording frequency of characters in pattern
    chars = {}
    for char in pattern:
        if char not in chars:
            chars[char] = 1
        else: chars[char] += 1

    # Create temporary list to store substring
    substring = []

    # Iterate over the string, updating the hashmap for occurences as we go
    for windowEnd in range(len(str)):
        # Checking and updating hashmap occurances
        if str[windowEnd] in pattern:
            chars[str[windowEnd]] -= 1
            # Last letter will be a match if hashmapped to 0. If it is less, then it has already been accounted for. If it is more, then there needs to be more instances of the letter in the substring.
            if chars[str[windowEnd]] == 0: 
                matching += 1
    
        # Once a complete match is found, shrink the window from the left and recheck the condition using a while loop
        while matching >= len(chars):
            # Store locations of variables
            if windowEnd - windowStart + 1 < min_length:
                # Slice string and store substring. End of substring has to be windowEnd + 1 because slicing will take windowEnd elements, but we want all elements up to index windowEnd (which is windowEnd + 1 elements as the array is 0 indexed)
                substring = str[windowStart:windowEnd + 1]
                min_length = windowEnd - windowStart + 1
            if str[windowStart] in pattern: 
                # Check if this character will be not matching after a frequency is removed:
                if chars[str[windowStart]] == 0:
                    matching -= 1
                # Add back freq of left char
                chars[str[windowStart]] += 1
            # Move windowStart up one
            windowStart += 1
    return "" if substring == [] else substring


main()
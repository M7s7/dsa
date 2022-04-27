# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
# Basically the same as the other solution, but slightly optimised by only storing the substring as a result.
# Time complexity is O(N + M) aka O(len(string + pattern)). Space complexity is O(M + N) where M is maximum 26 and N is the space for holding the substring. 

def main():
    string = "aabdec"
    pattern = "abc"
    print(find_substring(string, pattern))

def find_substring(str, pattern):
    # Initalise variables - sub_start is the starting index of the shortest valid window
    windowStart, matching, min_length, sub_start = 0, 0, len(str) + 1, len(str) + 1
    # Create hashmap with pattern characters, recording frequency
    chars = {}
    for char in pattern:
        if char not in chars:
            chars[char] = 1
        else: chars[char] += 1

    # Increment over the string, adding elements from the right
    for windowEnd in range(len(str)):
        # Check if the character is in the hashmap
        if str[windowEnd] in pattern:
            chars[str[windowEnd]] -= 1
            if chars[str[windowEnd]] == 0:
                matching += 1
    
        # Check condition and shrink window as much as possible until substring is no longer there
        while matching >= len(chars):
            # Record the index of the shortest substring if a new minimum length is reached
            if min_length > windowEnd - windowStart + 1:
                sub_start = windowStart
                min_length = windowEnd - windowStart + 1
            # Update the char list by removing first char
            if str[windowStart] in pattern:
                if chars[str[windowStart]] == 0:
                    matching -= 1
                chars[str[windowStart]] += 1
            # Increment windowStart
            windowStart += 1
    # Return the substring
    return str[sub_start:sub_start + min_length] if sub_start != len(str) + 1 else ""
    

main()

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character. Note that after backspacing an empty text, the text will continue empty.

# METHOD 1 (OPTIMAL): Two pointers 
# Surprisingly difficult question. Optimal solution uses two pointers initiated from the back, which jump to the next valid characters after backspaces have been accounted for. 
# Thus, a valid_char function has been added to take care of the backspaces, incrementing the indices past '#' and past characters when there is a backlog of backspaces built up. 
# Since each valid character is compared contemporaneously, the strings are only valid if they increment to s_p = t_p = -1 (as index 0 is the last character to compare). Anything else and we should return false.
# Time complexity is O(N + M) as we increment over both strings. Space complexity is O(1). 

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Initialise pointers at back of strings
        s_p = len(s) - 1
        t_p = len(t) - 1
        
        # Create loop to iterate through each character. Continue with the loop when at least one of the strings has not been fully iterated through yet
        while s_p >=0 or t_p >= 0:
            # Find the index of the next valid character for both strings (after backspaces are applied)
            s_index = modify_index(s, s_p)
            t_index = modify_index(t, t_p)
            
            # Now, we can COMPARE THE TWO VALID CHARS TOGETHER. 
            # Condition - if both indexes are less than 0, both strings have been fully compared at the same time without triggering a False return. Thus, they are a match. 
            if s_index < 0 and t_index < 0:
                return True
            
            # Condition - if only one string has been iterated through (note that the condition above has not been triggered if this condition is reached), then one string has been fully iterated through while the other has not. Thus, they do not match. 
            if s_index < 0 or t_index < 0:
                return False
            
            # Condition - now, directly comparing the characters - if they don't match, return false. 
            if s[s_index] != t[t_index]:
                return False
            
            # After validly comparing two characters, we increment to the next character. (Remember, if we increment the pointers to invalid characters, the valid_char function will place them on valid characters).
            s_p = s_index - 1
            t_p = t_index - 1
        # If the while loop is broken (eg. we finish comparing matching letters both indexed on 0), then both strings have been fully compared. Thus, return True. 
        return True
    

# This function checks if the index is on a backspace. If so, we count how many backspaces there are and increment the pointers accordingly
def modify_index(string, index):
    # Initiate counter number of consecutive backspaces
    backspace = 0
    # Initiate while loop, searching indexes. Loop stops at index = 0 because there is no character at -1.  
    while index >= 0:
        # When a backspace is found, increment variable by 1. Note that each backspace
        if string[index] == "#":
            backspace += 1
        # Since each backspace means delete a character, we can delete a character when encountered
        elif backspace > 0:
            backspace -= 1
        # If there are no backspaces, break out of the loop
        else:
            break
        # If there are backspaces in the counter or a backspace has been added, we decrement the index.
        # If the index was #, this just gets us past that # to the next character.
        # Else, if there are backspaces, this removes the characters as according to the backspaces
        index -= 1
    # Return the index of the next valid character
    return index


# METHOD 2: STACKS TO BUILD STRINGS
# We can use a function to build the strings, imitating the keystrokes as we go through the use of a stack. 

def backspaceCompare(self, s: str, t: str) -> bool:
    # Create function to make a string of valid characters
    def build_string(string):
        # This list will be used as a stack (LIFO) - appropriate because backspace removes the elements put in LAST.
        valid = []
        # Iterate through the string
        for char in string: 
            # If the character is an actual character, we put it on the stack
            if char != "#":
                valid.append(char)
            # If it is a backspace AND the list is not empty (elif valid returns false if valid is empty), then pop off the char
            elif valid:
                valid.pop()
        return str(valid)
    # Compare strings for bool value
    return build_string(s) == build_string(t)
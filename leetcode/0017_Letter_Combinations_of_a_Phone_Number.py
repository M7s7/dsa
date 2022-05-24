# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# Approach: DFS, using recursion. Can be done iteratively, but recursion is neater.
    # We can imagine this problem as a TREE, where the number of digits determines the number of levels of the tree, and the corresponding letters of the next digit determining the child nodes for the next level. 
    # Time Complexity: O(n * 4^n). amount of digits n * 4^n for worst case recursive call for each digit // Space Complexity: O(n * 4^n) - 4^n possible solutions of size n
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Create a hashmap to map each number to the corresponding letters
        correspondingLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        ans = []
        
        # DFS function must pass through the current digits index that we are on, and the current string created
        def dfs(i, string):
        # Base-case is if we have gotten a string with a letter for each digit. 
            if len(string) == len(digits):
                # Base-case means we have a complete string, so we can terminate this call
                ans.append(string)
                return
            
        # Recursive case - For the current string, we want to call dfs to create a new string for each letter corresponding to the current digit
            # Letters refers to the letters corresponding to the current digit
            letters = correspondingLetters[digits[i]]
            
            # Brute force: For each corresponding letter, call dfs, adding the char and incrementing the digit index
            for char in letters:
                dfs(i + 1, string + char)
        
        # Make sure we do not have an empty array before calling dfs (otherwise, we will return [""] instead of [] for no digits)
        if digits:
            # Calling dfs: Passing through 0 (to check the 0-indexed digit), and an empty string to concatenate to
            dfs(0, "")
        
        return ans
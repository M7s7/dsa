# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.


# Approach 1: BFS. Place each character into the queue. If it is a letter, place it twice in upper and lower. 
    # Append each new letter onto each old array, creating new permutations. Pop off the old ones.
    # Time Complexity: O(N * 2^N) - 2^N different permutations (as each letter can be upper or lower). Each permutation is converted into a string (N time)
    # Space Complexity: O(N * 2^N)
# Note: uses string concatenation - might be inefficient
import collections

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        perms = collections.deque()
        perms.append("")

        for char in s:
            old_sets = len(perms)
            for _ in range(old_sets):
                curr_perm = perms.popleft()
                if char.isalpha():
                    perms.append(curr_perm + char.upper())
                    perms.append(curr_perm + char.lower())
                else:
                    perms.append(curr_perm + char)
        return perms


# Approach 2: DFS
    # Call DFS for each character. If letter, call it on both upper and lower variations. 
    # Time Complexity: O(N * 2^N) same as above
    # Space Complexity: O(N * 2^N) Same as above
# NO BACKTRACKING VARIATION - uses string concatenation (less time efficient as string concatenation is m + n)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        all_perms = []
        
        def dfs(i, perm):
            # Base case - indexed out of string
            if i >= len(s):
                all_perms.append(perm[::])
                return
            
            # Recursive case
            if s[i].isalpha():
                # Call dfs upper and lower case
                dfs(i + 1, perm + s[i].upper())
                dfs(i + 1, perm + s[i].lower())
            # Else, if numerical
            else:
                dfs(i + 1, perm + s[i])
            
        dfs(0, "")
        return all_perms

# BACKTRACKING VARIATION - uses string-builder for time complexity efficiency
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        all_perms = []
        
        def dfs(i, perm):
            # Base case - indexed out of string
            if i >= len(s):
                # Join method to stringbuild - create a string
                all_perms.append(''.join(perm))
                return
            
            # Recursive case
            if s[i].isalpha():
                # Call dfs upper and lower case
                perm.append(s[i].upper())
                # Call 1: Upper case
                dfs(i + 1, perm)
                # Remember to pop off the upper case variation before adding the lower case variation
                perm.pop()
                # Call 2: Lower case
                perm.append(s[i].lower())
                dfs(i + 1, perm)
                
            # Else, if numerical
            else:
                perm.append(s[i])
                # If numerical, only need to call 1
                dfs(i + 1, perm)
            
            # Backtracking
            perm.pop()
        # Passing through list to build permutations
        dfs(0, [])
        return all_perms
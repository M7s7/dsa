# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Intuition:
    # Once we reach n right brackets, we have finished generating
    # We can only generate right brackets if we have more left brackets
    # We can generate up to n left brackets. 

# Approach 1: DFS Backtracking
    # Uses a stringbuilder. 
    # Time Complexity: Approximately O(N * 2^N) (2^N total permutations, but since there are only some valid combinations, it is bounded by the Catalan number (O(4^n/sqrt(n)))
    # Space Complexity: O(N * 2^N)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        
        def dfs(left, right, path):
            if right >= n:
                combs.append("".join(path))
                return
            
            if left < n:
                path.append("(")
                dfs(left + 1, right, path)
                # Backtrack
                path.pop()
                
            if right < left:
                path.append(")")
                dfs(left, right + 1, path)
                # Backtrack
                path.pop()
                
        dfs(0,0,[])
        return combs


# Approach 2: DFS No backtracking
    # Using string concatenation
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        
        def dfs(left, right, path):
            # Base case
            if right >= n:
                combs.append(path)
                return
        
            # Recursive case
            if left < n:
                dfs(left + 1, right, path + "(")
            
            if right < left:
                dfs(left, right + 1, path + ")")
            
        dfs(0, 0, "")
        return combs

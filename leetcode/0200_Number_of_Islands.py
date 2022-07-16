# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


# DFS recursion. 
    # Time Complexity: O(m*n) - operations
    # Space Complexity: O(m + n) - biggest stackframe
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            # Base case: Out of bounds, or no island
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return 0

            # These recursive calls are to mark pieces of land which make up the same island, so we don't double count. 
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            # Return 1 if we have found land. 
            return 1
        
        islands = 0
        for i in range(m):
            for j in range(n):
                islands += dfs(i, j)
        return islands
                

# DFS recursion - no input modification by using sets. Higher space complexity. 
    # Time Complexity: O(m*n) - operations
    # Space Complexity: O(m*n).
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        def dfs(i, j): 
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0' or (i, j) in visited:
                return 0
        
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
            return 1
        
        islands = 0
        for i in range(m):
            for j in range(n):
                islands += dfs(i, j)
        return islands
                
            
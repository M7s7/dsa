# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

 
 # Recursion. Every time we find land, flood fill all four directions until we exhaust everything.
    # Return the area of each island. Return the maximum. 
    # Time Complexity: O(m*n) - Visit each element in the grid
    # Space Complexity: O(m + n?) - Highest call stack we can get during our recursion? Hard to say what it is, but it seems like both added
 class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        
        def findLand(i, j):
            if i < 0 or j < 0 or i >= m or j>= n or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0           
            curr_area = 1 + findLand(i + 1, j) + findLand(i - 1, j) + findLand(i, j - 1) + findLand(i, j + 1) 
            return curr_area
        
        for i in range(m):
            for j in range(n):
                max_area = max(findLand(i, j), max_area)
        
        return max_area

# Recursion, using a set. 
    # Advantage: Does not modify the input.
    # Disadvantage: Space complexity increases to m*n (if every element is land)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        
        def findLand(i, j):
            if i < 0 or j < 0 or i >= m or j>= n or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0           
            curr_area = 1 + findLand(i + 1, j) + findLand(i - 1, j) + findLand(i, j - 1) + findLand(i, j + 1) 
            return curr_area
        
        for i in range(m):
            for j in range(n):
                max_area = max(findLand(i, j), max_area)
        
        return max_area
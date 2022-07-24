# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following properties:
    # Integers in each row are sorted in ascending from left to right.
    # Integers in each column are sorted in ascending from top to bottom.


# Binary Search on each row.
    # Time Complexity: O(nlogm), where n is number of rows, m is number of columns
    # Space Complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:      
        for row in matrix:
            # Check if row is in range:
            if target >= row[0] and target <= row[-1]:     
                l, r = 0, len(matrix[0]) - 1
                while l <= r:                
                    m = l + (r - l)//2
                    if target == row[m]:
                        return True
                    elif target < row[m]:
                        r = m - 1   
                    else:
                        l = m + 1
        return False


# 'Adaptive Search'. Must start at either top-right or bottom-left, as we can systematically eliminate columns/rows. 
    # We are maxing in one dimension, while minimising the other. 
# If the target is larger, eliminate the column and go left.
# If the target is smaller, eliminate the row and go down. 
    # Time Complexity: O(n+m) - maximum complexity is we go down the entire matrix then across the entire thing
    # Space Complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, n - 1
        while i < m and j >= 0:
            val = matrix[i][j]
            if val == target:
                return True
            if val < target:
                i += 1
            else:
                j -= 1
        return False
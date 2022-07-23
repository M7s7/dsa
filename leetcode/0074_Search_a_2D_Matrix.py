# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following properties:
    # Integers in each row are sorted from left to right.
    # The first integer of each row is greater than the last integer of the previous row.

# BINARY SEARCH SOLUTIONS
# Approach 1: Flatten the matrix into a 1D array.
# We can do this by treating the first element as 0 and continuing from left to right (last element is m * n - 1).
# This number can be divmod'd by the number of elements per row to find index (quotient is row, remainder is column)
    # Time Complexity: O(log(m*n))
    # Space Complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # Number of rows 
        n = len(matrix[0]) # Number of columns (elements per row)
        
        lo = 0 # Set first element as 0
        hi = m * n - 1 # Set last element as (number of elements) - 1
        while lo <= hi:
            mid = lo + (hi - lo)//2 
            # Divmod'ing will give us 
            i, j = divmod(mid, n)
            val = matrix[i][j]
            if val == target:
                return True
            elif val > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
            

# Approach 2: Search for row first, then search for the column. 
# Row search is by checking if the target is between the 'edges' of the row
    # Time Complexity: O(log(m*n)) - note that it is log(m) + log(n), which is the same as log(m*n)
    # Space Complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # Number of rows
        n = len(matrix[0]) # Number of columns

        # Check if our number lies in the search space
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        # Search for target row
        lo = 0
        hi = m - 1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            low_bound = matrix[mid][0]
            high_bound = matrix[mid][-1]
            if low_bound > target:
                hi = mid - 1
            elif high_bound < target:
                lo = mid + 1
            else:
                break
                
        # Loop above exits when we find target row
        row = mid
        lo = 0
        hi = n - 1
        # Search in the row for target element
        while lo <= hi:
            mid = lo + (hi - lo)//2
            val = matrix[row][mid]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1 
            else:
                hi = mid - 1
        return False
# Given an integer numRows (or N), return the first numRows of Pascal's triangle.


# Dynamic Programming. Below is the iterative approach (bottom up), which is the most efficient.
    # Remember that for the jth element on the ith row that is not on the edges, the value is the j-1th and jth elements on the i-1th row.
# Time Complexity: O(N^2), but actually less than that. The complexity is 1 + 2 + 3... + N (for each row)
# Space Complexity: O(N^2) - same as above.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                # Left and right of every row is a 1, so we can append this every time
                if j == 0 or j == i:
                    row.append(1)
                else:
                    # DP: Use the values stored in the previous row to calculate our new numbers
                    row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            pascal.append(row)
        return pascal
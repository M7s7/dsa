# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

    # Time complexity: O(N*M) where N is number of lists and M is size of list as nested forloop // Space Complexity: O(N*M) to hold reversed matrix
# Zip Approach
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Given several lists, zip will create an ITERATOR that will go through the each index of the lists simultaneously. 
        # The asterisk is to UNPACK the single list of lists into several lists. Then, we can iterate through those lists.
        return zip(*matrix)
    
# Traditional Approach
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Number of rows and columns in our original matrix - these will be reversed during transposition
        rows = len(matrix)
        columns = len(matrix[0])
        
        # Print a placeholder matrix of the transposed matrix - the amount of rows is len(columns), and each row has len(rows) elements
        output = [[None] * rows for _ in range(columns)]
        
        # Go through the matrix
        for i in range(rows):
            for j in range(columns):
                output[j][i] = matrix[i][j]
        
        return output
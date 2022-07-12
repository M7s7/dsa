# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# You must find a solution with a memory complexity better than O(n^2).


# Binary Search TBC

# Heap (Priority Queue). 
    # We start at the smallest number. Whenever we reach a current smallest number, we add the candidates for the next largest number to the heap. 
        # One possibility would be the number directly to the right, as the lists are sorted.
        # Another possibility would be a number on a row directly below the current row. 
    # Time Complexity: O(klogn), where n is the maximum heap size for k operations until we have the smallest number.
    # Space Complexity: O(n). Largest the heap gets is if we keep going directly down (adding 2n elements and subtracting n elements from the heap)
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = [(matrix[0][0], 0, 0)] # Store tuples (val, x, y)
        n = len(matrix)
        counter = k
        while min_heap and counter > 0:
            num, row, col = heapq.heappop(min_heap)
            counter -= 1
            # Check number below. Note that we only have to move down once per row (a maximum of n times), as after we go down once, we can access the whole row by going right. 
            if row < n - 1 and col == 0:
                heapq.heappush(min_heap, (matrix[row + 1][col], row + 1, col))
            # Check the number to the right. 
            if col < n - 1:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))                   
        return num


# Sorting. We can flatten the 2D array into a 1D array, then sort it and return the k - 1 index. 
    # Time Complexity: O(N^2). Extend will be (N^2 - N), sorting will be N^2log(N^2)
    # Space Complexity: O(N^2)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        for i in range(1, len(matrix)):
            matrix[0].extend(matrix[i])
        matrix[0].sort()
        
        return matrix[0][k - 1]
        
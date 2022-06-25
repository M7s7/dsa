# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# Approach: Bitwise operation. Reverse every row - while swapping, invert bit. 
    # Time Complexity: O(N^2) - Nested loop - N columns * N rows
    # Space Complexity: O(1)

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])
        for i in range(n):
            left, right = 0, n - 1
            while left <= right:
                image[i][left], image[i][right] = image[i][right] ^ 1, image[i][left] ^ 1
                left += 1
                right -= 1
        return image


# Small optimisation: If the left and right bits are different (ie. 0 and 1), when they are reversed and inverted, they are the same as they were originally. 
    # If the bits are the same, then they are simply inverted on both sides.
    # Thus, we can save some unneccesary operations if we only invert/swap when the numbers are the same. 
    # Space/Time complexity is the same. 
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])
        for i in range(n):
            left, right = 0, n - 1
            while left <= right:
                if image[i][left] == image[i][right]:
                    image[i][left], image[i][right] = image[i][left] ^ 1, image[i][right] ^ 1 # Done as a swap instead of two toggles to account for edge case that left and right are the same index
                left += 1
                right -= 1
        return image
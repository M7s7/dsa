# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


# Sliding Window
# First, slide the window to k length on one side and get the total sum. 
# Then, from the other side, begin to slide the window k length. Every time we add a number from the other end, 'remove' the deepest card from the original end
    # Time Complexity: O(k) - 2k for summing each side
    # Space Complexity: O(1)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # This variation uses sum() - thus, we don't need a left pointer to sum. However, we can initiate its index to subtract. 
        left, right = k - 1, len(cardPoints) - 1
        curr_sum = max_sum = sum(cardPoints[:k]) # Alternatively, we could go through a loop 

        # This loop adds the other end of the array        
        for _ in range(k):
            # Add right element and subtract deepest left element
            curr_sum += cardPoints[right] - cardPoints[left]
            max_sum = max(max_sum, curr_sum)
            right -= 1
            left -= 1
        
        return max_sum
        
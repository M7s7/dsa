# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:
    # horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
    # verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.


# Sort cuts. Then find biggest distance between all vCuts (including edges), and hCuts (including edges)
    # The answer is the multiple between the two. 
        # Time Complexity: O(nlogn) for sorting. 2nlogn + 2N
        # Space Complexity: O(N). 2N for sorting
class Solution:
    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:
        vCuts.sort()
        hCuts.sort()
        max_width = max(vCuts[0], w - vCuts[-1])
        max_height = max(hCuts[0], h - hCuts[-1])
        
        for i in range(1, len(vCuts)):
            max_width = max(vCuts[i] - vCuts[i - 1], max_width)
        
        for i in range(1, len(hCuts)):
            max_height = max(hCuts[i] - hCuts[i - 1], max_height)
            
        return (max_height * max_width) % (7 + 10 ** 9)
        
        
        
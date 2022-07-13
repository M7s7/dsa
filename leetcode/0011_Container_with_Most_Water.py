# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# Approach: Two Pointers
    # Start with two pointers as wide as we can go (left and right of the array). Our area is limited by our shorter side. 
    # Thus, we traverse our array my keeping our longer side and traversing our shorter side. Since the width gets necessary smaller, we need to increase the height of our shorter side. 
    # If we get a tie of side length, we can increment either side, as we still need to increase the height of our shorter side. Necessarily, both sides will have to be moved eventually. 
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        # Area of the container is index distance * smaller side
        left = 0
        right = len(height) - 1
    
        while left < right:
            left_side, right_side = height[left], height[right]
            width = right - left
            max_area = max(max_area, min(left_side, right_side) * width)
            if left_side < right_side:
                left += 1
            else:
                right -= 1
        return max_area
                
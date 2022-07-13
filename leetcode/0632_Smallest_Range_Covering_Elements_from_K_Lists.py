# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.


# Approach: Priority Queue, storing value and list location. Also, store the largest element as a variable. 
    # Remove the smallest element and see if we can add the next biggest number in its list (as the smallest number bounds how small we can make our range)
    # List has to be k size, so our heap will have to be k size. 
# Time Complexity: O(nlogk)
# Space Complexity: O(k)

import math
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        high_num = -math.inf
        k = len(nums)
        min_heap = []
        final_range = []

        # Initialise the heap: let i = list of lists index, j (currently 0) as list of nums index
        for i, arr in enumerate(nums):
            heapq.heappush(min_heap, (arr[0], i, 0))
            high_num = max(arr[0], high_num)
        
        # Heap must be k size as we need an element of each list
        while len(min_heap) == k:
            min_val, i, j = heapq.heappop(min_heap)
            curr_distance = high_num - min_val
            
            if final_range == [] or final_range[1] - final_range[0] > curr_distance:
                final_range = [min_val, high_num]
                
            # Push next element on the list of the smallest element if possible
            if j < len(nums[i]) - 1:
                new_element = nums[i][j + 1]
                heapq.heappush(min_heap, (new_element, i, j + 1))
                high_num = max(new_element, high_num)
        
        return final_range
                
            
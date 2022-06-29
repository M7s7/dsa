# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# Approach 1: Priority Queue/heap. 
    # We want to store tuples, as (distance, point). Since distance is tuple(0), heap will be arranged via distance. 
        # Time Complexity: O(NlogK) - heap is maximum k size. 
        # Space Complexity: O(k)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for i, point in enumerate(points):
            x, y = point
            distance = x**2 + y**2
            
            if i < k:
            # Negative distance to create a maxheap
                heapq.heappush(max_heap, (-distance, point))
            
            else:
            # If we have more than k values, then we can begin popping off values. Need to check if distance is smaller (closer) for popping. 
                if max_heap[0][0] < -distance:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-distance, point))
            
        return [i[1] for i in max_heap]


# Approach 2: TBC - Quick Select
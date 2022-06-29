# In order to decorate your new house, you need to process some sticks with positive integer length.
# You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y. Due to the construction needs, you must connect all the bars into one.
# Return the minimum cost of connecting all the given sticks into one stick in this way.


# Heap, using greedy algorithm.
    # Our greedy algorithm is to connect the two smallest sticks together at all times. Intuition: We will always be forced to make n - 1 connections. So, we will make the connections as cheap as possible. 
    # Heap to get the shortest sticks, and push the added stick back on the heap (one element is removed per loop)
    # Time Complexity: O(NlogN) - creation of the heap. Second loop will be smaller than NlogN as the heap is decreasing in size. 
    # Space Complexity: O(N) or O(1) depending if you think heapify on input counts as no space
import heapq
class Solution:
    def minimum_cost(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)

        while len(sticks) > 1:
            big_stick = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += big_stick
            heapq.heappush(sticks, big_stick)

        return cost
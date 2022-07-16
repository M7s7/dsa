# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
    # If x == y, both stones are destroyed, and
    # If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.


# Heap solution. Pop off two elements at a time and then compare them to either create a new rock or delet both rocks.
    # Time Complexity: O(NlogN) - heappopping and heappushing all elements (creation of up to N new elements)
    # Space Complexity: O(N) - creation of max heap
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            new_stone = heapq.heappop(max_heap) - heapq.heappop(max_heap)
            if new_stone != 0:
                heapq.heappush(max_heap, new_stone)
        
        if not max_heap:
            return 0
        return -max_heap[0]

    # Note that we can get space complexity of O(1) if we change it to an inplace heap. 
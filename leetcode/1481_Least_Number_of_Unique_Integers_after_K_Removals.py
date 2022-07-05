# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# Approach: Priority Queue. Eliminate the lowest frequency values. 
    # Time Complexity: O(nlogn) - popping off the entire heap
    # Space Complexity: O(N or 26) max
import heapq
import collections
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        min_heap = []
        for num in freq:
            min_heap.append([freq[num], num])
        heapq.heapify(min_heap)
        
        while k > 0 and min_heap[0][0] <= k:
            val, num = heapq.heappop(min_heap)
            k -= val
        
        return len(min_heap)

    # List comprehension/pythonic way
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:     
        freq = collections.Counter(arr)
        min_heap = [[val, char] for char, val in freq.items()]
        heapq.heapify(min_heap)
        
        while k > 0 and min_heap[0][0] <= k:
            val, num = heapq.heappop(min_heap)
            k -= val
        
        return len(min_heap)
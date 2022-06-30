# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Implement KthLargest class:
    # KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    # int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


# Approach: Min heap of k size. For clean code, we can use our helper function to initialise the heap as well. 
    # Time Complexity: O((n+m)logk), where n is the initial length of nums and m is the amount of added numbers
    # Space Complexity: O(k)
import heapq
 class KthLargest:
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]

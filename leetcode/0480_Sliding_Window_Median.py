# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the median array for each window in the original array. 

# Approach: Two heaps (max min) to find median. Trick in this question is to delete elements as they slide out the window, then rebalance.
    # Time Complexity: O(N * K). We go through all the elements. For each element, we may heappush/pop (logK) and remove an element (K)
    # Space Complexity: O(K) - heap sizes are only K size.
import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        # Two Heaps
        small = [] # This is a MAX HEAP
        large = [] # This is a MIN HEAP.
        
        # Index of start element
        start = 0
        
        for i, value in enumerate(nums):
            # By default, push to small heap
            heapq.heappush(small, value * - 1)

            # If our window is too large, remove an instance of the outside element from one of the heaps
            if i >= k: 
                outsideNumber = nums[start]
                if -1 * outsideNumber in small:
                    self.removeElement(small, -1 * outsideNumber)    
                else:
                    self.removeElement(large, outsideNumber) 
                start += 1
            
            # Rebalance our heaps
            self.rebalanceHeaps(small, large)

            # If our window is of k size, find a median
            if i >= k - 1:                
                # Find the median
                medians.append(self.findMedian(small, large))
        return medians
    
    
    # Helper function - Remove element when it moves outside the window
    def removeElement(self, heap, element):
        # Find element in heap - O(K) move
        index = heap.index(element)
        # Overwrite our target deletion element with the element on the end of our heap
        heap[index] = heap[-1]
        # Remove one of the duplicates
        del heap[-1]
        # Re-heap the value (O(K) operation with heapify)
        heapq.heapify(heap) # Note: We could instead sift our overwritten element to where it was originally, which is a O(LogK) operation
        return heap

    
    # Helper function - Rebalance heaps
    def rebalanceHeaps(self, small, large):
        # Condition 1: If small heap has element which is too large
        while small and large and small[0] * -1 > large[0]:
            heapq.heappush(large, -heapq.heappop(small))

        # Other conditions: If one list is too large
        while len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
            
        while len(large) > len(small) + 1:
            heapq.heappush(small, -heapq.heappop(large))
    
    
    # Helper function - Find the median value (will be a float)
    def findMedian(self, small, large):
        if len(small) > len(large):
            return -1.0 * small[0]

        elif len(large) > len(small):
            return 1.0 * large[0]

        else:
            return 0.5 * (large[0] + -1 * small[0])
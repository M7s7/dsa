# Implement the MedianFinder class:
    # MedianFinder() initializes the MedianFinder object.
    # void addNum(int num) adds the integer num from the data stream to the data structure.
    # double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Optimal Approach: Implement two heaps, a max and min heap, with the following conditions:
        # The heaps are of equal size +- 1
        # The heaps are divided into small numbers and large numbers, such that all the small heap's elements are SMALLER than all the large heap's elements
        # The small heap is a MAX heap, while the large heap is a MIN heap. 
    # By doing this, we will be able to seperate the numbers. For example, given the addNum arguments (9,2,7,1,8,0,3) we will seperate them into the following heaps:
        # [-3, -2, -0, -1] and [7, 9, 8] where the first indexes are the MAX small heap and the MIN large heap (note that they are negatives as python natively has minHeaps)
        # Thus, the area where the max heap[0] and min heap[0] meet IS where the median is. 
        # Note that the elements in the heaps do not have to be in sorted order. All we need to know is the two values at the max/min of the small/large heaps. 
    # Time Complexity: O(log(N))
        # Adding numbers - O(log(n)) - adding and removing elements from heaps is a O(logn) operation
        # Finding median - O(1) - indexing into the max/min values of max/min heaps is constant time
    # Space Complexity: O(N) to hold all the numbers in the heaps
import heapq

class MedianFinder:
    # Initalise data structures. Since these heaps are called outside of this function, we must initiate them as class level variables
    def __init__(self):
        # We will create two heaps that follow two conditions: 1) the heaps are of the same size give or take one element // 2) all the numbers of the small heap are SMALLER than all the numbers in the large heap
        self.small = [] # max heap
        self.large = [] # min heap

    # Function adds one number
    def addNum(self, num: int) -> None:
        # By default, add the number to any list. Arbitrarily, we will add it to the small list. 
            # python heaps are minHeaps by default. We will take negative numbers to get around this
        heapq.heappush(self.small, num * -1)
        
        # First condition: Our number in the small array is larger than any number in the other array. We will remove that number and place it into the other heap
            # Since we are indexing into both heaps, we need to check if there are elements in both. 
        if self.small and self.large:
            while -1 * self.small[0] > self.large[0]:
                heapq.heappush(self.large, -1 * self.small[0])
                heapq.heappop(self.small)
        
        # Second condition: If one heap is too large, we will remove an element from it and place it to the other heap. Since we move the max/min element, we will not ruin our condition that all nums in small are smaller than all nums in large.
            # If statements can work instead of while loops, as each time we call this function we add only one number. Thus, we can fix any size difference with one operation
        if len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, -1 * self.small[0])
            heapq.heappop(self.small)
            
        if len(self.large) - len(self.small) > 1:
            heapq.heappush(self.small, -1 * self.large[0])
            heapq.heappop(self.large)
        return
    
    # Function finds the median number (middle)
    def findMedian(self) -> float:
        # If the heaps are the same size, then we have an even number of numbers. The median is the average of the sum of the two middle numbers. 
        if len(self.small) == len(self.large):
            return (-1 * self.small[0] + self.large[0])/2
        
        # Else, the bigger size heap has the median value
        elif len(self.small) > len(self.large):
            return (-1 * self.small[0])
        
        else:
            return (self.large[0])

# Alternate approach - every time we add a number, we sort the list. In other words, we insert numbers in order. Then we index into the median element (if no median, then the average of the two middle numbers)
# Inserting into a list takes O(N) time. Thus, the time complexity is O(N)^2
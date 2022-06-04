# You are given an array of intervals, where intervals[i] = [start[i], end[i]] and each start[i] is unique.
# The right interval for an interval i is an interval j such that start[j] >= end[i] and startj is minimized. Note that i may equal j.
# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.


# Approach: Use two max heaps to store start and end values. These values will be stored as TUPLES with the index of the interval they are from.
    # Then, go through the values in the ends heap one at a time. To find the right interval, we need to find the smallest startValue that is still larger than the endValue. 
    # Once this value is found, we can store the values in an output array that we initiate earlier. 
    # If no value is found, do not modify the output array, since our output array will be initiated with all -1s. 

import heapq

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [] # Max heap
        ends = [] # Also a max heap
        # Initiate dummy list
        nextInterval = [-1 for _ in range(len(intervals))]
        
        # Store intervals as tuples in the heaps
        for i, interval in enumerate(intervals):
            start, end = interval
            # Heaps to store start/end value and index
            heapq.heappush(starts, (-start, i)) # Negative values to create a max heap
            heapq.heappush(ends, (-end, i))

        # Go through one endValue at a time and find the smallest startValue that is still larger than the endValue
        while ends:
            # Get one endValue that we will match with a startValue 
            endValue, endIndex = heapq.heappop(ends)
            # Pop off the highest startValue to check if an endValue exists
            startValue, startIndex = heapq.heappop(starts)
            
            # Check if our endValue actually has a rightvalue 
            if -startValue >= -endValue:
                # If we do, peek at the next largest startValue to see if there is a better right interval. 
                while starts and -starts[0][0] >= -endValue:
                    # Since the starts max heap is sorted, the second startValue is <= the previous one. Thus, we can update our stored startValue. 
                    # Note that we ONLY POP OFF values after we peek to see if they are a valid next interval. 
                    startValue, startIndex = heapq.heappop(starts)
                
                # Once we have the smallest right interval, update our results. 
                nextInterval[endIndex] = startIndex
            
            # Put the right interval back on the starts heap, just in case it is the right interval for our other intervals.
            heapq.heappush(starts, (startValue, startIndex))

        return nextInterval

    # Note: Why are we using maxHeaps?
    # If we consider the largest endValue first, we can immediately check the largest startValue to see if there is any right interval.
    # If there is, we can remove all the suboptimal startValues (remember, the optimal startValue is the smallest one that is still bigger than the endValue).
    # Because we are using maxHeaps, these removed startValues will never be an optimal right interval with any of the other endValues, as all the following endValues are smaller than the current one. 
        # We could use minHeaps but maxHeaps make more sense.
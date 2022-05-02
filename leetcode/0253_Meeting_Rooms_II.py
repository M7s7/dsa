# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

# Intuition: The most consecutive OVERLAPPING INTERVALS at any given time will be the max rooms.
# Interval A and interval B will overlap if A.start < B.end and B.start < A.end (this is the CROSS LOCK). If we can find a data structure to STORE THE END VALUES OF THE INTERVALS WE CHECK, we can check if future intervals overlap.
## In a sorted array of intervals, we can check if our current interval's start > smallest end value out of the previous end values. We can check this condition against ALL of stored end variables and see how many overlap. 
#### (Remember, we do not have to check for the other overlap condition (previous.start < current.end) as that is a given in a sorted list)
# If the current start value is LARGER than some of the previous interval ends, we can simply remove these interval endpoints as they no longer will overlap with any current or future intervals. 


# METHOD 1: SORTING AND CREATING TWO ARRAYS: START AND END. 
    # Create two sorted arrays - a start values and an end values. 
    # Inituitively, every time we reach a start value, we need another room.
    # Conversely, every time we encounter an end value, a meeting has ended during our considered interval.
    # If a start and end value end at the same time, we can END the meeting first and start a new one. 
    # Time complexity: O(N log n) for sorting // Space complexity: O(N) 

def min_meeting_rooms(self, intervals: List[Interval]) -> int:
    # Create and sort two arrays - one for start values and one for end values
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    # We need pointers to keep track of each array, as well as a counter variable
    s = e = rooms = max_rooms = 0

    # Iterate through the START array (if we reach the end of the start array, no more meetings are possible)
    for s in start: 
        # Each start found is immediately an instance of a new meeting, so add 1 to room 
        rooms += 1
        # However, if the start value is LARGER than the current end value, we need to keep incrementing up until we find an overlapping interval (where start < end)
        while s >= end[e]: # Remember, if the start and end values are equal, this is NOT an overlap. 
            rooms -= 1
            e += 1
        # After we find the number of overlapping intervals, store it
        max_rooms = max(rooms, max_rooms)
    return max_rooms

    ## NOTE: Neetcode uses a whileloop instead of a for loop, with the condition (while s < len(intervals))


# METHOD 2: HEAP SOLUTION. We use a min-heap to store interval end values on every iteration. With a min-heap, we can easily 'pop' off the smallest end value. (NOTE: A heap in python is implemented as an array). 
    # During every iteration, we also check if there are end values from previous intervals which DO NOT overlap. If so, we keep popping off these values until we are left with only overlapping intervals (this could mean that we are left with only our current interval)
    # The number of elements in the heap is equal to the size of the heap (as the heap values represent the end values of each currently overlapping interval)
    # We return the max of this number.
    # Time complexity: O(N log N) due to sorting. Other smaller factors include (N log k) for every heap action, where k is equal the amount of end values, (as heap has to maintain order) - means that worst case scenario is really 3 * N log N
    # Space complexity: O(N) due to heap storage

import heapq # THIS SHOULD BE PLACED GLOBALLY AT THE TOP WITH THE OTHER IMPORTS - DO NOT ADD IT IN THE CLASS SOLUTION.

def min_meeting_rooms(self, intervals):
    # First, sort the interval by start - this allows us to guarantee that start > previousEnd is an overlap
    intervals.sort(key = lambda x: x.start)
    
    # Create a heap (which is a list): Our heap will store the ENDS of each interval we have iterated over.  
    heap = [intervals[0].end] # Initialise the heap with our first end time so we have something to compare with
    # Initialise a 'rooms' variables. Remember that rooms is really a count of how many 'intervals' are overlapping at a given time (1 means 'overlapping with itself', 2 means two intervals overlapping, etc)
    rooms = 1 

    # Iterate through the intervals, starting from the second interval (as we have stored the first). 'i' represents the current interval
    for i in intervals[1:]:
        # Conditional, checking if the stored intervals are no longer overlapping with the current one 
        while heap and i.start >= heap[0]:
            # Start popping off previous intervals (which are stored endpoints, remember) which are not overlapping
            heapq.heappop(heap)
        # After verifying that there are ONLY overlapping intervals in the heap, add the current interval END as well to the heap
        heapq.heappush(heap, i.end)
        # Get the maximum number of overlapping intervals or 'rooms' needed
        rooms = max(rooms, len(heap))
    return rooms
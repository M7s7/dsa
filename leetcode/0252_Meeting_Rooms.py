# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Sort the list of intervals by START VALUE. Then, check if there is an intersection between the current interval and the next interval. 
# Time complexity: O(n log n) (due to the sorting of the array) // Space complexity: O(N) because we sort the array

def can_attend_meetings(self, intervals):
    # Sort intervals by start times
    intervals.sort(key = lambda x: x.start)

    # Do not need to go through all intervals - if we are on our last interval, there are no more conflicts
    for i in range(len(intervals) - 1):
        # Condition to check if we have an overlap - end of current interval is greater than start of next interval
        if intervals[i].end > intervals[i + 1].start:
            return False

    # If there are no conflicts, then return True
    return True

# NOTE: The solution looks like this because the 'intervals' is a lists of OBJECTS in the Lintcode problem instead of list of lists.
# eg. class Interval(object):
#    def __init__(self, start, end):
#        self.start = start
#        self.end = end
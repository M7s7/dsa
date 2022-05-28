# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Approach: When iterating through the list of intervals, keep track of the latest non-overlapping endpoint and compare it with the next startpoint. If currStart < prevEnd, we have an overlap.
    # When an overlap is encountered, we want to deal with it immediately. We need to either 'remove' the previous interval or the current interval. 
    # This can be represented by updating the prevEnd variable to the smaller of the two intervals, which symbolises a removal of the other interval. Since an interval is being removed, we can update the email
    # Time Complexity: O(NlogN) for sorting, + N for iteration through list // Space complexity: O(N) for sorting
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        # First, sort our list of intervals by start time
        intervals.sort(key = lambda x: x[0])
        ans = 0
        # PrevEnd variable will store the end-value of our last non-overlapping interval.
            # We can initialise it with our first interval's end time to compare against
        prevEnd = intervals[0][1]
        
        # Loop through all intervals, skipping the first one. 
        for i in intervals[1:]:
            start = i[0]
            end = i[1]
            
            # If our start time is smaller than our previous intervals' end, we have an overlap.
            if start < prevEnd:
                # If there is an overlap, we will keep our interval with the SMALLER endtime (which has less chance of overlapping future intervals), and remove the other one. 
                prevEnd = min(prevEnd, end)
                # Add counter as we have removed an interval
                ans += 1
            
            # Else, we update our prevEnd using our current interval's end
            else:
                prevEnd = end
            
        return ans
                
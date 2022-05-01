# Given a SORTED array of non-overlapping intervals in the list 'intervals', insert a 'newInterval' such that intervals is still sorted and non-overlapping.

# METHOD 1: We create a NEW list of intervals which we return. Approach: 
## Starting from interval[0], add as many the intervals which are non-overlapping.
## Once an overlap has been found with the newInterval, merge the two together. Continue checking for the next intervals.
## Once newInterval has been passed, add it to the list and then the rest of the intervals list. 
## If newInterval doesn't get passed, we want to append newIntervals at the end of the list and then return it. 
## Time complexity: O(N) (one pass solution) // Space complexity: O(N) (we store a new list)

def insert(self, intervals, newInterval):
    ans = []
 
    for i in range(len(intervals)):
        # Base case - interval end is smaller than newInterval start, then we just add the interval to the list
        if intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            continue
        
        # If there is an overlap, MERGE the intervals. 
        # Condition is if current end >= newIntervalStart AND current start <= newIntervalEnd. The first condition is already checked above
        elif newInterval[1] >= intervals[i][0]:
            # Merge the intervals together
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            # Do not add it to the answer yet, as we may need to merge more intervals
        
        # If we have PASSED the new interval, we can attach it and then append the rest of the intervals. 
        # We can determine passing it if the current START of our interval > newIntervalEnd (newInterval[1] < intervals[i][0])
        else: 
            # If we are past the new interval, append everything left
            ans.append(newInterval)
            return ans + intervals[i:]
    
    # If we don't return in the loop, it means that our newInterval is at the END and thus never got passed. Thus, we need to manually append it.
    ans.append(newInterval)
    return ans


# METHOD 2: We append the newInterval to the intervals list, then we MERGE IN-PLACE (same as problem 56.)
## Time complexity: O(nlogn) due to sorting // Space complexity: O(N + N) (storing a new list plus space for sorting)
def insert(self, intervals, newInterval):
    # Append the new interval to the list
    intervals.append(newInterval)
    
    # Re-sort the list, sorting it by first number of each list
    intervals.sort(key = lambda list: list[0])
    
    # Initialise an interval in the ans so we have something to compare next intervals with
    ans = [intervals[0]]
    # Implement merging function 
    for i in range(len(intervals)):
        # No overlap if this is the case
        if ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])
            continue
        
        # If there is an overlap, we want to merge it with the stored interval
        else:
            # ans[-1][0] = min(intervals[i][0], ans[-1][0]) <-- actually, don't need this code because the list is sorted so we are ALWAYS storing the minimum
            ans[-1][1] = max(intervals[i][1], ans[-1][1])
        
    return ans
# Given a SORTED array of non-overlapping intervals in the list 'intervals', insert a 'newInterval' such that intervals is still sorted and non-overlapping.

# METHOD 1: We create a NEW list of intervals which we return. Approach: 
## Starting from interval[0], add as many the intervals which are non-overlapping.
## Once an overlap has been found with the newInterval, merge the two together. Continue checking for the next intervals.
## Once newInterval has been passed, add it to the list and then the rest of the intervals list. 
## If newInterval doesn't get passed, we want to append newIntervals at the end of the list and then return it. 
    # Time complexity: O(N) (one pass solution)
    # Space complexity: O(N) (we store a new list)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        ans = []
        
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]
            # Situation 1: If our remaining intervals are after our new interval, we can append everything and terminate early
            if curr_start > new_end:
                ans.append([new_start, new_end])
                return ans + intervals[i:]
            # Situation 2: Overlapping interval - Merge our intervals, but do not append yet (as it could still extend further)
            if curr_end >= new_start:
                new_start = min(new_start, curr_start)
                new_end = max(new_end, curr_end)
            # Situation 3: Interval comes before our new interval - just append it to the list. 
            else:
                ans.append(intervals[i])
        # Exiting the loop means that the merged interval is either the last interval, or has merged with the last interval. Thus, we still need to append it
        ans.append([new_start, new_end])
        return ans


# METHOD 2: We append the newInterval to the intervals list, then we MERGE IN-PLACE (same as problem 56.)
    # Time complexity: O(nlogn) due to sorting
    # Space complexity: O(N + N) (storing a new list plus space for sorting)
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
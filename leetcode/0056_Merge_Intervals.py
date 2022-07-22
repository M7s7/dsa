# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# We sort the intervals (which is a list of lists) by the START value of each interval. 
# Then, starting from the first interval, we check if there is an overlap (if previous list end is larger than/equal to current list start.)
# If there is an overlap, merge the lists by changing the END VALUE of the last stored list (if there is a new maximum). If there is not overlap, store the next list and repeat the process.  
    # Time complexity: O(nlogn (for sorting)) + N for iteration over the intervals
    #  Space complexity: O(N) (N + N for storing every interval in the list + sorting)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # First, sort the list of lists by FIRST ELEMENT of each list
        intervals.sort(key = lambda list: list[0])
        
        # Create a list of results and initialise the first interval (list) in it
        ans = [intervals[0]]
        
        # Now, starting from the second list, see if there is an overlap of the ending with the next element. 
        # For each list, we will take the first and last numbers of the interval
        for start, end in intervals[1:]: 
            # Look at the latest list in the output and note its end value
            prevEnd = ans[-1][1]
            
            # MERGE LISTS: There is an overlap if the current interval's start is SMALLER than or EQUAL to the previous interval's end
            if start <= prevEnd: 
                # When we merge the lists, we want to take the MINIMUM start (which we already have as we have sorted the intervals) and the MAXIMUM end
                # If the lists overlap, we can KEEP the previous list stored in ans and continue to expand its END value
                ans[-1][1] = max(prevEnd, end)
           
            # ADD NEW LIST: If there is no overlap, then just add it as a new list
            else:
                ans.append([start, end])
        return ans

# My implementation - I think it is easier to understand. 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []
        
        # Use our first interval to compare with other intervals
        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            # If there is no overlap, we can append the previous interval and then store our current one
            if curr_start > prev_end: 
                merged.append([prev_start, prev_end])
                prev_start = curr_start
                prev_end = curr_end
            # If there is an overlap, extend our previous interval
            else:
                prev_end = max(prev_end, curr_end)
        # Append the interval we are storing at the end of the list
        merged.append([prev_start, prev_end])
        return merged
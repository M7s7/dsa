# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# We sort the intervals (which is a list of lists) by the START value of each interval. 
# Then, starting from the first interval, we check if there is an overlap (if previous list end is larger than/equal to current list start.)
# If there is an overlap, merge the lists by changing the END VALUE of the last stored list (if there is a new maximum). If there is not overlap, store the next list and repeat the process.  
# Time complexity: O(nlogn (for sorting)) + N for iteration over the intervals // Space complexity: O(N) (N + N for storing every interval in the list + sorting)

def merge(self, intervals):
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

# Other solution is using CONNECTED COMPONENTS. However, this one is convoluted and not more efficient. 


### Important new functions that I have learnt:
# for sorting: sort(key = lambda <insert function here)
# list[1][2]: For a list of lists, go into the FIRST INDEXED LIST. In that list, go to the SECOND INDEXED ELEMENT. 
# list[-1]: In the list, go to the LAST ELEMENT. list[-2] is the second last element, etc. 
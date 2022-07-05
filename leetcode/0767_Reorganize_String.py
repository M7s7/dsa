# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.

import collections
import heapq
# Approach: Heap/PQ. Add the most frequent character. Then take the second most frequent, and put the most frequent back on the heap. Continue until finished. 
    # Time Complexity: O(nlogn): N for heapify, N for hashmap, NlogN for push/pop loop
    # Space Complexity: O(N or 26) - N for freq, N for heap size (or 26 for each)

    # Method 1: My own implementation
        # My implementation of heap solution. A bit messy in how to alternate tuples. 
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = collections.Counter(s)
        max_heap = [(-freq[char], char) for char in freq]
        heapq.heapify(max_heap)
        
        string = []
        val, char = heapq.heappop(max_heap) # Initialise val/char.
        while True:
            string.append(char) 
            val += 1
            if not max_heap:
                break
            # Get the second most frequent character
            temp = heapq.heappop(max_heap) 
            if val != 0: # If there are still instances left, we can push the current character back on
                heapq.heappush(max_heap, (val, char)) # 
            # Now, we use the second character as our current to alternate chars
            val, char = temp
        
        # Check if our string is valid
        if len(string) != len(s):
            return ""
        return "".join(string)

    # Method 2: 'Cleaner' heap solution. 
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = collections.Counter(s)
        max_heap = [(-freq[char], char) for char in freq]
        heapq.heapify(max_heap)
        
        string = []     
        temp = None
        while max_heap or temp:
            if not max_heap:
                return ""
            val, char = heapq.heappop(max_heap)
            val += 1
            string.append(char)
            # Temp variable acts as a placeholder, storing the alternating most frequent character
            if temp:
                heapq.heappush(max_heap, temp) # Push on first
                temp = None # Important to initialise it as None again, just in case we can't use our current char anymore
            # If there is still frequency left on the char, we can use it again
            if val != 0:
                temp = (val, char)
 
        return "".join(string)
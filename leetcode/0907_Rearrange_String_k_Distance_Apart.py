# Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.
# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".


# Approach: Find most frequent elements. Build a string using the most frequent elements.
    # Use a queue to hold the used letters until we can reuse them. 
    # When the heap is empty, it means that we have no more valid letters left to append.
        # Time Complexity: O(nlogn) for heap operations (push and pop). O(N) for counter, array building, heapify, etc. 
        # Space Complexity: O(N). It is O(N) for counter, heap, queue. Each one can be max 26 elements long (alphabet). 
import collections
import heapq

class Solution:
    def rearrange_string(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        string = []
        freq = collections.Counter(s)
        max_heap = [(-val, char) for char, val in freq.items()]
        heapq.heapify(max_heap)
        used_letters = collections.deque()
        
        while max_heap:
            val, char = heapq.heappop(max_heap)
            val += 1
            string.append(char)

            # If char is used, we place it on the queue. Even place it on with 0 val to keep order. 
            used_letters.append((val, char))
            #
            if len(used_letters) >= k:
                val, char = used_letters.popleft()
                if val != 0:
                    heapq.heappush(max_heap, (val, char))
        
        if len(string) != len(s):
            return ""
        return "".join(string)
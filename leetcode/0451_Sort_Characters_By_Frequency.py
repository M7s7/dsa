# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.


# Freq hashmap + priority queue (maxheap) + return string
    # Time Complexity: O(N) - O(N) for freq, O(klogk) *2 (where k is max 62 or something for all chars) for heap operations
    # Space Complexity: O(1) - freq and pq are max around 62 each
        # Approach 1: String concatenation (worse)
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        max_pq = []
        for char in freq:
            val = freq[char]
            heapq.heappush(max_pq, (-val, char))
            
        ans = ""
        while max_pq:
            val, char = heapq.heappop(max_pq)
            ans += char * -val
        
        return ans

        # Approach 2: String-builder (better)
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        max_pq = []
        for char in freq:
            val = freq[char]
            heapq.heappush(max_pq, (-val, char))
            
        ans = []
        while max_pq:
            val, char = heapq.heappop(max_pq)
            ans.append(char * -val)
        
        return "".join(ans)
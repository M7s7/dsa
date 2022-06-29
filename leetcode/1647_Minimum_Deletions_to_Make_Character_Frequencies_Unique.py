# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.

# General intiution:
    # The characters themselves don't matter. We just want the FREQUENCIES of each value to be unique. There are several ways to do this:


# Single hashmap + reverse sorted array + single variable to track next unused frequency. Cleanest solution, but not that intuitive.
    # Take [3,3] as the frequency array for example. Initially, the unused freq is 6 (len(s)), then 3 (min). Then, since this value has been used, it is 2. 
    # On the next loop iteration, freq is 3. However, next unused is 2. Thus, add 1 to deleted chars. 
        # Time Complexity: O(N) - O(N) for hashmap, sorting is klogk MAXIMUM (but k maximum is 26), and O(N) for second loop. 
        # Space Complexity: O(min(26, N)) - freq map is max 26, and double this for the sorted array space
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        ans = 0
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        freq_sorted = sorted(freq.values(), reverse = True)

        # Initiate unused frequency variable.
        unused_freq = len(s)
        for val in freq_sorted:
            # If the current frequency has not been used, we will store it in this. However, if it has been used, it will not be stored (as it will be larger than the current unused)
            unused_freq = min(unused_freq, val)
            # Note that if the curr frequency has not been used, then this will add 0. 
            ans += val - unused_freq
            
            # When a frequency is used, we go to the next unused frequency (one less). We have to do this every loop until there are no freqs left, because every freq has to be unique. 
            if unused_freq > 0:
                unused_freq -= 1
                
        return ans


# Single hashmap + reverse sorted array + in-place changing of values. Very complicated and finnicky. 
    # Idea is we store all the frequencies in the hashmap. Then create an array which is reverse sorted frequency values (eg. [3, 2, 2, 1])
    # Then iterate through the array. When a non-decreasing number is found, we set it to the previous number - 1 and add the difference to change.
    # When we turn a number to 0, it means that the rest of the numbers will be also 0. Thus, we can iterate through the array and add their values to change
        # Time Complexity: O(N) - same as above
        # Space Complexity: O(min(26,N)) - same as above
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        ans = 0
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        freq_sorted = sorted(freq.values(), reverse = True)

        for i in range(1, len(freq_sorted)):
            if freq_sorted[i] >= freq_sorted[i - 1]:
                change = freq_sorted[i] - freq_sorted[i - 1] + 1
                ans += change
                freq_sorted[i] = freq_sorted[i - 1] - 1
                print(i, freq_sorted[i], freq_sorted[i - 1], ans, change)
                
            if freq_sorted[i] == 0:
                i += 1
                while i < len(freq_sorted):
                    ans += freq_sorted[i]
                    i += 1
                return ans
                    
        return ans


# Double hashmap - one to store frequency, one to store unique frequencies. 
    # Go through first frequency hashmap. If the value is unique, store it. If not, decrement it until it is unique, then store it. 
        # Time Complexity: O(N) - O(N) for hashmap + O(N) for second loop. If the array is sorted, then the second loop could be O(N^2) due to the decrementing while loop, so creating a reverse sorted array to draw from might be better. 
        # Space Complexity: O(min 26,N) - 2 times if no sorted array, 3 times if sorted array
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        unique = {}
        ans = 0
        
        for key in freq:
            count = freq[key]
            while count > 0 and count in unique:
                count -= 1
                ans += 1
            unique[count] = True
        return ans


# This solution is an abomination. Not even sure what is going on here tbh. Looks to be initial sorted string and then one freq hashmap?
    # Then, find freq of each char (count until diff char). Then, add it to the hashmap. If the number is already in the hashmap, decrement it until it is unique.
    # DO NOT USE THIS ONE. 
class Solution:
    def minDeletions(self, string: str) -> int:
        s = sorted(string)
        freq = {}
        ans = 0
        
        for i in range(len(s)):
            if i == 0:
                curr = s[0]
                curr_freq = 1
            
            else:
                if s[i] == s[i - 1]:
                    curr_freq += 1
                
                else:
                    while curr_freq > 0 and curr_freq in freq:
                        ans += 1
                        curr_freq -= 1
                        
                    freq[curr_freq] = True
                    curr_freq = 1
        while curr_freq > 0 and curr_freq in freq:
            ans += 1
            curr_freq -= 1
        return ans
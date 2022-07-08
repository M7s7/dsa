# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Hashmap with deletion
    # Time Complexity: O(N)
    # Space Complexity: O(N)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        operations = 0
        
        for num in nums:
            target = k - num
            if target in freq:
                operations += 1
                freq[target] -= 1
                if freq[target] == 0:
                    del freq[target]
            
            elif num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        return operations


# Hashmap, no deletion
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        operations = 0
        
        for num in nums:
            target = k - num
            if target in freq and freq[target] > 0:
                operations += 1
                freq[target] -= 1
            
            elif num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        return operations
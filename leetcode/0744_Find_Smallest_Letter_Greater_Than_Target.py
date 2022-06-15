# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
# Note that the letters wrap around. [a, b] with target z - answer would be a.

# Binary Search.   
    # Upper bound shrinks to mid. Lower bound shrinks past mid. Mid is a 'lower mid', ensuring that we do not accidentally index into our out-of-range index at the far right.
    # Our loop will exit when low and high converge. They should converge on the first letter greater than the target - note that moving our low bound EXCLUDES mid. 
        # Time Complexity: O(log N) - binary search modified
        # Space Complexity: O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) # Search space is larger than the actual array, as the largest char might be smaller than the target
        
        # When low and high converge, we return
        while low < high:
            mid = low + (high - low)//2
            mid_val = letters[mid]
            
            # Even if our mid value is the same as target, it is still OUTSIDE our searchspace, so move past it. 
            if mid_val <= target:
                low = mid + 1
            
            # Shrink search space, but DO NOT exclude mid value as this might be the answer
                # This condition is mid_val > target - which means that it is possible that it is the answer
            else:
                high = mid
        
        # If our answer is outside the array, it is either lower than our first char, or higher than the last.
            # Since the numbers wrap, the largest char for both is letter[0]
            # If it is lower than letter[0], we initalised low on 0 anyways so no need to change it.
        if low == len(letters):
            return letters[0]
        
        return letters[low]


# Slower binary search - uses ord() to convert char into numbers.
    # However, this is unnecessary as python uses lexicographic ordering. 
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) # Search space is larger than the actual array, as the largest char might be smaller than the target
        target_val = ord(target)
        
        while low < high:
            mid = low + (high - low)//2
            
            # Converts char to number (1-26)
            mid_val = ord(letters[mid])
            
            if mid_val <= target_val:
                low = mid + 1
            
            else:
                high = mid
            
        if low == len(letters) or low == -1:
            return letters[0]
        
        return letters[low]


# Slower, brute force solution
    # Time Complexity: O(N)
    # Space Complexity: O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
            
        return letters[0]
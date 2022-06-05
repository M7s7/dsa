# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# BFS: Easier solution. Same as Subsets I, but before adding each set, we will check if it is already in the set. 
    # By sorting the nums list first, we will get duplicate sets in the same order so it is easier to check.
        # Time Complexity: O(N * 2^N), 2^N sets created, looping through N numbers. 
        # Space Complexity: O(N * 2^N)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        #BFS:
        powerSet = [[]]
        
        for value in nums:
            for i in range(len(powerSet)):
                # Create a temporary subset
                temp = powerSet[i] + [value]
                # Check if subset is a duplicate before adding
                if temp not in powerSet:
                    powerSet.append(temp)
                
        return powerSet


# BFS: Harder solution. Instead of pythonically for duplicates, we will check if our current number is a duplicate.
    # If so, we will only add our number to NEWLY CREATED subsets from the last loop. Since the subsets are added in order, we can track the index threshold where the new added subsets start.
    # Conveniently, this index is the size of the powerSet BEFORE the new sets were added. 
        # Time Complexity: Big O time is the same, but may be slightly more efficient as we skip duplicate sets. 
        # Space Complexity: Big O is the same, but slightly more efficient as we don't need to create temp sets. 
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        powerSet = [[]]
        # Initiate a 'newIndex' variable. This will be the index in powerSets where the new added sets start. We will use this index only if we have a duplicate. 
        newIndex = 0
        
        for i, value in enumerate(nums):
            # If we have a duplicate, then we set our newIndex to where the newly added sets start. In other words, we SKIP all the older sets which would create duplicates. 
            if i > 0 and nums[i - 1] == value:
                newIndex = oldSets
            # If we have a new element, we reset. This is because the new element can make new subsets with ALL the sets. 
            else:
                newIndex = 0
            # oldSets will store an index indicating where the NEW ADDED SETS start. This will be used on the NEXT loop if needed. 
            oldSets = len(powerSet)
            
            # For-loop starts at our correct index (skipping old sets if we have a duplicate).
            for j in range(newIndex, len(powerSet)): # Note that we start from newIndex, and finish at index: len(powerSet) - 1. 
                powerSet.append(powerSet[j] + [value])
            
        return powerSet


# DFS: Similar to Subsets I approach - each number determines the children nodes for the next.
    # Slight modification: Initially, we will return a subset with every single element. When backtracking, we want to SKIP adding duplicate elements (in other words, if we pop off a number, we don't want to add the same number back.)
        # If we don't skip duplicate elements, we will have duplicate sets: eg. for [1, 2, 2] - there will be the duplicate sets [1, 2, _] and [1, _, 2] - the latter will be SKIPPED if we skip adding duplicate elements. 
            # Time Complexity: Same as above. We add 2^N sets with N elements in each path. 
            # Space Complexity: Same
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Again, sorting the index is neccessary to get the duplicates next to each other
        nums.sort()
        powerSet = []
        
        def findSets(index, subset):
            # Basecase:
            if index >= len(nums):
                powerSet.append(subset.copy())
                return
            
            # Add an element to our current subset. 
            subset.append(nums[index])
            findSets(index + 1, subset)
            
            # Backtrack
            subset.pop()
            
            # When backtracking, we want to skip duplicate numbers
            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            findSets(index + 1, subset)
        
        findSets(0, [])
        return powerSet

# DFS: Simpler solution, just check if we have the set in the current powerSet.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Again, sorting the index is neccessary to get the duplicates next to each other
        nums.sort()
        powerSet = []
        
        def findSets(index, subset):
            if index >= len(nums):
                # Modification: Only add set if we don't have it
                if subset not in powerSet:
                    powerSet.append(subset.copy())
                return
             
            subset.append(nums[index])
            findSets(index + 1, subset)
            
            subset.pop()
            findSets(index + 1, subset)

        findSets(0, [])
        return powerSet
    
    
    
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# 'BFS' Approach: Go through each number one at a time.
    # For each number, go through each previous set.
    # Insert the number at each index location of the previous sets. 
# Time Complexity: O(N * N!). There are a total of N! permutations. Insertion of a number into a list of size N is an O(N) operation
# Space Complexity: O(N * N!) - N! total permutations of N length

import collections

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = collections.deque()
        perms.append([])
        
        # Iterate through each number
        for num in nums: 
            # Initialise two variables:
            oldSets = len(perms) # Number of sets currently in queue that we need to create new permutations for
            insertIndex = len(perms[0]) + 1 # Number of new permutations for each subset
            
            # Go through each current set
            for _ in range(oldSets):
                currSet = perms.popleft() # Need to pop off old, transitory sets
                
                # For each current set, insert our next number at each index value
                for i in range(insertIndex):
                    temp = currSet.copy()
                    temp.insert(i, num)          
                    perms.append(temp)

        return perms


# DFS solution, with backtracking
    # Go through each number of the array, adding the numbers to a current permutation.
    # Every time you add a number, we want to remove it from the nums list that is used for the next dfs. 
    # Backtracking must be used as the perm variable is shared
# Time Complexity: O(N * N!) is the amount of recursive calls we make. N! permutations, each permutation has N nodes to call
# Space Complexity: O(N * N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_perms = []
        
        def dfs(nums, perm):
            # Base case
            if not nums:
                all_perms.append(perm[::])
                return
        
            # Recursive case to iterate through all the numbers of all nums lists
            for i in range(len(nums)):
                perm.append(nums[i])
                # Remove our current number from our list for our next iteration. Note that list concatenation creates a copy
                new_nums = nums[:i] + nums[i + 1:] # Note - this can also be done with del instead
                # Recursive call for all sub-nums lists
                dfs(new_nums, perm)
                # After resolving our paths for a number, we want to pop it off
                perm.pop()
    
        dfs(nums, [])

        return all_perms

# DFS solution, no backtracking
    # Instead of passing through the same curr perm variable, we pass through a copy of a new one instead. 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_perms = []
        
        def dfs(nums, perm):
            # Base case
            if not nums:
                all_perms.append(perm[::])
                return
        
            # Recursive case, over every nums list
            for i in range(len(nums)):
                # NEW PERM VARIABLE CREATED to avoid backtracking
                new_perm = perm + [nums[i]]
                # Remove our current number from our list for our next iteration
                new_nums = nums[:i] + nums[i + 1:]
                # New_perm is passed through instead
                dfs(new_nums, new_perm)
    
        dfs(nums, [])

        return all_perms

            
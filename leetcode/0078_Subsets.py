# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# BFS: For each given element, we can double the amount of current subsets by creating new sets where we simply add the new element to the current sets. 
    # Thus, for every element, we can loop through the current subsets and add modified copies with the element appended to it. 
    # Once we have done this for every element, we have completed our BFS. 
        # Time Complexity: O(N * 2^N). We loop through N numbers. Each loop, we have to add new sets - the amount of sets we add is doubled each loop, so 2^N. 
        # Space Complexity: O(N * 2^N), which is the amount of extra sets in output.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = [[]]
        
        for value in nums:           
            for i in range(len(powerSet)): # Note that we cannot use enumerate to iterate over the powerSet, as it will infinite loop because we are modifying powerSet. This is not a problem with range. 
                newSet = powerSet[i]
                powerSet.append(newSet + [value]) # List concatenation creates a new list, containing copies of the two lists. Thus, it is no longer passed through reference
                
        return powerSet

    
# DFS: We can reframe the question as follows:
    # The root node is an empty set.
    # Each number dictates the children nodes of the next level. Each node for the level above will have children [None] and [Number]. 
    # Thus, the leaf node paths will contain every combination of the sets. In other words, every subset will be represented by a root-to-leaf path.
# The DFS operates like this:
    # First, we search the path with all the numbers. Then, when we reach our base-case, we append the solution.
    # After this call resolves, we pop one element off. Then we search the path with all the numbers besides the last number (this will be the set without the last number).
    # This process is continued until every path is searched. 
        # Time Complexity: O(N * 2^N). We have 2^N subsets, and each one, in the worst case, is size N (this is the same size as the amount of nodes in the tree - root nodes (2^N) * path length (N))
        # Space Complexity: O(N * 2^N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = []
        currSet = [] # We can use a single instance of the currSet by modifying/backtracking it for each recursive call. 
        def dfs(index):
            # Base case: If we have run out of elements
            if index >= len(nums):
                powerSet.append(currSet.copy()) # We must append a copy. The currentSet is passed in via REFERENCE, so we have to make a copy of it. 
                return
            
            # Recursive case 1: Adding a number to the subset
            currSet.append(nums[index])
            dfs(index + 1)
            # Recursive case 2: Not adding the number
            currSet.pop() # Backtracking
            dfs(index + 1)

        dfs(0)
        return powerSet
 

 # Less space efficient DFS Solution, as we pass through the currSet to each recursive call. 
 class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = []
        
        def dfs(index, currSet):
            # Base case
            if index >= len(nums):
                powerSet.append(currSet.copy())
                return

            currSet.append(nums[index])
            dfs(index + 1, currSet)
            
            currSet.pop()
            dfs(index + 1, currSet)           

        dfs(0, [])
        return powerSet  
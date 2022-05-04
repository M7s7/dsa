# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# METHOD 1: TWO POINTERS
# Time complexity: O(N) // Space complexity: O(1)

def twoSum(numbers, target):
    # Create left and right pointers
    left = 0
    right = len(numbers) - 1
    
    # While loop, when pointers still have not iterated over the entire array:
    while right > left:
        # Track total Sum and create conditionals to move pointers
        totalSum = numbers[left] + numbers[right]
        if totalSum == target:
            return left + 1, right + 1
        if totalSum > target:
            right -= 1
        else: 
            left += 1
    return left + 1, right + 1
    


# METHOD 2: BINARY SEARCH
# Time complexity O(N log N) (do binary search (log n ) * n times) // Space complexity: O(1)

def twoSum(self, numbers, target):
    # For each element, we want to binary search the rest of the array for the needed number
    for i, value in enumerate(numbers):
        k = target - value # Find complementary number to nums[i]
        
        # Now we search for k
        low = i + 1
        high = len(numbers) - 1

        # Binary search for k    
        while low <= high:     
            mid = low + (high - low) // 2
            
            if numbers[mid] == k: 
                return i + 1, mid + 1
            
            elif numbers[mid] > k:
                high = mid - 1
                
            else:
                low = mid + 1


# METHOD 3: HASHMAP. Store values in hashmap and search to see if the complementary number exists
# Time complexity: O(N) (N to create hashmap. Another N to iterate) // Space complexity: O(N)

def twoSum(self, numbers, target):
    # Store numbers in here; key = value, value = index
    indices = {}
    
    for i, value in enumerate(numbers):
        k = target - value
        
        if k in indices:
            return indices[k] + 1, i + 1
        
        indices[value] = i

# Basically, this is 3Sum but with an extra outerloop. Both index loops check for duplicates. Again, when it is initalised, the first instance of a duplicate IS OK on the j loop because nums i and j can be the same. 
# However, if, upon the next initalisation, the number is the same, then j and the previous j would have been the same, which is not allowed. Thus, we skip it. 
# The problem is reduced to a TwoSum eventually. 

def main():
    nums = [4, 1, 2, -1, 1, -3]
    target = 1
    print(fourSum(nums, target))


def fourSum(nums, target):
    # Sort the array first
    nums.sort()
    # List of quads
    quads = []
    
    # Iterate over each number, leaving 3 spaces for the other numbers
    for i in range(len(nums) - 3):
        # Check for duplicates. For every number, the 3Sum will have calculated all possibilities for that particular index. Thus, duplicate indexes can be skipped.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Now, initiate threeSum. threeSum will be called for every viable index. The index pointer is one to the right of i.
        for j in range(i + 1, len(nums) - 2):
            # Checking for duplicates. First instance of nums[j] and nums[i] being duplicates is FINE. However, if nums[j] and a previous nums[j] is the same, then we will be counting duplicate quadruplets. 
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # Initialise pointers for the subarray beyond i and j pointers. 
            l = j + 1
            r = len(nums) - 1
            
            # TwoSum
            while l < r:
                fourSum = nums[i] + nums[j] + nums[l] + nums[r]
                
                if fourSum == target:
                    quads.append([nums[i], nums[j], nums[l], nums[r]])
                    # Move either pointer, checking if duplicate
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1                    
                # As mentioned in 3Sum, duplicates are automatically filtered out of inequalities   
                elif fourSum < target:
                    l += 1   
                else:
                    r -= 1                      
    return quads
    

main()
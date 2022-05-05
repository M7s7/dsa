# Given an unsorted array of size n. Array elements are in the range from 1 to n. 
# One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

# METHOD 1: CYCLIC SORT. Sort the array - if we swap a duplicate number, we return that as the dupe. Keep sorting the array til the end
    # Then we pass through the array again and see which number is out of place in the 1 indexed array. We return the number that should have been there as the missing number. 
    # Time Complexity: O(N) - cyclic sort is N, then second pass is another N. // Space complexity: O(1) 

def main():
    arr = [3, 1, 2, 3, 6, 4]
    print(find_corrupt_numbers(arr))

def find_corrupt_numbers(nums):
    # Left pointer for nums list, dupe variable to store the duplicate number
    i = 0
    dupe = 0

    # Cyclic sort it, when we see the same number, store it
    while i < len(nums):
        # Each number should sit on the index where [value - 1]
        j = nums[i] - 1

        # Check if number is in the wrong index
        if i != j: 
            # If this condition is met, it means that there is a duplicate (as the same number is in 2 different indices). 
            if nums[i] == nums[j]:
                # Do not need to have this condition - just prevents us from re-recording the duplicate number (even without the condition, we will still get the right answer)
                if dupe == 0:
                    dupe = nums[i]
                # Then, we can skip this index to prevent an infinite loop
                i += 1

            # If not duplicates, we can swap. Keep doing this until we hit a duplicate or we have sorted i
            elif nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
        # If the number is in the right index, search the next
        else:
            i += 1

    
    # Now, we can scan the array and find the instance of the duplicate. We return the index of the unsorted duplicate and 1 index it to return the value of the missing number
    for i, value in enumerate(nums):
        # Again, find the index where each number should be
        j = value - 1

        if j != i:
            return (f"Duplicate: {dupe}, Missing: {i + 1}")
    return False

main()


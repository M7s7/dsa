# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Approach: Start on every index of the array. For the right side of that index, do two-sum to try to find a total sum of 0 between all three numbers.
# To prevent duplicate triplets, implement conditionals that skip duplicated numbers
# Time complexity is O(N^2) (technically + O(nlogn) due to sorting) // Space complexity is O(N) due to sorting

def main():
    arr = [-3, 0, 1, 2, -1, 1, -2]
    print(find_triplet(arr))


def find_triplet(nums):
    # Sort the array so we can use double pointers
# Sort the array
    nums.sort()
    # Create a list of lists of triplets
    triplets = []
    # Iterate through the array with your index pointer. Can leave 2 spaces in the array as a triplet is needed. 
    for index in range(len(nums) - 2):
        # Check if index number is a duplicate. If so, increment index. Instead of this, you can use while
        if index > 0 and nums[index] == nums[index - 1]:
            continue
        # Create two pointers (left and right) to iterate through the subarray to the left of index
        left = index + 1
        right = len(nums) - 1
        
        # While pointers are still valid:
        while left < right:
            trip_sum = nums[index] + nums[left] + nums[right]
            # Condition found; store list of values in triplets table
            if trip_sum == 0:
                triplets.append([nums[index], nums[left], nums[right]])

            if trip_sum < 0:
                left += 1
                # We need to check for duplicates, making sure that the pointers do not cross:
                while nums[left] == nums[left - 1] and left < right: 
                    left += 1

            else:
                right -= 1
                # We need to check for duplicates, making sure that the pointers do not cross:
                while nums[right] == nums[right + 1] and left < right: 
                    right -= 1
    return triplets


main()
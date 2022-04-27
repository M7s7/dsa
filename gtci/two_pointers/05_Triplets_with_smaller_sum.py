# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
# Write a function to return the count of such triplets.
# This question is similar to ThreeSum target, but the trick is with the counter. Every time a solution is found, we can add all triplets of (nums[i], nums[left], nums[left + 1 to right]) because the array is sorted. 
# Time complexity is O(N^2) (+ nlogn for sorting) // Space complexity is O(N) for sorting. 

def main():
    arr = [-1, 4, 2, 1, 3]
    target = 5
    print(find_triplets(arr, target))

def find_triplets(arr, target):
    # Sort to use two-pointer finding of numbers
    arr.sort()
    # Variables - counter for triplets, 
    count = 0

    # Increment over array - index of first number. Leave 2 spaces for pointers
    for i in range(len(arr) - 2):
        # Initialise pointers of subarray
        left = i + 1
        right = len(arr) - 1

        # 2Sum on subarray, searching for all pairs fitting the condition
        while left < right:
            # Variable for sum
            threeSum = arr[i] + arr[left] + arr[right]
            # Condition is met: 
            if threeSum < target:
                # Logically, all numbers from arr[left + 1] to arr[right] will be under the target when summed with arr[i] and arr[left], as the threeSum will only get lower as arr[right] goes to the right. Thus, we can count them all as valid triplets.
                count += right - left
                # Increment the bottom pointer up and check if the condition holds
                left += 1
            
            # If the condition is not met, then we will have to lower threeSum and recheck.
            else: 
                right -= 1
        return count

main()
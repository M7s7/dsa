# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Approach: Start on every index of the array. For the right side of that index, do two-sum to try to find a total sum of 0 between all three numbers.
# To prevent duplicate triplets, implement conditionals that skip duplicated numbers

def main():
    arr = [-3, 0, 1, 2, -1, 1, -2]
    print(find_triplet(arr))


def find_triplet(arr):
    # Sort the array so we can use double pointers
    arr.sort()
    # List of triplets
    triplets = []
    # For each number in array, have left and right pointers on the right subarray. Index can stop early as the subarray will be too small if it is size of 3 (needs two right spaces from index). Remember, range of len goes up to index len - 1. 
    for index in range(len(arr) - 2): 
        # DUPLICATE PREVENTION 1: For every index after [0], check if it is a duplicate of the previous number. If so, skip the number
        if index > 0 and index == arr[index - 1]:  
            continue

        left = index + 1
        right = len(arr) - 1

        # Check for triplets with a while loop - if the pointers are on the same index, you have failed as there will only be 2 numbers and not a triplet
        while left < right: 
            # Calculate triplet sum
            trip_sum = arr[left] + arr[right] + arr[index]
            # If statements to check validity - if invalid, we will increment the pointers:
            if trip_sum == 0:
                triplets.append([arr[index], arr[left], arr[right]])
            if trip_sum < 0:
                left += 1
                # DUPLICATE PREVENTION 2: Keep incrementing the pointer if it is the same as the previous. However, we want to make sure that the pointers do not cross
                while arr[left] == arr[left - 1] and left < right:
                    left += 1
            else: 
                right -= 1
                # DUPLICATE PREVENTION 3: Same as 2 - note that the previous is [right + 1] as we decrement this pointer instead of increment it
                while arr[right] == arr[right + 1] and left < right:
                    right -= 1
    return triplets


main()
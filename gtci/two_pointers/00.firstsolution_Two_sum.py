# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# First implementation of two sum - a little messy and fails on negative inputs. 

def main():
    arr = [2, 5, 9, 11]
    target = 11
    print(two_sum(arr, target))

def two_sum(arr, target):
    # Initialise the pointer at first and last index
    p1 = 0
    p2 = len(arr) - 1

    while arr[p1] + arr[p2] != target:
        # Sum is too large; decrement the end pointer
        if arr[p1] + arr[p2] > target:
            p2 -= 1
        # Sum is too small; increment the start pointer
        if arr[p1] + arr[p2] < target:
            p1 += 1
            
    return p1, p2


main()
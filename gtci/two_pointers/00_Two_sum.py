# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

def main():
    arr = [-1,-2,-3,-4,-5]
    target = -8
    print(two_sum(arr, target))


def two_sum(arr, target):
    # Initialise the pointer at first and last index
    left = 0
    right = len(arr) - 1

    while right > left:
        current_sum = arr[right] + arr[left]
        if current_sum == target:
            return left, right
        
        if current_sum < target: 
            left += 1

        else:
            right -= 1


    return right, left


main()
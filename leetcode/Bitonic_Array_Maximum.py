# Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
# Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

# Binary search - find last element that is increasing
    # This element is the largest

def find_max(nums):
    low, high = 0, len(nums) - 1

    # Find first number that is not in ascending order
    while low < high:
        mid = low + (high - low)//2
        # If there is still a larger number (ascending), search the right of mid
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        # If the number is decreasing, search the left
        else:
            high = mid   
    return nums[low]


def main():
    print(find_max([1,3,8,12,4,2]))
    print(find_max([3,8,3,1]))
    print(find_max([1,3,8,12]))
    print(find_max([10,9,8,7]))

main()
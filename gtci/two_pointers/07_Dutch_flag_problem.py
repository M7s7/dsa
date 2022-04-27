# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
# Initialise three pointers - left stores 0s, right stores 2s and index scans the array. 
# Time complexity is O(N) // Space complexity is O(1)

def main():

    arr = [1, 0, 2, 1, 0, 1, 1, 2, 0, 1, 0, 0]
    dutch_flag_sort(arr)
    print(arr)


def dutch_flag_sort(arr):
    # Initialise pointers
    left = i = 0
    right = len(arr) - 1

    # Initialise loop, where index goes through array. Make sure index does not go past right pointer or it will unsort the array
    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            # Move both pointers if swapping
            left += 1
            i += 1
        
        elif arr[i] == 2:
            arr[i], arr[right] = arr[right], arr[i]
            # Move right pointer. No need to move i pointer as we want to recheck it, just to check what arr[right] was originally
            right -= 1
        else: i+= 1


main()
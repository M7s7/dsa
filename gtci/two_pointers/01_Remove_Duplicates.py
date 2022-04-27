# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; after removing the duplicates in-place return the new length of the array. [I decided to return the array itself too]
# Time complexity: O(N) // Space complexity: O(1)
def main():
    arr = [2, 2, 2, 3, 6, 9, 11]
    print(remove_duplicates(arr))

def remove_duplicates(arr):
    # Create two pointers: One to iterate over the list, checking for duplicates, and one to track where to put the number in the index if different
    index, new_index = 0, 0

    # Loop over index, starting at 1
    for index in range(len(arr)):
        # Check if index and new_index are duplicates. If they are, then keep moving index up until they are not duplicates. 
        # If they are not duplicates, it is safe to increment new_index up one spot and place the new, unique number there. 
        if arr[index] != arr[new_index]:
            new_index += 1
            arr[new_index] = arr[index]

    return(arr[0:new_index + 1]), new_index + 1

main()

# Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.
# Use two pointers: One to iterate over the index and check for non-keys, the other as the location of where the non-key elements should be placed.
# Time complexity: O(N); Space complexity: O(1)

def main():
    key = 2
    arr = [2, 11, 2, 2, 1]
    print(remove_element(key, arr))

def remove_element(key, arr):
    # Initialise pointers - index to iterate over array; next as a location for the next non-key element
    index, next = 0, 0

    # Increment over array
    for index in range(len(arr)):
        # Compare index to the key. If it is not the key, store it at 'next' and move 'next' up one. If duplicate, just ignore it and keep going for a unique number. 
        if arr[index] != key:
            arr[next] = arr[index]
            next += 1
    # Again, 
    return next

main()
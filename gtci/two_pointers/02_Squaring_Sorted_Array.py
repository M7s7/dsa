# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
# Can do this multiple ways, but creating a dummy list instead of list reversal seems the most efficient as it is purely O(N).
# Time complexity is O(N) // Space complexity is O(N)

def main():
    arr = [-7,-3,2,3,11]
    print(square_array(arr))


def square_array(arr):
    # Create left and right pointers
    left = 0
    right = len(arr) - 1
    # Create insertion index in the square array
    index = len(arr) - 1

    # Create array of len(arr) with dummy values, replacing values in this array with final values
    square = [0 for i in range(len(arr))]

    # Move pointers until they converge, iterating over the entire array
    while left <= right:
        # Place larger square in right-most index, and then decrement index
        if abs(arr[left]) > arr[right]:
            square[index] = arr[left]**2
            # Increment left pointer to move up
            left += 1
        else: 
            square[index] = arr[right]**2
            # Increment right pointer to move down
            right -= 1
        # Move the index down 1
        index -= 1
    return square


main()
# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

# Approach - CYCLIC SORT, placing numbers on the appropriate index (1 on index 0, 2 on index 1, etc)
    # Note: Normal sorting won't work here as we want to put as many numbers on their indices as possible. All other numbers we will treat as garbage fillers. 
# Then, we will pass through the array and pass through the array, finding mismatched numbers until we reach k numbers. 
    # Time complexity: O(N + k) (n for the for the first two loops, and k for the last one) // Space complexity: O(k) (need to store the additional numbers)

def main():
    arr = [3, -1, 4, 5, 5]
    k = 3
    
    print(find_k(arr, k))


def find_k(arr, k):
    # List of answers we want to append our k missing numbers to
    ans = []
    # Implement Cyclic sort
    i = 0

    while i < len(arr):
        # This is the index that we want all numbers to go to
        j = arr[i] - 1 

        # Handling if j is out of bounds or if we hit a duplicate - we will just ignore the number if this is the case 
        if j < 0 or j >= len(arr) or arr[i] == arr[j]:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]

    # Some of the missing numbers MAY be actually included in our k values, so we must store them. [eg. [2, 3, 4] will be sorted [4, 2, 3] but 4 should not be ignored for k = 2]
    extra_numbers = set()
    # At this step, we will be appending numbers that are missing in the array AND storing the numbers that currently don't belong. 
    for i in range(len(arr)):
        if k == 0:
            break
        # Condition if number is not sorted properly
        if i + 1 != arr[i]:
            # Add the number that should have been at the index
            ans.append(i + 1)
            # Also add the number that is actually there to our extra numbers
            extra_numbers.add(arr[i])
            k -= 1

    # If we still do not have enough missing numbers, add more to the end. Remember, we have already checked all numbers up to len(n). 
    i = 1 + len(arr) # Again, we can add (len(arr)) as we have already checked all the valid numbers from 1 to len(n) in the loop above
    while k != 0:
        # We will be going through the numbers from 1, checking if they are missing (eg. not in the original array) until we satisfy finding the remaining k 
        if i not in extra_numbers:
            ans.append(i)
            k -= 1
        i += 1

    return ans


main()
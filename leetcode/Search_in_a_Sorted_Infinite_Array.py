# Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array. 
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

import math

# Given by the problem
class ArrayReader:
    def __init__(self, arr):
        self.arr = arr
    
    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]

# Written by me:
def search(reader, key):
    # Find what the low and high bounds are for the search space. 
    low, high = 0, 1
    # If the number is not in the search space, double our high bound exponentially until we find it. 
    while reader.get(high) < key:
        low = high + 1
        high = high * 2
    
    # Now conduct binary search. Exit condition is when low and high are past each other. Thus, if high and low are equal, line 30 will check if they are equal to the key. 
    while low <= high:
        mid = low + (high - low)//2
        mid_val = reader.get(mid)
        
        if mid_val == key:
            return mid

        elif mid_val < key:
            low = mid + 1
        
        else:
            high = mid - 1
    # If we exit without finding the key, return -1
    return -1

def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search(reader, 6))

main()
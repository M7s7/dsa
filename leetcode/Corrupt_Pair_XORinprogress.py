def main():
    arr = [3, 1, 2, 3, 6, 4]
    print(find_corrupt_numbers(arr))

def find_corrupt_numbers(nums):
    # XOR all the indices (adding 1 to the number), and then add all the numbers in the array. The numbers that remain will be the two numbers.  
    numxor = 0
    # Numxor
    for num in nums:
        numxor ^= num

    # Get rid of the range. Remember range is 1 to n, which is len(nums). However, range by default stops one before the number in range, so we add one.
    for i in range(1, len(nums) + 1):
        numxor ^= i


    return numxor
        
main()

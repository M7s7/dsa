# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:
#    Starting with any positive integer, replace the number by the sum of the squares of its digits.
#    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#    Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.

# This question is essentially a LINKED-LIST question, where the node is the number (head node being n), and the next pointer is the function of squaring the digits and adding them. 
# Thus, we can tackle the problem through either Floyd's cycle detection (better) or a hashmap (easier).
# We also need a function to give us the next 'node' - this is 'squareSum' in my implementation. Two versions - one is simple operations, the other uses divmod. 

# METHOD 1: Fast and slow pointers, using Floyd's cycle detection algorithm.
# Two pointers go through the .next process in the form of going through the squareSum function. 
# If they equial the same number, there is a cycle; note there is an edge case that we have to account for when fast and slow both == 1 (which would mean no cycle) 
# Time complexity: O(log n) (technically O(2 log n) as there are 2 pointers). This is because the number of digits in any number is logN + 1 (base 10) (eg. log100 is 2, log1000 is 3)
# Space complexity: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        # Use fast and slow pointer - if they equal, then we know there is a cycle
        fast, slow = n, n
        
        # Condition - while fast is not a happy number
        # Remember that 1 will always return 1 through the squaresum function so it does not matter if we skip the first instance of 1
        while fast != 1:
            # Slow goes through the process once; fast goes through the process twice
            slow = squareSum(slow)
            fast = squareSum(squareSum(fast))
            
            # Check if the pointers match, but be careful - if the first squareSum pass makes them both happy numbers (eg. if n = 10), then we will return a false positive.
            # Thus, we have to check if fast is 1 or not
            if slow == fast and fast != 1:
                return False
        return True
        
# This is the cleaner implementation of the squareSum function
def squareSum(num):
    # New number will be sum of squares of all digits of old number
    new_num = 0
    # If number is equal to zero, we have gone through all the digits in the number
    while num != 0:
        # Divmod takes a numerator and denominator; returns the quotient and the remainder (in this case, the remaining old number and the digit to square)
        num, digit = divmod(num, 10)
        new_num += digit ** 2

    # Return the new_number
    return new_num


# METHOD 2: Hashmap. Using only one pointer, store every value travelled to on the hashmap. Return false if a number has been repeatedly visited.
# Time complexity: O(logn) for the same reasons as above.
# Space complexity: O(logn) - space depends on how many numbers we are storing, and how many digits are in each of those numbers. 

class Solution:
    def isHappy(self, n: int) -> bool:
        # Hashmap storing nodes that we have seen before
        seen = {}    
        # While the number is not a happy number, we want to continue performing the square sum function
        while n != 1:
            # We check to see if we have seen n before
            if n in seen:
                return False 
            else: seen[n] = True
            # Find the next number - go through the process of squaring and adding
            n = squareSum(n)
        # If the condition is broken, n = 1 and thus the original number was a happy number
        return True

# This is the uglier, less pythonic implementation of the squareSum function.
def squareSum(num):
    # New number will be sum of squares of all digits of old number
    new_num = 0
    # If number is equal to zero, we have gone through all the digits in the number
    while num != 0:
        digit = num % 10
        # Add squared digit to num number total
        new_num += digit ** 2
        # Update old number to remove last digit - iterating through all the digits in the number
        num //= 10

    # Return the new_number
    return new_num
    
## MATHEMATICAL ANALYSIS ON TOTAL TIME COMPLEXITY:
# Calculating the next number also involves iterating through those digits, so, with insignificant constants, it would be:
# O(243⋅3 + logn +loglogn+ logloglogn)... = O(log⁡n)
# 243 * 3 comes from processing 3 digits 243 times (243 is the largest number we can get, because 999's squareSum is 243, meaning that 243 acts as a ceiling). 
# If the number starts higher than 243, then we have to process it logn + loglogn + logloglogn... amount of times until it goes down to 243. 
# Luckily, the auxilary values are so small that this simplifies down to O(logN)
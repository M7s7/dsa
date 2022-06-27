# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
# Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.


# Approach - Return the largest number. 
    # We can reach any 9 digit with 9 1s. Since we can contribute 1 to each place for every added number, the maximum numbers we need is the biggest value. 
    # Time Complexity: O(N)
    # Space Complexity: O(1)

class Solution:
    def minPartitions(self, n: str) -> int:
        max_num = n[0]
        
        for num in n:
            max_num = max(max_num, num)
        
        return max_num

# One line equivalent
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)


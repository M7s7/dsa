# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# Greedy solution using stack. 
    # Push each number to the stack. Make sure the stack is as monotonically increasing as we can make it (ie. if the top digit on the stack is larger than the current number, remove it if we can)
    # This works because the left most digits are HIGHER PRIORITY. Thus, even a small decrease in the left most digit will be better than a larger decrease on the right (for 329, (3)29 is smaller than 32(9))
        # Time Complexity: O(N)
        # Space Complexity: O(N)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # We can get away with an array stack, as we will only be pushing and popping to the right (O(1))
        stack = []
        for digit in num:
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If we have k remaining, remove the right most k digits
        stack = "".join(stack[:len(stack) - k])
        if stack:
            # Convert to an int first to remove leading zeroes
            return str(int(stack))
        # If array is empty (k >= string length), then return 0
        else:
            return '0'

            
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
# Note that division between two integers should truncate toward zero.
# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


# APPROACH: USE A STACK to keep elements in left to right order. 
    # Time Complexity: O(N) one pass
    # Space Complexity: O(N) but actually something like 1/2N because operators are some of the values
# Cleaner solution using anonymous functions. Operations are mapped in a hashmap
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y : int(x/y) # Cannot use // in python. Eg, for -1/10, python floors it to -1 instead of 0
        }

        for token in tokens:
            if token in operations:
                # Be careful - the order the numbers are popped off is right to left, not left to right
                r_num, l_num = stack.pop(), stack.pop()
                val = operations[token](l_num, r_num)
                stack.append(val) 
            else:
                stack.append(int(token))     
        return stack[0]


# More explicit solution with conditionals for each operator. 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char in "+-/*":
                r_num = stack.pop()
                l_num = stack.pop()
                
                if char == '+':
                    val = r_num + l_num
                if char == '-':
                    val = l_num - r_num
                if char == '/':
                    val = int(l_num / r_num)
                if char == '*':
                    val = r_num * l_num
                stack.append(val)
            else:
                int(stack.append(char))
        return stack[0]
                    
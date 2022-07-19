# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
    # MinStack() initializes the stack object.
    # void push(int val) pushes the element val onto the stack.
    # void pop() removes the element on the top of the stack.
    # int top() gets the top element of the stack.
    # int getMin() retrieves the minimum element in the stack.

# You must implement a solution with O(1) time complexity for each function.
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Approach 1: Two Stacks
    # Every push, we will also push on the current minimum on a different stack. 
    # Elements are pushed and pop in sync with the two stacks.
# Time Complexity: O(1) per operation
# Space Complexity: O(N)
import collections
class MinStack:
    def __init__(self):
        self.stack = collections.deque()
        self.min_stack = collections.deque()
        
    def push(self, val: int) -> None:
        min_val = val
        if self.min_stack: 
            min_val = min(min_val, self.min_stack[-1])
        self.min_stack.append(min_val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Approach 2: Hashmap
    # Store the minimum at every length of the stack (length as the key), modifying it when needed. 
# Time Complexity: O(1) per operation
# Space Complexity: O(N), but worse than two stacks as it never reduces (unless we del keys)
class MinStack: 
    def __init__(self):
        self.size = 0
        self.min_val = {}
        self.stack = collections.deque()
        
    def push(self, val: int) -> None:
        self.size += 1
        curr_min = val
        if self.size > 1:
            curr_min = min(self.min_val[self.size - 1], curr_min)
        self.stack.append(val)
        self.min_val[self.size] = curr_min

    def pop(self) -> None:
        self.size -= 1
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[self.size]



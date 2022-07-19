# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Approach: This problem is basically the same as the Fibonnaci sequence. 
    # We can calculate the amount of unique steps it takes from the start to each path.
    # Since every step k can be reached by k-1 or k-2 (1 or 2 stepper), we can add the paths of both of those steps to get the paths to k.

# Recursion
    # Time Complexity: O(2^N)
    # Space Complexity: O(N) ?? Not sure
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2     
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# DP (Top Down)
    # Time Complexity: O(N)
    # Space Complexity: O(N) 
class Solution:
    memo = {
        1:1,
        2:2
    }
    
    def climbStairs(self, n: int) -> int:
        if n in self.memo: 
            return self.memo[n]      
        else:
            paths = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.memo[n] = paths
            return paths


# DP (Bottom Up, Hashmap)
    # Time Complexity: O(N)
    # Space Complexity: O(N) 
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {
            1:1,
            2:2
        }

        paths = 0
        for i in range(1, n + 1):
            if i not in memo:
                memo[i] = memo[i - 1] + memo[i - 2] 
        return memo[n]


# DP (Bottom Up, Constant Space)
    # Time Complexity: O(N)
    # Space Complexity: O(1) 
class Solution:
    def climbStairs(self, n: int) -> int:
        left = 1
        right = 2
        steps_left = n - 2
        
        if n < 2:
            return n        
        for i in range(steps_left):
            temp = left + right
            left = right
            right = temp       
        return right
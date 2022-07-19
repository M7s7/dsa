# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Approaches: Recursive -> Top down -> Bottom Up
# Recursion
    # Time Complexity: O(2^N) - Exponential time (number of elements in binary tree recursive call)
    # Space Complexity: O(N) - maximum depth of DFS (recursion) is depth of tree, or N
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        max_i = len(cost) - 1
        
        def minCost(i):
            if i == 0:
                return cost[0]
            elif i == 1:
                return cost[1]
            
            return cost[i] + min(minCost(i - 1), minCost(i - 2))
        
        return min(minCost(max_i), minCost(max_i - 1))


# Top down DP
    # Time Complexity: O(N) (only one branch of the recursive tree is needed to be explored - the rest of the values are stored)
    # Space Complexity: O(N) - depth of recursive tree, and O(N) for memo
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {
            0 : cost[0],
            1 : cost[1]
        }
        max_i = len(cost) - 1
        
        def minCost(i):
            if i in memo:
                return memo[i]
             
            new_cost = cost[i] + min(minCost(i - 1), minCost(i - 2))
            memo[i] = new_cost                       
            return new_cost
        
        minCost(max_i)
        return min(memo[max_i], memo[max_i - 1])


# Bottom Up DP - Hashmap
    # Time Complexity: O(N)
    # Space Complexity: O(N) - memo hashmap
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        steps = len(cost)
        
        for i in range(steps):
            if i < 2:
                memo[i] = cost[i]
            else:
                memo[i] = cost[i] + min(memo[i - 1], memo[i - 2])
        return min(memo[steps - 1], memo[steps - 2])


# Bottom Up DP - Constant space
    # Time Complexity: O(N)
    # Space Complexity: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_a = cost[0]
        cost_b = cost[1]
        
        for i in range(2, len(cost)):
            temp = cost[i] + min(cost_a, cost_b)
            cost_a = cost_b
            cost_b = temp
        
        return min(cost_a, cost_b)
# Classic N Knapsack problem

# Recursive Solution
def solve_knapsack(profits, weights, capacity):
  max_profit = 0

  def recursion(i, curr_profit, curr_weight):
    if curr_weight > capacity:
      return

    nonlocal max_profit
    max_profit = max(curr_profit, max_profit)
    for i in range(i, len(profits)):
      p = profits[i]
      w = weights[i]
      recursion(i + 1, curr_profit + p, curr_weight + w)
  
  recursion(0, 0, 0)
  return max_profit

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
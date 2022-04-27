# Given an integer n, return a string array answer (1-indexed) where Fizz is printed when i divisible by 3, Buzz when i is divisible by 5, i if neither and FizzBuzz if both. 
# This solution is still simple - uses basic concatenation to avoid too many else statements
# Time complexity is O(N) // Space complexity is O(N)

def fizzBuzz(self, n: int) -> List[str]:
    list = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if output == "":
            output = str(i)
        list.append(output)
    return list
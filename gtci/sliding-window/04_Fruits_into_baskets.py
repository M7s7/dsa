# Given an array of fruits, find the maximum total number of fruits that you can fit in 2 buckets. Each bucket can only hold one type of fruit. You can start with any fruit, but you cannot skip fruits after starting. 
# This problem can be simplified to finding the longest substring with k distinct characters where K = 2. Thus, the problem is solved the exact same way. 
# Time complexity is O(N). Space complexity is O(K) (in this case, it will always be a maximum of O(3), simplified to O(1))

def main():
    fruits = ['A', 'B', 'C', 'B', 'B', 'C']
    print(fruits_into_baskets(fruits))


def fruits_into_baskets(fruits):
    # Initialise variables - windowStart is the leftmost element, the max variables are storing the current maximum of fruits in the basket
    windowStart, maxFruit = 0, 0
    # Create hash-table to store current count of fruits
    fruitCount = {}

    # Iterate over the entire array
    for windowEnd in range(len(fruits)):
        # Add new element to the hashtable, checking to see if it is already in there
        if fruits[windowEnd] not in fruitCount: 
            fruitCount[fruits[windowEnd]] = 1
        else: fruitCount[fruits[windowEnd]] += 1 

        # While loop to check for condition, removing elements from the left until condition is met. If left element was unique, we can continue adding elements to the new substring and check for a new maximum. If not unique, then the substring was already at its maximum. 
        while len(fruitCount) > 2: # 2 is the hardcoded basket size in the problem
            fruitCount[fruits[windowStart]] -= 1
            # Remove element if no longer in the dictionary
            if fruitCount[fruits[windowStart]] == 0:
                del fruitCount[fruits[windowStart]]
            # Move windowStart forward
            windowStart += 1

        # Calculate current maximums - Fruit amount is the size of the array at the current time
        maxFruit = max(windowEnd - windowStart + 1, maxFruit)
    return maxFruit


main()

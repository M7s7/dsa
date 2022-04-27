# Basically, find the longest substring of k distinct characters where k = 2. 
# Time complexity is O(N); Space complexity is O(1)

def totalFruit(fruits):
    # Initiate variables - i is the index for left most element
    maxFruits, i = 0, 0
    
    # Create a hashmap of frequency, storing the occurences of fruit types and how many
    freq = {}
    
    # Increment over the trees
    for j in range(len(fruits)):
        # Add fruit to frequency table
        if fruits[j] not in freq:
            freq[fruits[j]] = 1
        else: freq[fruits[j]] += 1
        
        # Check condition: valid solution is when total items is equal to 2
        while len(freq) > 2:
            # Remove left-most element until condition is satisfied, updating hashmap as you go
            freq[fruits[i]] -= 1
            # If the frequency is 0, then it is no longer in the window
            if freq[fruits[i]] == 0: 
                del freq[fruits[i]]
            # Increment i to close the window
            i += 1
    
        # Number of fruits is equal to the size of the window
        maxFruits = max(maxFruits, j - i + 1)
    return maxFruits
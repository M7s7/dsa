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



##  Alternate implementation, where window is not constantly shrunk but rather shrunk once. Return the size of the current window

def totalFruit(self, fruits):
    freq = {}
    start = 0
    for i, fruit in enumerate(fruits):
        # Add elements to the window
        if fruit not in freq: 
            freq[fruit] = 1
        else: freq[fruit] += 1
    
        # Check if window is valid - if not, we remove an element
        if len(freq) > 2:
            first = fruits[start]
            freq[first] -= 1
            start += 1
            if freq[first] == 0:
                del freq[first]

    return i - start + 1
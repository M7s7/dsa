# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.


# Double hashmaps. Create a hashmap both 'forwards' and 'backwards'. 
    # Then check if both strings adhere to the mapping. If they don't it is not a valid map
    # Time Complexity: O(N*k) - where k is the length of the pattern
    # Space Complexity: O(N*k) - N*k for output. Also, N for maps: For each word (N), 2 maps are created of max 26 size (as we will exit if there is a discrepency in mapping)
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def mapLetters(word):
            map1 = {} # Mapping each letter in the pattern to a letter in the word
            map2 = {} # Mapping each letter in the word to a letter in the pattern
            for i in range(len(pattern)):
                if pattern[i] not in map1:
                    map1[pattern[i]] = word[i]
                if word[i] not in map2:
                    map2[word[i]] = pattern[i]
                # Compare the keys for each string to the other string to see if they match.
                if map1[pattern[i]] != word[i] or map2[word[i]] != pattern[i]:
                    return False
            return True
        # Filter will return an iterable of 'True' results from the function - aka every valid word. 
        return list(filter(mapLetters, words))


# Double hashmaps, using zip
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def mapLetters(word):
            map1 = {}
            map2 = {} 
            # Zip for parallel iteration (both strings at the same time): 'a' will be a char from word, 'b' will be a char from pattern
            for a, b in zip(word, pattern):
                if a not in map1:
                    map1[a] = b
                if b not in map2:
                    map2[b] = a
                if map1[a] != b or map2[b] != a:
                    return False
            return True
        return list(filter(mapLetters, words))


# My trash implementation of one hashmap. 
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        
        for word in words:
            key = {}
            flag = 0
            for i in range(len(pattern)):
                # Map each letter of the pattern to the words
                if pattern[i] not in key:
                    # If the value has already been mapped, then our permutation is wrong
                    if word[i] in key.values():
                        flag = 1
                        break
                    key[pattern[i]] = word[i]
                # If it is a letter we have seen before, see if it matches the pattern
                else:
                    if key[pattern[i]] != word[i]:
                        flag = 1
                        break
            if flag == 0:
                ans.append(word)
        return ans
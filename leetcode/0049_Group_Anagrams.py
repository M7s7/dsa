# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# HASHMAP SOLUTIONS
# Approach 1: For each word, use a tuple of its frequency of characters (tuple of an array of 26 elements) as its key. 
    # Time Complexity: O(N * (M + 26)) where N is number of words, M is length of each word
    # Space Complexity: O(26N)
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Defaultdict will add an empty list for a key if it doesn't exist
        anagram = collections.defaultdict(list)
        key = [0] * 26
        
        for word in strs:
            # Reset key to all zeroes
            for i in range(len(key)):
                key[i] = 0
            for char in word:
                # Assign char index to 0 to 25
                index = ord(char) - ord('a')
                key[index] += 1
            # Add element to hashmap
            anagram[tuple(key)].append(word)
        return list(anagram.values())


# Approach 2: SORTING: The sorted word will be the key. 
    # Time Complexity: O(N * MlogM)
    # Space Complexity: O(N * M)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            key = str(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())
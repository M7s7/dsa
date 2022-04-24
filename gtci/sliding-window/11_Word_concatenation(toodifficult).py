# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.
# INCOMPLETE - TOO DIFFICULT AT THIS TIME TO DO

def main():


def find_word_concatenation(str, words):
    # Store indices found in a list
    index = []

    # Create hashmap to store how many times a word appears in the string
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else: word_freq[word] += 1
    
    # Store variables
    word_count = len(word_freq)
    word_length = len(word[0]) # words are of the same length so any word will do
    
    # Increment windowStart and slowly close the window. windowStart only has to travel to len(str) - the length of a possible concatenated string (as there has to be enough array space for the right side of the window to fit the concatenated string)
    for windowStart in range((len(str) - word_count * word_length) + 1):
        # Create a hashmap to count how many words have been seen and refresh it every time the window shrinks
        words_seen = {}
        # Move the right side of the window (relative to windowStart) and check for words
        for windowExtend in range(0, word_count):
            next_word_index = windowStart + windowExtend * word_length
            
            word = str[next_word_index: next_word_index + word_length]
            if word not in word_freq:
                break

        if word not in words_seen:
            words_seen[word] = 0
        words_seen[word] += 1
main()
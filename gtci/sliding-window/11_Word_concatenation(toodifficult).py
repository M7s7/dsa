# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.
# INCOMPLETE - TOO DIFFICULT AT THIS TIME TO DO

def main():
    string = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    print(find_word_concatenation(string, words))

def find_word_concatenation(str, words):
    # Variables
    word_length = len(words[0])
    starting_indices = []
    i = 0
    match = 0
    # Create hashmap of frequency of the words
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else: freq[word] += 1
    # Create a copy if a reset is needed
    duplicate_freq = freq

    # Initialise window, incrementing range by word length until the end, starting window at the last letter of the first word
    for j in range(0, len(str), word_length):
        # Temp variable for current string
        substring = str[j: j + word_length]

        # If word is found in hashmap, decrement hashmap
        if substring in freq:
            freq[substring] -= 1
            if freq[substring] == 0:
                match += 1
            # Move substring if freq is too negative
            while freq[substring] < 0:
                if str[i: i + word_length] == substring:
                    freq[str[i: i + word_length]] += 1
                    if freq[str[i: i + word_length]] > 0:
                        match += 1
                i += word_length
                    

        print(match)

        # If there is a word not found in the hashmap, we have to reset the entire thing.
        if substring not in freq: 
            match == 0
            # Reset the hashtable
            freq = duplicate_freq
            # Move i up the hashtable
            i = j + word_length     

        # If match is found, append it to the list of starting indices.
        if match == len(freq):
            starting_indices.append(i)
            # Then, to prepare for the next one, remove the first element and add it back to the hashtable. Also, remove a matching
            freq[str[i: i + word_length]] += 1
            match -= 1
            i += word_length
    return starting_indices


main()
import random

wordList = 'wordlist.txt'

def get_random_word(min_word_length):
    """ Chooses a random word from the word list using no extra memory.
    """
    words = []
    with open(wordList, 'r') as file:
        for word in file:

            # skips word if contains parentheses
            if '(' or ')' in word:
                continue
            word = word.strip().lower()

            # skip word if it's too short
            if len(word) < min_word_length:
                continue

            words.append(word)
    return random.choice(words)


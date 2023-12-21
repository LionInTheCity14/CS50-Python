import random, string
from words import list_of_words as words

def get_valid_word(words):
    word = ' '
    while '-' in word or ' ' in word :
        word = random.choice(words) #randomly choose something from the list

    return word

def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word) # letters in the word (set, so unique)
    print(len(word), set(word))
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

hangman()
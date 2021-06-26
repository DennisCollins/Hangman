
import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    user_input = input("Let's play hangman. Hit enter: ")
    # getting the user's input
    while len(word_letters) > 0 and lives > 0:
        # letter already used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what the current word is ( _ _ _ D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes away a life if wrong
            print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You just guessed that letter. Try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when the len(word_letters)  == 0 OR when lives == 0
    if lives == 0:
        print('Sorry. You died. The word was', word, '.')
    else:
        print('You are right! You guessed the word', word, '!')


print(hangman())


from random import choice
from os import system
from time import sleep as sl

hangman = [
    """
    _______
    |     |
    |     O
    |    -|-
    |     |
    |    / \\
    |
    """,
    """
    _______
    |     |
    |     O
    |    -|-
    |     |
    |    / 
    |
    """,
    """
    _______
    |     |
    |     O
    |    -|-
    |     |
    |      
    |
    """,
    """
    _______
    |     |
    |     O
    |    -|
    |     |
    |      
    |
    """,
    """
    _______
    |     |
    |     O
    |     |
    |     |
    |      
    |
    """,
    """
    _______
    |     |
    |     O
    |      
    |     
    |      
    |
    """,
    """
    _______
    |     |
    |      
    |      
    |     
    |      
    |
    """]
words = ["hello","world"]

word = choice(words)
word_letters = set(word)
alphabet = set('abcdefghijklmnopqrstuvwxyz')
used_letters = set()

lives = 6

while len(word_letters) > 0 and lives > 0:
    system("cls")
    # Clear terminal
    print(hangman[lives])
    # Man picture

    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').lower()

    if user_letter in alphabet - used_letters:
        sl(0.4)
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            lives -= 1
            print('Letter is not in word.')
            sl(1)
    elif user_letter in used_letters:
        print('You have already used that character. Please try again.')
        sl(1)
    else:
        print('Invalid character. Please try again.')
        sl(1)
if lives == 0:
    print('Sorry, you died. The word was', word)
else:
    print('Congratulations! You guessed the word', word)
input()

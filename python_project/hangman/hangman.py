import os
from random import choice
os.chdir('python_project/hangman')

with open('words_to_choose.txt', 'r') as f:
    secret_word = choice(f.readlines()).strip()
    
with open('hangman.txt','r') as f:
    content = f.read()
stages = content.split('######\n')

blanks = ["_"] * len(secret_word)
wrong_guess = 0
guessed = 0


qwerty = (
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"     
)

def char_search(user):
    for i, ch in enumerate(secret_word):
        if ch == user:
            blanks[i] = user

def user_validation(user):
    if len(user) != 1:
        print(f'one letter only')
        return False

    if user not in qwerty:
        print('letters only')
        return False
    else:
        return True


while wrong_guess < len(stages) and '_' in blanks:
    attempts = f'{wrong_guess} / {len(stages)}'
    print(" ".join(blanks))
    user_input = input('character: ').lower()
    if user_validation(user_input):
        if user_input not in secret_word:  
            print(stages[wrong_guess])
            wrong_guess+=1
            print(attempts)

        else:
            guessed+=1
            char_search(user_input)
            print(" ".join(blanks))
            print(stages[wrong_guess])
            print(attempts)
    




    

'''
Answer for Question 5. Kids' Friendly.

Author:
SID:
Unikey:
'''

import random

'''
This part should be your solution from Assignment 1, 3. Functions.
'''


def is_valid_name(name: str) -> bool:
    if 9 >= len(name) >= 1 == len(name.split()) and name[0].isalpha():
        return True
    else:
        return False


def is_profanity(word: str, database='/home/files/list.txt', records='/home/files/history.txt') -> bool:
    with open(database, 'r') as f:
        crude_words = f.read()
        if crude_words.find(word) != -1:
            with open(records, 'a') as f:
                add_word = f.write
                add_word(word + '\n')
            return True
        else:
            return False


def count_occurrence(word: str, file_records="/home/files/history.txt", start_flag=True) -> int:
    if not isinstance(word, str):
        print(f'First argument must be a string object!')
        return 0
    if len(word) == 0:
        print(f'Must have at least one character in the string!')
        return 0
    with open(file_records, 'r') as f:
        bad_word = f.read()
        if bad_word.find(word) != -1:
            start_flag = False
            count = bad_word.count(word)
            return count
        else:
            start_flag = True
            count = bad_word.count(word[0])
            return count
        

def generate_name(word: str, src="/home/files/animals.txt", past="/home/files/names.txt") -> str:
    if src != "/home/files/animals.txt":
        print(f'Source file is not found!')
        return "Bob"
    if not isinstance(word, str):
        print("First argument must be a string object!")
        return "Bob"
    if len(word) == 0:
        print(f'Must have at least one character in the string!')
        return "Bob"
    with open(src, 'r') as f:
        names = f.read().splitlines()
        return f'{new_name}'

def main():
    while True:
        check_name = input("Check name: ")
        is_profanity(check_name)
        if is_profanity(check_name) == True:
            count_occurrence(check_name)
        is_valid_name(check_name)
        if is_profanity(check_name) == True  and is_valid_name(check_name) == False:
            new_name = generate_name(check_name)
            print(f'Your new name is {new_name}')
        else:
            print(f'{check_name} is a valid name!')




if __name__ == "__main__":
    main()


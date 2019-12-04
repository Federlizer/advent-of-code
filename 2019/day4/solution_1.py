#!/usr/bin/env python3

puzzle_input = '236491-713787'
min_value, max_value = puzzle_input.split('-')

def find_adjecent_digits(string):
    previous_char = None

    for char in string:
        if previous_char == None:
            previous_char = char
            continue

        if char == previous_char:
            return True

        previous_char = char

    return False


def digits_increase(string):
    previous_number = -1

    for char in string:
        num = int(char)
        if num < previous_number:
            return False

        previous_number = num

    return True


def meets_criteria(n):
    n_str = str(n)

    if len(n_str) != 6:
        return False

    if not find_adjecent_digits(n_str):
        return False

    if not digits_increase(n_str):
        return False

    return True

possible_passwords = []

for n in range(int(min_value), int(max_value)):
    if meets_criteria(n):
        possible_passwords.append(n)

print(len(possible_passwords))


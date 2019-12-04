#!/usr/bin/env python3

puzzle_input = '236491-713787'

min_value, max_value = puzzle_input.split('-')

def find_two_adjecent_digits(string):
    digit_count_dict = {}

    for char in string:
        if char in digit_count_dict:
            digit_count_dict[char] += 1
        else:
            digit_count_dict[char] = 1

    if 2 in digit_count_dict.values():
        return True
    else:
        return False



def digits_increase(n):
    previous_number = -1

    for char in n:
        num = int(char)
        if num < previous_number:
            return False

        previous_number = num

    return True


def meets_criteria(n):
    n_str = str(n)

    if len(n_str) != 6:
        return False

    if not find_two_adjecent_digits(n_str):
        return False

    if not digits_increase(n_str):
        return False

    return True


possible_passwords = []

for n in range(int(min_value), int(max_value)):
    if meets_criteria(n):
        possible_passwords.append(n)

print(len(possible_passwords))

#!/usr/bin/env python3

from executeprogram import execute_program

def test_all_possibilities(program, desired_output):
    for noun in range(100):
        for verb in range(100):
            program[1] = noun
            program[2] = verb

            output = execute_program(program)
            
            if (output == desired_output):
                return (noun, verb)


with open('./input.txt') as file:
    program = file.read()[:-1].split(',')
    # convert to ints
    program = [int(x) for x in program]

    desired_output = 19690720

    noun, verb = test_all_possibilities(program, desired_output)
    result = 100 * noun + verb

    print('Result is {}'.format(result))

#!/usr/bin/env python3

from executeprogram import execute_program


with open('./input.txt') as file:
    program = file.read()[:-1].split(',')
    program = [int(x) for x in program]

    # replace values as required from the problem
    program[1] = 12
    program[2] = 2

    output = execute_program(program)

    print(output)

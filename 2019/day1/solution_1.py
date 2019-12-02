#!/usr/bin/env python3

def calculate_fuel_required(mass: int):
    # divide and round down
    fuel_required = ( mass // 3 ) - 2

    return fuel_required


with open('./input.txt') as input:
    total_fuel_required = 0
    data = input.read()

    for mass in data[:-1].split('\n'):
        fuel_required = calculate_fuel_required(int(mass))
        total_fuel_required += fuel_required

    print(total_fuel_required)

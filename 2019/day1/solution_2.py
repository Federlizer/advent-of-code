#!/usr/bin/env python3

def calculate_fuel_required(mass: int):
    total_fuel_required = 0;

    fuel_required = ( mass // 3 ) - 2

    while fuel_required > 0:
        total_fuel_required += fuel_required
        fuel_required = ( fuel_required // 3 ) - 2

    return total_fuel_required


with open('./input.txt') as file:
    total_fuel_required = 0
    data = file.read()

    for mass in data[:-1].split('\n'):
        fuel_required = calculate_fuel_required(int(mass))
        total_fuel_required += fuel_required

    print(total_fuel_required)

#!/usr/bin/python3

import math

def calculate_fuel(mass):
    ret = math.floor(int(mass) / 3) - 2
    if ret < 0:
        return 0
    return  ret

def parse_input_1():
    with open('input.txt') as input_file:
        total_fuel = 0
        for mass in input_file:
            fuel = calculate_fuel(mass)
            total_fuel += fuel
        print(total_fuel)


def parse_input_2():
    with open('input.txt') as input_file:
        total_fuel = 0
        for mass in input_file:
           m = int(mass)
           module_fuel = 0
           while m > 0:
               m = calculate_fuel(m)
               module_fuel += m
           total_fuel += module_fuel
           print(module_fuel)
        print("Total: " + str(total_fuel))


def main():
    print("Here we go !")
#    parse_input-1()
    parse_input_2()

main()



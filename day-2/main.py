#!/usr/bin/python3

import sys

_input="1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,6,23,2,6,23,27,2,27,9,31,1,5,31,35,1,35,10,39,2,39,9,43,1,5,43,47,2,47,10,51,1,51,6,55,1,5,55,59,2,6,59,63,2,63,6,67,1,5,67,71,1,71,9,75,2,75,10,79,1,79,5,83,1,10,83,87,1,5,87,91,2,13,91,95,1,95,10,99,2,99,13,103,1,103,5,107,1,107,13,111,2,111,9,115,1,6,115,119,2,119,6,123,1,123,6,127,1,127,9,131,1,6,131,135,1,135,2,139,1,139,10,0,99,2,0,14,0"
input_test="1,9,10,3,2,3,11,0,99,30,40,50"


def compute(operation, value1, value2):
    if operation == 1:
        return (value1 + value2)
    if operation == 2:
        return (value1 * value2)
    if operation == 99:
        return -1
    print ("Wrong operation: " + int(operation))
    sys.exit(1)

def parse_four(input_array, i):
    if input_array[i] == 99:
        return -1
    value = compute(input_array[i], input_array[input_array[i + 1]], input_array[input_array[i + 2]])
    input_array[input_array[i + 3]] = value
    return (i + 4)

def part_1():
    input_array=[int(n) for n in _input.split(",")]
    input_array[1] = 12
    input_array[2] = 2
    i = 0
    while i < len(input_array):
        if input_array[i] == 99:
            break
        i = parse_four(input_array, i)
    print("Result: " + str(input_array[0]))

def _part_2(input_array, noun, verb):
    input_array[1] = noun
    input_array[2] = verb
    i = 0
    while i < len(input_array):
        i = parse_four(input_array, i)
        if i < 0:
            break

    if input_array[0] == 19690720:
        print("Result: " + str(input_array[0]))
        print("Params: ", (noun, verb))
        return

def part_2():
    input_array = [int(n) for n in _input.split(",")]
    for n in range(0, 100):
        for v in range(0, 100):
            tmp_array = input_array.copy()
            _part_2(tmp_array, n, v)

def main():
    part_1()
    part_2()

main()

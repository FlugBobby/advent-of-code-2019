#!/usr/bin/python3

import sys

input_day_2="1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,6,23,2,6,23,27,2,27,9,31,1,5,31,35,1,35,10,39,2,39,9,43,1,5,43,47,2,47,10,51,1,51,6,55,1,5,55,59,2,6,59,63,2,63,6,67,1,5,67,71,1,71,9,75,2,75,10,79,1,79,5,83,1,10,83,87,1,5,87,91,2,13,91,95,1,95,10,99,2,99,13,103,1,103,5,107,1,107,13,111,2,111,9,115,1,6,115,119,2,119,6,123,1,123,6,127,1,127,9,131,1,6,131,135,1,135,2,139,1,139,10,0,99,2,0,14,0"
input_test_day_2="1,9,10,3,2,3,11,0,99,30,40,50"

_input="3,225,1,225,6,6,1100,1,238,225,104,0,1101,61,45,225,102,94,66,224,101,-3854,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,31,30,225,1102,39,44,224,1001,224,-1716,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,92,41,225,101,90,40,224,1001,224,-120,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1101,51,78,224,101,-129,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1,170,13,224,101,-140,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,14,58,225,1102,58,29,225,1102,68,70,225,1002,217,87,224,101,-783,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,19,79,225,1001,135,42,224,1001,224,-56,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,2,139,144,224,1001,224,-4060,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,9,51,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,102,2,223,223,1006,224,329,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,434,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,464,101,1,223,223,1108,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,7,677,677,224,1002,223,2,223,1006,224,494,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,509,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,524,101,1,223,223,8,226,677,224,1002,223,2,223,1005,224,539,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,599,101,1,223,223,1007,226,677,224,102,2,223,223,1006,224,614,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,629,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,644,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,107,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226"
input_test_1 = "3,0,4,0,99"
input_test_2 = "1002,4,3,4,33"

param = 1
halt = False

###############
# Operations Utils
##############

def get_value_mode(input_array, modes, args, args_index):
    modes = modes.rjust(len(args), '0')[::-1]
    mode = int(modes[args_index])

    if (mode == 1):
#        print ("IMMEDIATE")
        return (int(args[args_index]))
    else:
#        print ("POSITION")
#        print (args_index, args)
        return (input_array[args[args_index]])

def store_result(input_array, modes, args, value_index, current_position, op_result):
    modes = modes.rjust(len(args), '0')[::-1]
    mode = int(modes[value_index])

    if (mode == 1):
#        print ("IMMEDIATE")
        input_array[current_position + value_index] = op_result
#        print("Writing to ", current_position + value_index, op_result)
        return (0)
    else:
#        print ("POSITION")
        input_array[args[value_index]] = op_result
#        print("Writing to ", args[value_index], op_result)
        return (0)

###############
# Operations
##############

def add(input_array, modes, args, current_position):
    result = get_value_mode(input_array, modes, args, 0) + get_value_mode(input_array, modes, args, 1)
    store_result(input_array, modes, args, 2, current_position, result)

def mul(input_array, modes, args, current_position):
    result = get_value_mode(input_array, modes, args, 0) * get_value_mode(input_array, modes, args, 1)
    store_result(input_array, modes, args, 2, current_position, result)

def store_input(input_array, modes, args, current_position):
    store_result(input_array, modes, args, 0, current_position, param)

def output(input_array, modes, args, current_position):
    print("OUTPUT: ", get_value_mode(input_array, modes, args, 0))

def stop(input_array, modes, args, current_position):
    global halt
    halt = True

operations= {
    "99": (stop, 0),
    "1":  (add, 3),
    "2":  (mul, 3),
    "3":  (store_input, 1),
    "4":  (output, 1)
}

##############
# Computing
##############

def treat_opcode(input_array, i):

    instruction = input_array[i]
    opcode = str(instruction % 100)

    args_nbr = operations[opcode][1] + 1
    args = input_array[i + 1:i + args_nbr]

    modes = (str(instruction)[0:len(str(instruction)) - 2])

    print("instruction", instruction)

    operations[opcode][0](input_array, modes, args, i)
    return (i + args_nbr)

def run_machine(_input, noun):
    input_array = [int(n) for n in _input.split(",")]

    timeout = 200
    t = 0
    i = 0

    while (halt == False and t < timeout):
        t += 1
        i = treat_opcode(input_array, i)
#        print(input_array)
#        print("---")
    return ()

#########
# Main
#########

def main():
    run_machine(_input, 1)

main()

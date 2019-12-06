#!/usr/bin/python3


def valid_number(nbr):
    consecutive_digits = 0
    for i in range(1,  len(nbr)):
        if nbr[i] == nbr[i - 1]:
            consecutive_digits += 1
    if consecutive_digits == 0:
        return (False)
    print("consecutive_digits", consecutive_digits)
    if consecutive_digits == 0:
        return (False)
    for i in range(1,  len(nbr)):
        if nbr[i] < nbr[i - 1]:
            print(str(nbr[i]) + " is lower than " + str(nbr[i - 1]))
            return (False)
            consecutive_digits += 1
    return True

def check_next(current, input_max):
    if valid_number(current):
        return 
    return True

def iterate_number(nbr):

    if ()
# [a


def part_1(_input):
    print (_input)
    answer = 0
    input_array = []
    current = [int(x) for x in _input.split('-')[0]]
    input_max = [int(x) for x in _input.split('-')[1]]
    finished = False

    while finished == False:
        finished = check_next(current, input_max)
#        current = iterate_number(current)
#        if current == input_max:
#            break
        answer += 1
    # print( input_min, input_max)
    # print(_input_min)
    print (answer - 1)

def main():
    _input = "171309-643603"
    _input_test_1 = "112145-120000"
    part_1(_input_test_1)
    print("Here we go!")

main()

#!/usr/bin/python3

def valid_number_2(nbr, input_max):
    consecutive_digits = 1
    current_group = nbr[0]
    valid_groups = 0
    for i in range(1,  len(nbr)):
        if nbr[i] == nbr[i - 1]:
            if (nbr[i] == current_group):
                consecutive_digits += 1
            elif consecutive_digits == 2:
                valid_groups += 1
                current_group = nbr[i]
                consecutive_digits = 1
            else:
                current_group = nbr[i]
                consecutive_digits = 2
        elif consecutive_digits == 2 :
            valid_groups += 1
            current_group = nbr[i]
            consecutive_digits = 1
        else:
            consecutive_digits = 1
    if consecutive_digits == 2:
        valid_groups += 1
    if valid_groups == 0:
        return (False)
    for i in range(1,  len(nbr)):
        if nbr[i] < nbr[i - 1]:
            return (False)
            consecutive_digits += 1
    return True

def valid_number_1(nbr, input_max):
    consecutive_digits = 0
    for i in range(1,  len(nbr)):
        if nbr[i] == nbr[i - 1]:
            consecutive_digits += 1
    if consecutive_digits == 0:
        return (False)
    if consecutive_digits == 0:
        return (False)
    for i in range(1,  len(nbr)):
        if nbr[i] < nbr[i - 1]:
            return (False)
            consecutive_digits += 1
    return True

def get_highest_next(nbr):
    highest = nbr[0]
    for i in range(1,  len(nbr)):
        if nbr[i] < highest:
            for j in range(i,  len(nbr)):
                nbr[j] = highest
            return (nbr)
        else:
            highest = nbr[i]
    return nbr

def iterate_number(nbr):
    for i in reversed(range(0, len(nbr))):
        if nbr[i] == 9:
            if nbr[i - 1] == 9:
                continue
            nbr[i - 1] += 1
            for j in range(i, len(nbr)):
                nbr[j] = nbr[i - 1]
            return (nbr)
        else:
            nbr[i] += 1
            return (nbr)
    return (nbr)

def get_int(n):
    m = [1, 10, 100, 1000, 10000, 100000]
    _sum = 0
    for i in range(0, len(n)):
        _sum += (n[i] * m[len(n) - i - 1])
    return (_sum)

def compare(n1, n2):
    for i in range(0, len(n1)):
        if (n1[i] != n1[2]):
            return (False)
    return (True)

def loop(_input, validate_func):
    print (_input)
    answer = 0
    input_array = []
    current = [int(x) for x in _input.split('-')[0]]
    input_max = [int(x) for x in _input.split('-')[1]]
    finished = False

    current = get_highest_next(current)
    while finished == False:
        if get_int(current) > get_int(input_max):
            break
        if validate_func(current, input_max) == True:
            answer += 1
        current = iterate_number(current)
    print ("Answer", answer)

def part_1(_input):
    loop(_input, valid_number_1)

def part_2(_input):
    loop(_input, valid_number_2)

def main():
    print("Here we go!")
    _input = "171309-643603"
    _input_test_1 = "112145-120000"
    _input_test_2 = "119149-140000"
    part_1(_input)
    part_2(_input)

main()

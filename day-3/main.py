#!/usr/bin/python3

import numpy
from numpy import zeros

distance = 100000
starting_point = (0,0)

def set_value(res_array, x, y, wire_id):
    if res_array[x][y] == wire_id:
        return
    if res_array[x][y] == 0:
        res_array[x][y] = wire_id
    else:
        res_array[x][y] = 8
        global starting_point
        global distance
        d = calculate_distance(starting_point,(x,y))
        if d < distance:
            distance = d

def write_path(res_array, coord, direction, value, wire_id):
    if direction == "R":
#        print(coord)
        x = coord[0]
        while (x < coord[0] + value):
            x += 1
            set_value(res_array, x, coord[1], wire_id)
        return (x, coord[1])
    if direction == "L":
#        print(coord)
        x = coord[0]
        while (x > coord[0] - value):
            x -= 1
            set_value(res_array, x, coord[1], wire_id)
        return (x, coord[1])
    if direction == "U":
#        print(coord)
        y = coord[1]
        while (y > coord[1] - value):
            y -= 1
            set_value(res_array, coord[0], y, wire_id)
        return (coord[0], y)
    if direction == "D":
#        print(coord)
        y = coord[1]
        while (y < coord[1] + value):
            y += 1
            set_value(res_array, coord[0], y, wire_id)
        return (coord[0], y)
    return coord

def calculate_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def parse_wire(res_array, wire, coord, wire_id):
    new_coord = coord
    for c in wire.split(','):
        new_coord = write_path(res_array, new_coord, c[:1], int(c[1:]), wire_id)
#        print("C", c)
#        print("new coord", new_coord)
#        print(starting_point)

def part1(_input, max_size):
    coord = (max_size, max_size)

    global starting_point
    starting_point = (max_size, max_size)
    global closest_intersection
    closest_intersection = 100000

    res_array = numpy.zeros([max_size * 2, max_size * 2])
    wire_id = 1
    res_array[max_size][max_size] = 9
    with open(_input) as input_file:
        for wire in input_file:
            parse_wire(res_array, wire, coord, wire_id)
            wire_id += 1
#    print(res_array)
    print (distance)

def main():
    part1("input.txt", 10000)

main()

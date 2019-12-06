#!/usr/bin/python3

import numpy
from numpy import zeros

closest_intersection = 100000
distances = [0, 0]
starting_point = (0,0)
#intersection = (0,0)
reached_intersection = [False, False]
intersections = []
current_intersection = (0, 0)

def increase_distance(res_array, x, y, wire_id):
    global distances
    global reached_intersection
    global current_intersection
    if res_array[x][y] == 8 and current_intersection[0] == x and current_intersection[1] == y:
        distances[wire_id - 1] += 1
        reached_intersection[wire_id - 1] = True
    else:
        if reached_intersection[wire_id - 1] == False:
            distances[wire_id - 1] += 1

def set_value(res_array, x, y, wire_id):
    if res_array[x][y] == wire_id:
        return
    if res_array[x][y] == 0:
        res_array[x][y] = wire_id
    else:
        global starting_point
        global closest_intersection
        global intersections
        res_array[x][y] = 8
        intersections.append((x,y))
        d = manhattan_distance(starting_point,(x,y))
        if d < closest_intersection:
            closest_intersection = d

def write_path(res_array, coord, direction, value, wire_id, write=True):
    if direction == "R":
        x = coord[0]
        while (x < coord[0] + value):
            x += 1
            if write:
                set_value(res_array, x, coord[1], wire_id)
            else:
                increase_distance(res_array, x, coord[1], wire_id)
        return (x, coord[1])
    if direction == "L":
        x = coord[0]
        while (x > coord[0] - value):
            x -= 1
            if write:
                set_value(res_array, x, coord[1], wire_id)
            else:
                increase_distance(res_array, x, coord[1], wire_id)
        return (x, coord[1])
    if direction == "U":
        y = coord[1]
        while (y > coord[1] - value):
            y -= 1
            if write:
                set_value(res_array, coord[0], y, wire_id)
            else:
                increase_distance(res_array, coord[0], y, wire_id)
        return (coord[0], y)
    if direction == "D":
        y = coord[1]
        while (y < coord[1] + value):
            y += 1
            if write:
                set_value(res_array, coord[0], y, wire_id)
            else:
                increase_distance(res_array, coord[0], y, wire_id)
        return (coord[0], y)
    return coord

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def parse_wire(res_array, wire, coord, wire_id):
    new_coord = coord
    for c in wire.split(','):
        new_coord = write_path(res_array, new_coord, c[:1], int(c[1:]), wire_id)

def calculate_distance(res_array, wire, coord, wire_id):
    global distances
    global reached_intersection

    new_coord = coord
    for c in wire.split(','):
        new_coord = write_path(res_array, new_coord, c[:1], int(c[1:]), wire_id, False)
        if reached_intersection[wire_id - 1] == True:
            break

def part2(_input, max_size):
    global starting_point
    starting_point = (max_size, max_size)
    global closest_intersection
    closest_intersection = 100000
    global intersections
    global reached_intersection
    global distances
    global current_intersection
    coord = (max_size, max_size)
    res_array = numpy.zeros([max_size * 2, max_size * 2])
    wire_id = 1
    res_array[max_size][max_size] = 9

    with open(_input) as input_file:
        for wire in input_file:
            parse_wire(res_array, wire, coord, wire_id)
            wire_id += 1

    answer = 120000
    for i in intersections:
        reached_intersection = [False, False]
        wire_id = 1
        distances = [0, 0]
        current_intersection = i
        with open(_input) as input_file:
           for wire in input_file:
               calculate_distance(res_array, wire, coord, wire_id)
               wire_id += 1
        if (distances[0] + distances[1]) < answer:
            answer = (distances[0] + distances[1])
    print(answer)

def main():
    part2("input.txt", 10000)

main()

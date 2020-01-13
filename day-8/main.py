#!/usr/bin/python3

import sys
import numpy

class Layer:
    def __init__(self, _input, width, height, offset):
        self.width = width
        self.height = height
        self.layer = []
        self.__init_layer__(_input, offset)

    def __init_layer__(self, _input, offset):
        self.layer = numpy.zeros([self.height, self.width])
        for line in range(0, self.height):
            for column in range(0, self.width):
                self.layer[line, column] = _input[offset + (line * self.width) + column]

    def __str__(self):
        return str(self.layer)

    def get_point(self, x, y):
        return (self.layer[x, y])

    def count_value(self, value):
        return ((self.layer == value).sum())


class Image:
    def __init__(self, input_file, width, height):
        self.width = width
        self.height = height
        self.input = []
        self.__init_input__(input_file)
        self.layers = []
        self.__init_layers__(input_file)

    def __init_layers__(self, input_file):
        i = 0
        while i < len(self.input):
            self.layers.append(Layer(self.input,
                                     self.width, self.height, i))
            i += (self.height * self.width)

    def __init_input__(self, input_file):
        f = open(input_file)
        for line in f:
            self.input.extend(map(int, line.rstrip()))
        f.close()

    def print_layers(self):
        i = 0
        for l in self.layers:
            i += 1
            print("Layer " + str(i))
            print(l)

    def find_layer_by_min_value(self, value):
        min_value = 100
        for l in self.layers:
            count = l.count_value(value)
            if count <= min_value:
                min_value = count
                save_layer = l
        return (save_layer)

    def get_pixel(self, x, y):
        for layer in self.layers:
             point = layer.get_point(x, y)
             if point != 2:
                return (point)
        return (0)

    def calculate_image_layers(self):
        image = []
        for line in range(0, self.height):
            for column in range(0, self.width):
                point = int(self.get_pixel(line, column))
                if point == 0:
                    point = ' '
                if point == 1:
                    point = '+'
                image.append(str(point))
        i = 0
        while i < len(image):
            print(''.join(image[i:i + self.width]))
            i += self.width

    def solve_part_1(self, layer, v1, v2):
        return (layer.count_value(v1) * layer.count_value(v2))


def main():
    image = Image(sys.argv[1], 25, 6)
    layer = image.find_layer_by_min_value(0)
    print("ANSWER: ", image.solve_part_1(layer, 1, 2))
    image.calculate_image_layers()

main()

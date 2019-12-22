#!/usr/bin/python3

class Machine:

### Public methods
    def __init__(self, _input):
        self.memory = [int(n) for n in _input.split(",")]
        self.index = 0
        self.operations = {
            "99": (self._stop, 0),
            "1":  (self._add, 3),
            "2":  (self._mul, 3),
            "3":  (self._store_param, 1),
            "4":  (self._output, 1),
            "5":  (self._jump_if_true, 2),
            "6":  (self._jump_if_false, 2),
            "7":  (self._less_than, 3),
            "8":  (self._equals, 3)
        }

    def run(self, param):
        self.param = param
        self.halt = False

        while (self.halt == False):
            self.index = self._treat_opcode()

### Private methods
    def _treat_opcode(self):
        instruction = self.memory[self.index]
        opcode =  str(int(instruction) % 100)
        args_nbr = self.operations[opcode][1] + 1
        args = self.memory[self.index + 1:self.index + args_nbr]
        modes = (str(instruction)[0:len(str(instruction)) - 2])

        print("[", self.index, "] instruction", instruction)
        return (self.operations[opcode][0](modes, args))


    def _get_value(self, modes, args, args_index):
        modes = modes.rjust(len(args), '0')[::-1]
        mode = int(modes[args_index])

        if (mode == 1):
            return (int(args[args_index]))
        else:
            return (int(self.memory[args[args_index]]))


    def _set_value(self, modes, args, args_index, value):
        modes = modes.rjust(len(args), '0')[::-1]
        mode = int(modes[args_index])

        if (mode == 1):
            self.memory[self.position + args_index] = value
        else:
            self.memory[args[args_index]] = value


### Operations
    def _stop(self, modes, args):
        self.halt = True
        return (self.index + self.operations["99"][1] + 1)

    def _add(self, modes, args):
        result = self._get_value(modes, args, 0) + self._get_value(modes, args, 1)
        self._set_value(modes, args, 2, result)
        return (self.index + self.operations["1"][1] + 1)

    def _mul(self, modes, args):
        result = self._get_value(modes, args, 0) * self._get_value(modes, args, 1)
        self._set_value(modes, args, 2, result)
        return (self.index + self.operations["2"][1] + 1)

    def _store_param(self, modes, args):
        self._set_value(modes, args, 0, self.param)
        return (self.index + self.operations["3"][1] + 1)

    def _output(self, modes, args):
        print("OUTPUT: ", self._get_value(modes, args, 0))
        return (self.index + self.operations["4"][1] + 1)

    def _jump_if_true(self, modes, args):
        if (self._get_value(modes, args, 0) != 0):
            return (self._get_value(modes, args, 1))
        return (self.index + self.operations["5"][1] + 1)

    def _jump_if_false(self, modes, args):
        if (self._get_value(modes, args, 0) == 0):
            return (self._get_value(modes, args, 1))
        return (self.index + self.operations["6"][1] + 1)

    def _less_than(self, modes, args):
        if (self._get_value(modes, args, 0) < self._get_value(modes, args, 1)):
            self._set_value(modes, args, 2, 1)
        else:
            self._set_value(modes, args, 2, 0)
        return (self.index + self.operations["7"][1] + 1)

    def _equals(self, modes, args):
        if (self._get_value(modes, args, 0) == self._get_value(modes, args, 1)):
            self._set_value(modes, args, 2, 1)
        else:
            self._set_value(modes, args, 2, 0)
        return (self.index + self.operations["8"][1] + 1)

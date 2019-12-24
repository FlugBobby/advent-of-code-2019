#!/usr/bin/python3

from machine import Machine

class Amplification:

    def __init__(self, program, phases):
        self.phases = phases
        self.program = program


    def run_once(self):
        output = 0

        for phase in self.phases:
            m = Machine(self.program)
            m.add_input(phase)
            m.add_input(output)
            output = m.run()[0]
        return (output)


    def run_feedback(self):
        amplifiers = []
        output = 0
        halted = 0

        for p in self.phases:
            m = Machine(self.program, "INFO")
            m.add_input(p)
            amplifiers.append(m)
        while halted < len(self.phases):
            for m in amplifiers:
                m.add_input(output)
                output = m.run()[0]
                halt = m.get_halt()
                if halt == True:
                    halted += 1
        return (output)

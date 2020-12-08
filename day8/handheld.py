# -*- coding:utf-8 -*-

import os


def read_input():
    with open(os.path.join('day8','input'), 'r') as f:
        lines = f.read().splitlines()
        return [line.split(' ') for line in lines]

instructions = read_input()


class Handheld:
    def __init__(self):
        self.acc_register = 0 # Accumulator
        self.pc_register = 0 # Program counter
        self._op_builder = {'nop': self._nop, 'acc': self._acc, 'jmp': self._jmp}

    def _nop(self, arg):
        self.pc_register += 1

    def _acc(self, arg):
        self.acc_register += arg
        self.pc_register += 1

    def _jmp(self, arg):
        self.pc_register += arg

    def exec(self, opcode, arg):
        self._op_builder[opcode](arg)
        

# Part 1
print('Part 1')
checker = [False] * len(instructions)
handheld = Handheld()
while True:    
    if checker[handheld.pc_register]:
        break
    checker[handheld.pc_register] = True
    next_instruction = instructions[handheld.pc_register]
    handheld.exec(next_instruction[0], (int(next_instruction[1])))

print(f'\tSolution Found {handheld.acc_register}')

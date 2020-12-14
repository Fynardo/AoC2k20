# -*- coding:utf-8 -*-

import os
import re


def read_input():
    with open(os.path.join('day14','input'), 'r') as f:
        return f.read().splitlines()


program = read_input()

# Part 1
def apply_mask(mask, value):
    bin_value = bin(int(value))[2:]
    expanded_bin = ''.join(['0'] * (36 - len(bin_value))) + bin_value
    new_value = ''
    for i, m in enumerate(mask):
        new_value += m if (m == '0' or m == '1') else expanded_bin[i]
    return int('0b'+new_value, 2)


print('Part 1')
mask = None
memory = {}
for op in program:
    if op.startswith('mask'):
        mask = op.split(' = ')[1]
    elif op.startswith('mem'):
        p = re.match('^mem\[(\d+)\] = (\d+)$', op)
        memory[p.group(1)] = apply_mask(mask, p.group(2))

print(f'\tSolution Found: {sum(list(memory.values()))}')
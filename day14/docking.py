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
    modified_value = ''.join([m if (m == '0' or m == '1') else expanded_bin[i] for i, m in enumerate(mask)])
    return int('0b'+modified_value, 2)


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


# Part 2
def land_floating_mask(v):
    if v.count('X') == 0:
        return v
    else:      
        return land_floating_mask(v.replace('X', '0', 1)) + ' ' + land_floating_mask(v.replace('X' ,'1', 1))

def apply_floating_mask(mask, value):
    bin_value = bin(int(value))[2:]
    expanded_bin = ''.join(['0'] * (36 - len(bin_value))) + bin_value
    modified_value = ''.join([m if (m == '1' or m == 'X') else expanded_bin[i] for i, m in enumerate(mask)])
    concrete_locations = land_floating_mask(modified_value).split()
    return [int(c, 2) for c in concrete_locations]


print('Part 2')
mask = None
memory = {}
for op in program:
    if op.startswith('mask'):
        mask = op.split(' = ')[1]
    elif op.startswith('mem'):
        p = re.match('^mem\[(\d+)\] = (\d+)$', op)        
        memory_list = apply_floating_mask(mask, p.group(1))
        for mem_dir in memory_list:
            memory[mem_dir] = int(p.group(2))

print(f'\tSolution Found: {sum(list(memory.values()))}')
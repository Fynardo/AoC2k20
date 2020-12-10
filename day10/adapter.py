# -*- coding:utf-8 -*-

import os

def read_input():
    with open(os.path.join('day10','input'), 'r') as f:
        return [int(line) for line in f.read().splitlines()]


adapters = read_input()


# Part 1
wall_plug = 0
my_device = max(adapters) + 3
adapters_end_to_end = [wall_plug] + adapters + [my_device]

print('Part 1')
jolts_diff = [y-x for x,y in zip(sorted(adapters_end_to_end)[:-1], sorted(adapters_end_to_end)[1:])]
print(f'\tSolution Found: Diff3 ({jolts_diff.count(3)}) * Diff1({jolts_diff.count(1)}) = {jolts_diff.count(3)*jolts_diff.count(1)}')


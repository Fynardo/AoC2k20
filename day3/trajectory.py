# -*- coding:utf-8 -*-
import os
import math
import functools

# Setup
def read_input():
    with open(os.path.join('day3', 'input'), 'r') as f:
        return f.read().splitlines()


area = read_input()


# Common
rows = len(area)
cols = len(area[0])

def find_trees_in_slope(offset_x, offset_y):
    jumps_down = [(i * offset_y) for i in range(1, math.ceil(rows/offset_y))]
    jumps_right = [(i * offset_x) % cols for i in range(1, rows)]
    return list(filter(lambda x: area[x[0]][x[1]] == '#', zip(jumps_down, jumps_right)))
    


# Part 1
print('Part 1')
offset_x = 3
offset_y = 1
trees = find_trees_in_slope(offset_x, offset_y)
print(f'\tFound solution {len(trees)}')


# Part 2
print('Part 2')
offset_x = [1, 3, 5, 7, 1]
offset_y = [1, 1, 1, 1, 2]
trees = [len(find_trees_in_slope(x, y)) for x, y in zip(offset_x ,offset_y)]
print(f'\tFound solution {functools.reduce(lambda a,b: a*b, trees)}')
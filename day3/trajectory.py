# -*- coding:utf-8 -*-
import os


# Setup
def read_input():
    with open(os.path.join('day3', 'input'), 'r') as f:
        return f.read().splitlines()


area = read_input()


# Part 1
print('Part 1')
offset_x = 3
offset_y = 1

rows = len(area)
cols = len(area[0])

jumps_down = list(range(1, rows))
jumps_right = [(i * offset_x) % cols for i in range(1, rows)]

trees = list(filter(lambda x: area[x[0]][x[1]] == '#', zip(jumps_down, jumps_right)))
print(f'\tFound solution {len(trees)}')
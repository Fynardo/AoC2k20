# -*- coding:utf-8 -*-
import os


def read_input():
    with open(os.path.join('day1', 'input'), 'r') as f:
        return [int(r) for r in f.readlines()]

# Setup
lines = read_input()
wanted = 2020


# Part 1
print('Part 1:')
for i, x in enumerate(lines):
    for j in range(i, len(lines)):
        y = lines[j]
        if x + y == wanted:
            print(f'\t solution found: {x*y}')


# Part 2
print('Part 2:')
for i, x in enumerate(lines):
    for j in range(i, len(lines)):
        y = lines[j]
        diff = wanted - x - y
        try:
            z = lines[lines.index(diff)]
            print(f'\t solution found: {x*y*z}')
        except ValueError:
            continue


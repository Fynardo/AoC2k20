# -*- coding:utf-8 -*-
import os


def read_input():
    with open(os.path.join('day1', 'input'), 'r') as f:
        return [int(r) for r in f.readlines()]

# Setup
lines = read_input()


# Part 1
for i, x in enumerate(lines):
    for j in range(i, len(lines)):
        y = lines[j]
        if x + y == 2020:
            print(x*y)



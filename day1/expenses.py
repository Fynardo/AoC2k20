# -*- coding:utf-8 -*-
import os


def read_input():
    with open(os.path.join('day1', 'input'), 'r') as f:
        return [int(r) for r in f.readlines()]

# Setup
lines = read_input()
wanted = 2020


# Part 1
for i, x in enumerate(lines):
    for j in range(i, len(lines)):
        y = lines[j]
        if x + y == wanted:
            print(x*y)


# Part 2
cache = {}
for i, x in enumerate(lines):
    for j in range(i, len(lines)):
        y = lines[j]
        diff = wanted - x - y
        try:
            last = lines[lines.index(diff)]
            print(x*y*last)
        except ValueError:
            continue


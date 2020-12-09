# -*- coding:utf-8 -*-

import os


def read_input():
    with open(os.path.join('day9', 'input'), 'r') as f:
        return [int(line) for line in f.read().splitlines()]


xmas = read_input()

# Part 1
print('Part 1')
preamble_length = 25
offset = 0

preamble = xmas[offset: offset + preamble_length]
hash = [{x+y for y in preamble if x!=y} for x in preamble]
flatten_hash = set.union(*hash)
next_number = xmas[offset+preamble_length]

while next_number in flatten_hash:
    # print(preamble, next_number, hash)
    preamble[offset % preamble_length] = next_number
    hash[offset % preamble_length] = {next_number + x for x in preamble}
    flatten_hash = set.union(*hash)
    offset += 1
    next_number = xmas[offset+preamble_length]
print(f'\tSolution Found: {next_number}')

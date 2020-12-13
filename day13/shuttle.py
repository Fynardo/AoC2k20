# -*- coding:utf-8 -*-

import os


def read_input():
    with open(os.path.join('day13','input'), 'r') as f:
        estimate, busses = f.read().split('\n')
        estimate = int(estimate)
        busses = [int(b) for b in busses.split(',') if b != 'x']
        return estimate, busses


estimate, busses = read_input()

# Part 1
print('Part 1')
wait_times = [(bus - estimate % bus, bus) for bus in busses]
min_time = min(wait_times)
print(f'\tSolution Found: {min_time[0] * min_time[1]}')


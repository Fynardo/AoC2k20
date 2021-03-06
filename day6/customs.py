# -*- coding:utf-8 -*-

import os

def read_input():
    with open(os.path.join('day6','input'), 'r') as f:
        groups = f.read().split('\n\n')
        return groups

groups = read_input()


# Part 1
print('Part 1')
answers = [len(set(g.replace('\n',''))) for g in groups]
print(f'\tSolution Found: {sum(answers)}')


# Part 2
print('Part 2')
answers = [[set(passenger) for passenger in g.split('\n')] for g in groups]
common_answers = [len(a[0].intersection(*a[1:])) for a in answers]
print(f'\tSolution Found: {sum(common_answers)}')

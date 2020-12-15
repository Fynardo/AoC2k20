# -*- coding:utf-8 -*-


# Common
initial_numbers = [8,11,0,19,1,2]


def find_n_number(spoken, iters):
    for i in range(len(initial_numbers)-1, iters):
        if spoken not in cache:
            cache[spoken] = (i,-1)
            spoken = 0
        else:
            cache[spoken] = (i, cache[spoken][0])
            spoken = cache[spoken][0] - cache[spoken][1]
    return spoken


# Part 1
print('Part 1')
p1_iters = 2019
spoken = initial_numbers[-1]
cache = {n:(i,-1) for i,n in enumerate(initial_numbers[:-1])}
print(f'\tSolution Found:{find_n_number(spoken, p1_iters)}')

# Part 2
print('Part 2')
p2_iters = 29999999
spoken = initial_numbers[-1]
cache = {n:(i,-1) for i,n in enumerate(initial_numbers[:-1])}
print(f'\tSolution Found:{find_n_number(spoken, p2_iters)}')

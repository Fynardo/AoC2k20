# -*- coding:utf-8 -*-


initial_numbers = [8,11,0,19,1,2]


# Part 1
max_iters = 2019
spoken = initial_numbers[-1]
cache = {n:(i,-1) for i,n in enumerate(initial_numbers[:-1])}

print('Part 1')
for i in range(len(initial_numbers)-1,max_iters):
    if spoken not in cache:
        cache[spoken] = (i,-1)
        spoken = 0
    else:
        cache[spoken] = (i, cache[spoken][0])
        spoken = cache[spoken][0] - cache[spoken][1]


print(f'\tSolution Found:{spoken}')

# -*- coding:utf-8 -*-

import os

def read_input():
    with open(os.path.join('day11','input'), 'r') as f:
        return f.read().splitlines()

seats = read_input()


# Common
rows = len(seats)
cols = len(seats[0])

flat_seats = ''.join(seats)


# Part 1
def get_surroundings(seats, i):
    retval = []
    # clockwise
    retval.append(seats[i-cols] if i//cols > 0 else '.')
    retval.append(seats[i-cols+1] if (i % cols < cols - 1 and i // cols > 0) else '.')
    retval.append(seats[i+1] if i % cols < cols -1 else '.')
    retval.append(seats[i+cols+1] if (i % cols < cols - 1 and i // cols < rows - 1) else '.')
    retval.append(seats[i+cols] if i//cols < rows - 1 else '.')
    retval.append(seats[i+cols-1] if (i % cols > 0 and i // cols < rows - 1) else '.')
    retval.append(seats[i-1] if i % cols > 0 else '.')
    retval.append(seats[i-cols-1] if (i % cols > 0 and i // cols > 0) else '.')
    return retval


def check_empty(seats, i):
    surroundings = get_surroundings(seats, i)
    return all(list(map(lambda x: x == '.' or x =='L', surroundings)))


def check_occupied(seats, i):
    surroundings = get_surroundings(seats, i)
    return len(list(filter(lambda x: x == '#', surroundings))) >= 4


def simulate(seats):
    new_seats = []
    for i,s in enumerate(seats):
        if s == 'L':
            new_seats.append('#' if (check_empty(seats, i)) else 'L')            
        elif s == '#':
            new_seats.append('L' if (check_occupied(seats, i)) else '#')
        elif s == '.':
            new_seats.append('.')
    return ''.join(new_seats)


print('Part 1')
cur_seats = '' 
new_seats = flat_seats
while new_seats != cur_seats:
    cur_seats = new_seats
    new_seats = simulate(cur_seats)

print(f'\tSolution Found: {new_seats.count("#")}')


# Part 2
def get_fov(seats, i):
    retval = []
    # clockwise
    # North
    offset_y = 1
    while i//cols - offset_y >= 0 and seats[i - cols*offset_y] == '.':
        offset_y+=1
    retval.append('.' if i//cols - offset_y < 0 else seats[i - cols*offset_y])
    # North-East
    offset_x = 1
    offset_y = 1
    while i//cols - offset_y >= 0 and (i % cols) + offset_x < cols and seats[i - cols * offset_y + offset_x] == '.':
        offset_x += 1
        offset_y += 1
    retval.append('.' if i//cols - offset_y < 0 or (i % cols) + offset_x >= cols else seats[i - cols*offset_y + offset_x])
    # East
    offset_x = 1
    while (i % cols) + offset_x < cols and seats[i + offset_x] == '.':
        offset_x += 1
    retval.append('.' if (i % cols) + offset_x >= cols else seats[i + offset_x])
    # South-East
    offset_x = 1
    offset_y = 1
    while i//cols + offset_y < rows and (i % cols) + offset_x < cols and seats[i + cols * offset_y + offset_x] == '.':
        offset_x += 1
        offset_y += 1
    retval.append('.' if i//cols + offset_y >= rows or (i % cols) + offset_x >= cols else seats[i + cols*offset_y + offset_x])
    # South
    offset_y = 1
    while i//cols + offset_y < rows and seats[i + cols*offset_y] == '.':
        offset_y+=1
    retval.append('.' if i//cols + offset_y >= rows else seats[i + cols*offset_y])
    # South-West
    offset_x = 1
    offset_y = 1
    while i//cols + offset_y < rows and (i % cols) + offset_x >= 0 and seats[i + cols * offset_y - offset_x] == '.':
        offset_x += 1
        offset_y += 1
    retval.append('.' if i//cols + offset_y >= rows or (i % cols) - offset_x < 0 else seats[i + cols*offset_y - offset_x])
    # West
    offset_x = 1
    while (i % cols) - offset_x >= 0 and seats[i - offset_x] == '.':
        offset_x += 1
    retval.append('.' if (i % cols) - offset_x < 0 else seats[i - offset_x])
    # North-West
    offset_x = 1
    offset_y = 1
    while i//cols - offset_y >= 0 and (i % cols) - offset_x >= 0 and seats[i - cols * offset_y - offset_x] == '.':
        offset_x += 1
        offset_y += 1
    retval.append('.' if i//cols - offset_y < 0 or (i % cols) - offset_x < 0 else seats[i - cols*offset_y -offset_x])

    return retval


def check_empty_fov(seats, i):
    surroundings = get_fov(seats, i)
    return all(list(map(lambda x: x == '.' or x =='L', surroundings)))


def check_occupied_fov(seats, i):
    surroundings = get_fov(seats, i)
    return len(list(filter(lambda x: x == '#', surroundings))) >= 5


def simulate_fov(seats):
    new_seats = []
    for i,s in enumerate(seats):
        if s == 'L':
            new_seats.append('#' if (check_empty_fov(seats, i)) else 'L')            
        elif s == '#':
            new_seats.append('L' if (check_occupied_fov(seats, i)) else '#')
        elif s == '.':
            new_seats.append('.')
    return ''.join(new_seats)


print('Part 2')
cur_seats = '' 
new_seats = flat_seats
while new_seats != cur_seats:
    cur_seats = new_seats
    new_seats = simulate_fov(cur_seats)

print(f'\tSolution Found: {new_seats.count("#")}')

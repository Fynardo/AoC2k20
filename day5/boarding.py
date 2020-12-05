# -*- coding:utf-8 -*-
import os


def read_input():
    with open(os.path.join('day5','input'), 'r') as f:
        return f.read().splitlines()

passes = read_input()


# Part 1
def _aux(boarding_pass, a, b, l, u):
    letter = boarding_pass[0]
    if (b - a == 2):
        return (a if letter == l else b - 1)
    else:
        if letter == l:
            b = (a + b) // 2
        elif letter == u:
            a = (a + b) // 2
        return _aux(boarding_pass[1:], a, b, l, u)

def decode_row(boarding_pass):
    return _aux(boarding_pass, 0, 128, 'F', 'B')

def decode_col(boarding_pass):
    return _aux(boarding_pass, 0, 8, 'L', 'R')

def decode(boarding_pass):
    return decode_row(boarding_pass[:7]) * 8 + decode_col(boarding_pass[7:])

print('Part 1')
seat_ids = [decode(boarding_pass) for boarding_pass in passes] 
print(f'\tSolution Found: {max(seat_ids)}')

# Part 2
print('Part 2')
sorted_seats = sorted(seat_ids)
my_seat = [y-1 for x,y in list(zip(sorted_seats[:-1],sorted_seats[1:])) if y - x > 1][0]
print(f'\tSolution Found: {my_seat}')
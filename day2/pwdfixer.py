# -*- coding:utf-8 -*-
import os
from dataclasses import dataclass

# Setup
@dataclass
class Passwd:
    text: str
    letter: str
    lower: int
    upper: int


def read_input():
    passwords = []
    with open(os.path.join('day2', 'input'), 'r') as f:
        for line in f:
            policy, passwd = [x.strip() for x in line.split(':')]
            times, letter = policy.split(' ')
            lower, upper = [int(x) for x in times.split('-')]
            passwords.append(Passwd(passwd, letter, lower, upper))
    return passwords
            

# Part 1
print('Part 1:')
passwords = read_input()
valid = filter(lambda passwd: passwd.lower <= passwd.text.count(passwd.letter) <= passwd.upper, passwords)
print(f'\t Solution found: {len(list(valid))}')


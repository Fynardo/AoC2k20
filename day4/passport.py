# -*- coding:utf-8 -*-

import os


def read_input():
    with open(os.path.join('day4','input'), 'r') as f:
        passports = []
        new_passport = {}
        lines = f.read().splitlines()
        for line in lines:        
            if line == '':
                # next passport
                passports.append(new_passport)
                new_passport = {}                
            else:
                fields = line.split(' ')
                for field in fields:
                    k,v = field.split(':')
                    new_passport[k] = v
        passports.append(new_passport)
    return passports


passports = read_input()

# Part 1
print('Part 1:')
required_fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
valid_passports = list(filter(lambda x: required_fields.issubset(set(x.keys())), passports))
print(f'\t Found Solution: {len(valid_passports)}')
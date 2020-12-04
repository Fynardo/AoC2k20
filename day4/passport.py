# -*- coding:utf-8 -*-

import os
import re


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


# Part 1
passports = read_input()
print('Part 1:')
required_fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
valid_passports = list(filter(lambda x: required_fields.issubset(set(x.keys())), passports))
print(f'\t Found Solution: {len(valid_passports)}')


# Part 2
class Field:
    def __init__(self, value):
        self.value = value
    def validate(self):
        pass

class BYR(Field):
    def validate(self):
        return 1920 <= int(self.value) <= 2002

class IYR(Field):
    def validate(self):
        return 2010 <= int(self.value) <= 2020

class EYR(Field):
    def validate(self):
        return 2020 <= int(self.value) <= 2030

class HGT(Field):
    def _extract(self):
        return self.value[:-2], self.value[-2:]
    def validate(self):
        height, metric = self._extract()
        if metric == 'cm':
            return 150 <= int(height) <= 193
        elif metric == 'in':
            return 59 <= int(height) <= 76
        else:
            return False

class HCL(Field):
    def validate(self):
        hashtag, color = self.value[0], self.value[1:]
        return hashtag == '#' and re.compile('^[a-f0-9]{6}$').match(color)

class ECL(Field):
    def validate(self):
        return self.value in {'amb','blu','brn','gry','grn','hzl','oth'}

class PID(Field):
    def validate(self):
        return re.compile('^[0-9]{9}$').match(self.value)

class CID(Field):
    def validate(self):
        return True


field_builder = {'byr': BYR, 'iyr': IYR, 'eyr': EYR, 'hgt': HGT, 'hcl': HCL, 'ecl': ECL, 'pid': PID, 'cid': CID}


class Passport:
    def __init__(self, fields):
        self._fields = fields
        self._required_fields = {BYR, IYR, EYR, HGT, HCL, ECL, PID}
    
    def validate(self):
        return all([f.validate() for f in self._fields]) and self._required_fields.issubset(set([type(x) for x in self._fields]))


print('Part 2:')
dicts = read_input()
passports = [Passport([field_builder[k](v) for k, v in d.items()]) for d in dicts]
valid = [p.validate() for p in passports]
print(f'\tSolution Found: {sum(valid)}')



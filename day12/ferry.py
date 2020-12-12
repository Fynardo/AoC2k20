# -*- coding:utf-8 -*-

import os
import math


def read_input():
    with open(os.path.join('day12','input'), 'r') as f:
        return [(line[0],int(line[1:])) for line in f.read().splitlines()]

navigation = read_input()


class Ship:
    def __init__(self):
        self._lat = 0
        self._long = 0
        self._direction = 0
        self._actions = {'N': self.go_north, 'S': self.go_south, 'E': self.go_east, 'W': self.go_west, 'L': self.rotate_left, 'R': self.rotate_right, 'F': self.forward}
   
    @property
    def location(self):
        return (self._lat, self._long)

    def maneuver(self, action, value):
        self._actions[action](value)

    def rotate_left(self, degrees):
        self._direction += degrees % 360

    def rotate_right(self, degrees):
        self._direction -= degrees % 360

    def go_north(self, distance):
        self._lat += distance

    def go_south(self, distance):
        self._lat -= distance

    def go_east(self, distance):
        self._long += distance
    
    def go_west(self, distance):
        self._long -= distance

    def forward(self, value):
        _lat_despl = round(math.sin(math.radians(self._direction)), 2)
        _long_despl = round(math.cos(math.radians(self._direction)), 2)
        self._lat += _lat_despl*value
        self._long += _long_despl*value    



# Part 1
def manhattan(lat, long):
    return abs(lat) + abs(long)

print('Part 1')
ferry = Ship()
for (action, value) in navigation:
    ferry.maneuver(action, value)

print(f'\tSolution Found: {manhattan(*ferry.location)}')

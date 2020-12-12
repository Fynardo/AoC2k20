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


def manhattan(lat, long):
    return abs(lat) + abs(long)

# Part 1
print('Part 1')
ferry = Ship()
for (action, value) in navigation:
    ferry.maneuver(action, value)

print(f'\tSolution Found: {manhattan(*ferry.location)}')


# Part 2
class WaypointShip(Ship):
    def __init__(self):
        super().__init__()
        self._waypoint_lat = 1
        self._waypoint_long = 10
        self._quadrants = [(1,1),(1,-1),(-1,-1),(-1,1)]
        self._cur_quadrant = 0

    def _rotate(self, cuad_offset):
        if cuad_offset % 2 == 1:
            self._waypoint_lat, self._waypoint_long = self._waypoint_long, self._waypoint_lat
        self._waypoint_lat = abs(self._waypoint_lat) * self._quadrants[self._cur_quadrant][0]
        self._waypoint_long = abs(self._waypoint_long) * self._quadrants[self._cur_quadrant][1]

    def rotate_left(self, degrees):
        cuad_offset = degrees//90
        self._cur_quadrant = (self._cur_quadrant + cuad_offset) % 4
        self._rotate(cuad_offset)

    def rotate_right(self, degrees):
        cuad_offset = degrees//90
        self._cur_quadrant = (self._cur_quadrant - cuad_offset) % 4
        self._rotate(cuad_offset)

    def relocate(self):
        if self._waypoint_lat > 0 and self._waypoint_long > 0:
            self._cur_quadrant = 0
        if self._waypoint_lat > 0 and self._waypoint_long < 0:
            self._cur_quadrant = 1
        if self._waypoint_lat < 0 and self._waypoint_long < 0:
            self._cur_quadrant = 2
        if self._waypoint_lat < 0 and self._waypoint_long > 0:
            self._cur_quadrant = 3

    def go_north(self, distance):
        self._waypoint_lat += distance        
        self.relocate()

    def go_south(self, distance):
        self._waypoint_lat -= distance
        self.relocate()

    def go_east(self, distance):
        self._waypoint_long += distance
        self.relocate()
    
    def go_west(self, distance):
        self._waypoint_long -= distance
        self.relocate()

    def forward(self, value):
        self._lat += value * self._waypoint_lat
        self._long += value * self._waypoint_long


print('Part 2')
ferry = WaypointShip()
for (action, value) in navigation:
    ferry.maneuver(action, value)

print(f'\tSolution Found: {manhattan(*ferry.location)}')

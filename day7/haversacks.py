# -*- coding:utf-8 -*-

import os
import re


def read_input():
    with open(os.path.join('day7', 'input'), 'r') as f:
        return f.read().splitlines()


def lines_to_graph():
    bag_graph = {}
    lines = read_input()
    for line in lines:
        outer_bag = re.findall('^\w+ \w+', line)[0]
        inner_bags = re.findall('(\d+) (\w+ \w+)', line)
        for count, bag in inner_bags:
            if bag in bag_graph:
                bag_graph[bag].append((outer_bag, count))
            else:
                bag_graph[bag] = [(outer_bag, count)]
        if outer_bag not in bag_graph:
            bag_graph[outer_bag] = []
    return bag_graph



# Part 1
print('Part 1')
bag_graph = lines_to_graph()
def search(graph, bag):
    explored = []
    frontier = [(bag, None)]
    while frontier:
        bag,_ = frontier.pop(0)
        explored.append(bag)
        frontier += graph[bag]
    return len(set(explored))-1

explored_bags = search(bag_graph, 'shiny gold')
print(f'\tSolution Found: {explored_bags}')


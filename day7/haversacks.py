# -*- coding:utf-8 -*-

import os
import re


def read_input():
    with open(os.path.join('day7', 'input'), 'r') as f:
        return f.read().splitlines()


# Part 1
def lines_to_inverse_graph():
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


bag_graph = lines_to_inverse_graph()
def search_colors(graph, bag):
    explored = []
    frontier = [(bag, None)]
    while frontier:
        bag,_ = frontier.pop(0)
        explored.append(bag)
        frontier += graph[bag]
    return len(set(explored))-1

print('Part 1')
explored_bags = search_colors(bag_graph, 'shiny gold')
print(f'\tSolution Found: {explored_bags}')


# Part 2
def lines_to_direct_graph():
    bag_graph = {}
    lines = read_input()
    for line in lines:
        outer_bag = re.findall('^\w+ \w+', line)[0]
        inner_bags = re.findall('(\d+) (\w+ \w+)', line)
        bag_graph[outer_bag] = inner_bags
    return bag_graph

bag_graph = lines_to_direct_graph()
def search_needed_bags(graph, bag):
    if not graph[bag]:  
        return 0
    return sum([int(x[0]) + int(x[0]) * search_needed_bags(graph, x[1]) for x in graph[bag]])

print('Part 2')
needed_bags = search_needed_bags(bag_graph, 'shiny gold')
print(f'\tSolution Found: {needed_bags}')
    






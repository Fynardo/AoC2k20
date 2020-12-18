# -*- coding:utf-8 -*-

import os
import re


def read_input():
    with open(os.path.join('day16','input'), 'r') as f:
        data = f.read()
        fields,my_ticket,nearby_tickets = data.split('\n\n')
        fields = re.findall('(.*): (\d+)-(\d+) or (\d+)-(\d+)', fields)
        rules = {}
        for f,l1,h1,l2,h2 in fields:
            rules[f] = set.union(set(range(int(l1),int(h1)+1)), set(range(int(l2),int(h2)+1)))
        my_ticket = eval(my_ticket.split('\n')[1])
        nearby_tickets = [eval(ticket) for ticket in nearby_tickets.split('\n')[1:-1]]
    return rules, my_ticket, nearby_tickets



rules, my_ticket, nearby_tickets = read_input()
# Part 1
print('Part 1')
merged_rules = set.union(*rules.values())
merged_tickets = [f for t in nearby_tickets for f in t]
invalid_fields = filter(lambda x: x not in merged_rules, merged_tickets)
print(f'\tSolution Found: {sum(invalid_fields)}')



                           

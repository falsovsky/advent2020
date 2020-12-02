#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

database = []

# read input
regex = r"(\d+)-(\d+) (\w): (\w+)"
fp = open('input', 'r') 
for line in fp:
    m = re.search(regex, line)
    database.append({
        'a': int(m.group(1)),
        'b': int(m.group(2)),
        'c': m.group(3),
        'p': m.group(4)
    })
fp.close()

# part1
valid = 0
for i in database:
    counter = 0
    for c in i['p']:
        if c == i['c']:
            counter += 1
    if (counter >= i['a'] and
            counter <= i['b']):
        valid += 1
print('part1', valid)

# part2
valid = 0
for i in database:
    counter = 0
    idxa = i['a'] - 1
    idxb = i['b'] - 1
    if i['p'][idxa] == i['c']:
        counter += 1
    if i['p'][idxb] == i['c']:
        counter += 1
    if counter == 1:
        valid +=1
print('part2', valid)
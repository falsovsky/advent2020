#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

bags = []

# read input
fp = open('input', 'r')
for line in fp:
    bags.append(line.strip())
fp.close()

# part 1
regex_name = r"([\w ]+) bags contain (\d+).*"
regex_contents = r"(\d+) ([\w ]+) bags?"
def baggings(name):
    types = []
    for bag in bags:
        bagname = re.search(regex_name, bag)
        contents = re.findall(regex_contents, bag)
        if contents:
            for c in contents:
                if c[1] == name:
                    srcname = bagname.group(1)
                    if srcname not in types:
                        types.append(srcname)
                    zbr = baggings(srcname)
                    for i in zbr:
                        if i not in types:
                            types.append(i)
    return types
print('part1', len(baggings('shiny gold')))

# part 2
def baggings2(name, number):
    total = 0
    for bag in bags:
        m1 = re.search(regex_name, bag)
        if m1 and m1.group(1) == name:
            m2 = re.findall(regex_contents, bag)
            if m2:
                for m in m2:
                    total += number * baggings2(m[1], int(m[0]))
    return total + number
print('part2', baggings2('shiny gold', 1) - 1)
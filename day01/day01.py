#!/usr/bin/env python
# -*- coding: utf-8 -*-

entries = []

fp = open('input', 'r') 
for line in fp:
    entries.append(int(line))
fp.close()

#print(entries)

print("Part1")
for a in entries:
    for b in entries:
        if a + b == 2020:
            print(a*b)
            
print("Part2")
for a in entries:
    for b in entries:
        for c in entries:
            if a + b + c == 2020:
                print(a*b*c)

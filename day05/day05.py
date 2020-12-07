#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

passes = []
sorted_passes = []

# read input
fp = open('input', 'r')
for line in fp:
    passes.append(line.strip())
fp.close()

# part 1
def boarding(zbr, pos = 0, rfirst = 0, rlast = 127, cfirst = 0, clast = 7):
    #print('row', rfirst, rlast, cfirst, clast)
    changed = False
    if pos < len(zbr):
        changed = True
        if zbr[pos] == 'F':
            rlast = math.floor((rlast / 2) + (rfirst / 2))
        elif zbr[pos] == 'B':
            rfirst = math.ceil((rlast / 2) + (rfirst / 2))
        elif zbr[pos] == 'L':
            clast = math.floor((clast / 2) + (cfirst / 2))
        elif zbr[pos] == 'R':
            cfirst = math.ceil((clast / 2) + (cfirst / 2))
    
    if changed == True:
        return boarding(zbr, pos + 1, rfirst, rlast, cfirst, clast)
    else:
        return rlast * 8 + clast

hid = 0
for p in passes:
    zbr = boarding(p)
    sorted_passes.append(zbr)
    if zbr> hid:
        hid = zbr
print('part1', hid)

# part 2
tid = 0
for x in range(math.floor(hid / 2), hid):
    if x not in sorted_passes:
        tid = x
print('part2', tid)

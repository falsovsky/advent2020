#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

EMPTY = "L"
OCCUP = "#"
FLOOR = "."

# https://codereview.stackexchange.com/a/62165
rules = [
    [-1, -1], [-1, 0], [-1, +1],
    [ 0, -1],          [ 0, +1],
    [+1, -1], [+1, 0], [+1, +1]
]

# read input
grid = []
fp = open('input', 'r')
for line in fp:
    row = []
    for c in line.strip():
        row.append(c)
    grid.append(row)
fp.close()

def shallow_find(items, x, y, xplus, yplus):
    newx = x + xplus
    newy = y + yplus
    if newx >= 0 and newx < len(items) and newy >= 0 and newy < len(items[newx]):
        if items[newx][newy] in [EMPTY, OCCUP]:
            return items[newx][newy]
    return False

def solve1(items):
    seats = copy.deepcopy(items)
    for idxline in range(0,len(items)):
        for idxrow in range(0, len(items[idxline])):
            value = items[idxline][idxrow]
            if value != ".":
                neighbours = []
                for rule in rules:
                    neighbour = shallow_find(items, idxline, idxrow, rule[0], rule[1])
                    if neighbour:
                        neighbours.append(neighbour)
                if value == EMPTY and neighbours.count(OCCUP) == 0:
                    seats[idxline][idxrow] = OCCUP
                if value == OCCUP and neighbours.count(OCCUP) >= 4:
                    seats[idxline][idxrow] = EMPTY
    return seats

def deep_find(items, x, y, xplus, yplus):
    newx = x
    newy = y
    while True:
        newx += xplus
        newy += yplus
        if newx < 0 or newx >= len(items) or newy < 0 or newy >= len(items[newx]):
            break
        if items[newx][newy] in [EMPTY, OCCUP]:
            return items[newx][newy]
    return False

def solve2(items):
    seats = copy.deepcopy(items)
    for idxline in range(0,len(items)):
        for idxrow in range(0, len(items[idxline])):
            value = items[idxline][idxrow]
            if value != ".":
                neighbours = []
                for rule in rules:
                    neighbour = deep_find(items, idxline, idxrow, rule[0], rule[1])
                    if neighbour:
                        neighbours.append(neighbour)
                if value == EMPTY and neighbours.count(OCCUP) == 0:
                    seats[idxline][idxrow] = OCCUP
                if value == OCCUP and neighbours.count(OCCUP) >= 5:
                    seats[idxline][idxrow] = EMPTY
    return seats

zbr = copy.deepcopy(grid)
while True:
    new = solve1(zbr)
    equal = True
    for x in range(0, len(zbr)):
        for y in range(0, len(zbr[x])):
            if zbr[x][y] != new[x][y]:
                equal = False
                break
    if equal:
        part1 = 0
        for x in new:
            part1 += x.count(OCCUP)
        break
    zbr = copy.deepcopy(new)
print("part1", part1)


zbr = copy.deepcopy(grid)
while True:
    new = solve2(zbr)
    equal = True
    for x in range(0, len(zbr)):
        for y in range(0, len(zbr[x])):
            if zbr[x][y] != new[x][y]:
                equal = False
                break
    if equal:
        part2 = 0
        for x in new:
            part2 += x.count(OCCUP)
        break
    zbr = copy.deepcopy(new)
print("part2", part2)

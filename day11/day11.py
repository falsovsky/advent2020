#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import copy

# read input
grid = []
fp = open('input', 'r')
for line in fp:
    row = []
    for c in line.strip():
        row.append(c)
    grid.append(row)
fp.close()

# part 1
pp = pprint.PrettyPrinter(width=60, compact=True)
#pp.pprint(grid)

empty = "L"
occup = "#"

def solve(items):
    seats = copy.deepcopy(items)
    for idxline in range(0,len(items)):
        for idxrow in range(0, len(items[idxline])):
            # Empty
            if items[idxline][idxrow] == empty:
                valid = True
                # left
                if idxrow - 1 >= 0 and items[idxline][idxrow - 1] == occup:
                    valid = False
                # right
                if idxrow + 1 < len(row) and items[idxline][idxrow + 1] == occup:
                    valid = False
                # up
                if idxline - 1 >= 0 and items[idxline - 1][idxrow] == occup:
                    valid = False
                # down
                if idxline + 1 < len(items) and items[idxline + 1][idxrow] == occup:
                    valid = False
                # up left
                if idxline - 1 >= 0 and idxrow - 1 >= 0 and items[idxline - 1][idxrow - 1] == occup:
                    valid = False
                # up right
                if idxline - 1 >= 0 and idxrow + 1 < len(row) and items[idxline - 1][idxrow + 1] == occup:
                    valid = False
                # down left
                if idxline + 1 < len(items) and idxrow - 1 >= 0 and items[idxline + 1][idxrow - 1] == occup:
                    valid = False
                # down right
                if idxline + 1 < len(items) and idxrow + 1 < len(row) and items[idxline + 1][idxrow + 1] == occup:
                    valid = False
                if valid == True:
                    seats[idxline][idxrow] = occup

            # Occupied
            if items[idxline][idxrow] == occup:
                c = 0
                # left
                if idxrow - 1 >= 0 and items[idxline][idxrow - 1] == occup:
                    c += 1
                # right 
                if idxrow + 1 < len(row) and items[idxline][idxrow + 1] == occup:
                    c += 1
                # up
                if idxline - 1 >= 0 and items[idxline - 1][idxrow] == occup:
                    c += 1
                # down
                if idxline + 1 < len(items) and items[idxline + 1][idxrow] == occup:
                    c += 1
                # up left
                if idxline - 1 >= 0 and idxrow - 1 >= 0 and items[idxline - 1][idxrow - 1] == occup:
                    c += 1
                # up right
                if idxline - 1 >= 0 and idxrow + 1 < len(row) and items[idxline - 1][idxrow + 1] == occup:
                    c += 1
                # down left
                if idxline + 1 < len(items) and idxrow - 1 >= 0 and items[idxline + 1][idxrow - 1] == occup:
                    c += 1
                # down right
                if idxline + 1 < len(items) and idxrow + 1 < len(row) and items[idxline + 1][idxrow + 1] == occup:
                    c += 1
                if c >= 4:
                    seats[idxline][idxrow] = empty
    return seats

def deep_find(items, x, y, xplus, yplus):
    result = []
    height = len(items)
    width = len(items[0])
    newx = x
    newy = y
    newx += xplus
    newy += yplus
    while newx >= 0 and newx < height and newx >= 0 and newx < width:
        if items[newx][newy] != ".":
            result.append(items[newx][newy])
            break
        newx -= xplus
        newy += yplus
    return result

def get_neighbours(items, x, y):
    neighbours = []

    # up
    #neighbours.append(deep_find(items, x, y, -1, 0))

    newx = x
    newy = y
    newx -= 1
    while newx >= 0:
        if items[newx][newy] != ".":
            neighbours.append(items[newx][newy])
            break
        newx -= 1


    # down
    newx = x
    newy = y
    newx += 1
    while newx < len(items):
        if items[newx][newy] != ".":
            neighbours.append(items[newx][newy])
            break
        newx += 1

    # left
    newx = x
    newy = y
    newy -= 1
    while newy >= 0:
        if items[newx][newy] != ".":
            neighbours.append(items[newx][newy])
            break
        newy -= 1

    # right
    newx = x
    newy = y
    newy += 1
    while newy < len(items[0]):
        if items[newx][newy] != ".":
            neighbours.append(items[newx][newy])
            break
        newy += 1

    # up left
    newx = x
    newy = y
    newx -= 1
    newy -= 1
    while newx >= 0 and newy >= 0:
        if items[newx][newy] != ".":
            neighbours.append(items[newx][newy])
            break
        newx -= 1
        newy -= 1
    
    # up right
    newx = x
    newy = y
    newx -= 1
    newy += 1
    while newx >= 0 and newy < len(items[0]):
        if items[newx][newy] != ".":
            neighbours.append(items[newx][newy])
            break
        newx -= 1
        newy += 1

    # down left
    newx = x
    newy = y
    newx += 1
    newy -= 1
    while newx < len(items) and newy >= 0:
        if items[newx][newy] != ".":
            neighbours.append(items[newx][newy])
            break
        newx += 1
        newy -= 1

    # down right
    newx = x
    newy = y
    newx += 1
    newy += 1
    while newx < len(items) and newy < len(items[0]):
        if items[newx][newy] != ".":
            neighbours.append(items[newx][newy])
            break
        newx += 1
        newy += 1
    
    return neighbours

def solve2(items):
    seats = copy.deepcopy(items)
    for idxline in range(0,len(items)):
        for idxrow in range(0, len(items[idxline])):
            value = items[idxline][idxrow]
            if value != ".":
                neighbours = get_neighbours(items, idxline, idxrow)
                if value == empty and neighbours.count(occup) == 0:
                    seats[idxline][idxrow] = occup
                if value == occup and neighbours.count(occup) >= 5:
                    seats[idxline][idxrow] = empty
    return seats

zbr = copy.deepcopy(grid)
while True:
    new = solve(zbr)
    equal = True
    for x in range(0, len(zbr)):
        for y in range(0, len(zbr[x])):
            if zbr[x][y] != new[x][y]:
                equal = False
                break
    if equal:
        part1 = 0
        for x in range(0, len(zbr)):
            for y in range(0, len(zbr[x])):
                if new[x][y] == occup:
                    part1 += 1
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
            part2 += x.count(occup)
        break
    zbr = copy.deepcopy(new)
print("part2", part2)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import copy

# read input
grid = []
fp = open('sample3', 'r')
for line in fp:
    row = []
    for c in line.strip():
        row.append(c)
    grid.append(row)
fp.close()

# part 1
pp = pprint.PrettyPrinter(width=60, compact=True)
pp.pprint(grid)

"""
print("max", len(grid), len(grid[0]))

#up left
x = len(grid)
y = len(grid[0])
while x >= 0 and y >= 0:
    x -= 1
    y -= 1
    print("upleft", x, y)

#up right
x = len(grid)
y = 0
while x >= 0 and y < len(grid[0]):
    x -= 1
    y += 1
    print("upright", x ,y)

# down left
x = 0
y = len(grid[0])
while x < len(grid) and y >= 0:
    x += 1
    y -= 1
    print("downleft", x, y)

# down right
x = 0
y = 0
while x < len(grid) and y < len(grid[0]):
    x += 1
    y += 1
    print("downright", x, y)
"""

occup = "#"
empty = "L"


def get_neighbours(items, x, y):
    neighbours = []

    # up
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

"""
# up 
x = 4
y = 3
print(x, y, grid[x][y])
x -= 1
found1 = False
found2 = False
rule2 = 0
while x >= 0:
    if grid[x][y] != ".":
        if found1 == False and grid[x][y] == occup:
            has_adjacent = False
            found1 = True
        elif found2 == False and grid[x][y] == occup:
            rule2 += 1
            found2 = True
    print(x)
    x -= 1
print(found1, found2, rule2)
"""

print(get_neighbours(grid, 0, 0))
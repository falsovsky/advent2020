#!/usr/bin/env python
# -*- coding: utf-8 -*-

cardinals = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270,
}

angles = {
      0: 'N',
     90: 'E',
    180: 'S',
    270: 'W',
}

movements = {
    'N': [ 0,  1],
    'S': [ 0, -1],
    'W': [-1,  0],
    'E': [ 1,  0],
}

def change(current, side, angle):
    if angle == 360:
        return current
    if side == 'L':
        tmp = cardinals[current] - angle
        while tmp < 0:
            tmp += 360
        return angles[tmp]
    if side == 'R':
        tmp = cardinals[current] + angle
        while(tmp >= 360):
            tmp -= 360
        return angles[tmp]

def forward(current, units):
    new = current[:]
    move = movements[current[2]]
    for idx in range(0, 2):
        if move[idx] > 0:
            new[idx] += units
        elif move[idx] < 0:
            new[idx] -= units
    return new

def change2(waypoint, side, angle):
    new = waypoint[:]
    if side == "L":
        for z in range(0, int(angle / 90)):
            x = new[1] * -1
            y = new[0]
            new[0] = x
            new[1] = y
    if side == "R":
        for z in range(0, int(angle / 90)):
            x = new[1]
            y = new[0] * -1
            new[0] = x
            new[1] = y
    return new

def forward2(current, waypoint, units):
    if waypoint[0] > 0: w1 = 'E'
    else: w1 = 'W'
    if waypoint[1] > 0: w2 = 'N'
    else: w2 = 'S'

    new = current[:]
    new.insert(2, 0)
    for i in range(0, units):
        new[2] = w1
        new = forward(new, abs(waypoint[0]))
        new[2] = w2
        new = forward(new, abs(waypoint[1]))

    return new[:-1]

# read input
nav = []
fp = open('input', 'r')
for line in fp:
    nav.append(line.strip())
fp.close()

# part1
current = [0, 0, 'E']
for i in nav:
    action, units = i[0], int(i[1:])
    if action == "F":
        current = forward(current, units)
    elif action in ["L", "R"]:
        current[2] = change(current[2], action, units)
    elif action in ['N', 'S', 'W', 'E']:
        move = movements[action]
        for idx in range(0, 2):
            if move[idx] > 0:
                current[idx] += units
            elif move[idx] < 0:
                current[idx] -= units
print('part1', abs(current[0]) + abs(current[1]))

# part2
current = [0, 0]
waypoint = [10, 1]
for i in nav:
    action, units = i[0], int(i[1:])
    if action == "F":
        current = forward2(current, waypoint, units)
    elif action in ["L", "R"]:
        waypoint = change2(waypoint, action, units)
    elif action in ['N', 'S', 'W', 'E']:
        move = movements[action]
        for idx in range(0, 2):
            if move[idx] > 0:
                waypoint[idx] += units
            elif move[idx] < 0:
                waypoint[idx] -= units
print('part2', abs(current[0]) + abs(current[1]))

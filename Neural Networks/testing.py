import sys
import math
import random


def simulate(a, b, c):
    start = [a, b, c]
    file = open(sys.argv[1], 'r+')
    total = file.readlines()
    layers = []
    if sys.argv[2] == 'T1':
        transfer = lambda x: x
    elif sys.argv[2] == 'T2':
        transfer = lambda x: x if x > 0 else 0
    elif sys.argv[2] == 'T3':
        transfer = lambda x: 1 / (1 + (math.e ** (-x)))
    else:
        transfer = lambda x: -1 + 2 / (1 + (math.e ** (-x)))
    for i in total:
        curr = i[:-1] if i[-1] == '\n' else i
        temp = curr.split(' ')
        layers.append([float(x) for x in temp if x != ''])
    for i in layers[:-1]:
        x = len(i) // len(start)
        temp = []
        for j in range(x):
            added = 0
            for k in range(len(start)):
                added += start[k] * i[j * len(start) + k]
            added = transfer(added)
            temp.append(added)
        start = temp
    for i in range(len(start)):
        start[i] = start[i] * layers[-1][i]
    return start[0]


keys = set()
for i in range(-15, 15, 3):
    for j in range(-15, 15, 3):
        keys.add((i / 10.0, j / 10.0))
for i in range(100):
    keys.add((random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5)))
fail_count = 0
for m in keys:
    x = m[0]
    y = m[1]
    z = simulate(x, y, 1)
    if (x * x + y * y > 1.1773591057948605) != (z >= 0.5):
        fail_count += 1
        print("{}:{}:{}".format(m, x * x + y * y >= 1.308809905580818, z))
print(fail_count)

import sys
import math


def main():
    start = [float(x) for x in sys.argv[3:]]
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
        layers.append([float(x) for x in temp if x!=''])
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
    print(str(start).replace('[', '').replace(']', '').replace(',', ''))


if __name__ == '__main__':
    main()

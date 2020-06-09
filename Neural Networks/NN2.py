import sys
import math
import random
import time


def transfer(x):
    return 1 / (1 + math.e ** (-x))


def derivative(x):
    return x * (1 - x)


def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError
    temp = 0
    for i in range(len(a)):
        temp += a[i] * b[i]
    return temp


def simulate(layer, f, pairs):
    result = {}
    temp = [-1]
    to_multiply = pairs
    while len(f[temp[0]]) != 0:
        if temp[0] == -1:
            for i in f[-1]:
                result[i] = transfer(dot_product(to_multiply, layer[i]))
            temp = f[-1]
            to_multiply = [result[x] for x in temp]
        else:
            for j in f[temp[0]]:
                if len(f[j]) == 0:
                    result[j] = dot_product(to_multiply, layer[j])
                else:
                    result[j] = transfer(dot_product(to_multiply, layer[j]))
            temp = f[temp[0]]
            to_multiply = [result[x] for x in temp]
    return result


def total_error(start, weights, f):
    net = 0
    for x in start:
        done = simulate(weights, f, x)[len(weights) - 1]
        net += (start[x] - done) ** 2
    return net / 2


def main():
    z = time.time()
    f = open(sys.argv[1])
    k = f.readlines()
    train = {}
    s = 0
    for i in k:
        if i != '':
            temp = i.split()
            b = temp.index('=>')
            x = tuple([int(x) for x in temp[:b]] + [1])
            y = int(temp[b + 1])
            train[x] = y
            s = len(x)
    layer_count = [2, 1, 1]
    layers = []
    prev = [-1]
    forward = {prev[0]: []}
    # for i in layer_count:
    #     for j in range(i):
    #         temp = [random.random() for x in range(s)]
    #         layers.append(temp)
    #         for t in prev:
    #             forward[t].append(len(layers) - 1)
    #         forward[len(layers) - 1] = []
    #     prev = forward[prev[0]]
    #     s = i
    layers = [[2, 1, 0], [1, 2, 3], [0.5, 0.75], [0.875]]
    forward = {-1: [0, 1], 0: [2], 1: [2], 2: [3], 3: []}
    reverse = {}
    st = ""
    for i in range(len(layers)):
        for j in layers[i]:
            st += str(j) + " "
        if i >= layer_count[0] - 1:
            st += '\n'
    print("Epoch 0:\nLayer counts: {}\n{}".format(str(len(layers[0])) + " 2 1 1", st))
    for i in forward:
        for j in forward[i]:
            if j not in reverse:
                reverse[j] = [i]
            else:
                reverse[j].append(i)
    total = [[0 for x in range(len(y))] for y in layers]
    count = 0
    while True:
        count += 1
        if total_error(train, layers, forward) <= 0.01:
            break
        for i in train:
            temp = simulate(layers, forward, i)
            prop_error = [0 for x in temp]
            prop_error[-1] = train[i] - temp[len(temp) - 1]
            for j in range(len(temp) - 2, -1, -1):
                mult_1 = [prop_error[x] for x in forward[j]]
                mult_2 = [layers[x][reverse[x].index(j)] for x in forward[j]]
                prop_error[j] = dot_product(mult_1, mult_2) * derivative(temp[j])
            for j in range(len(layers)):
                if reverse[j][0] == -1:
                    for k in range(len(layers[j])):
                        total[j][k] += i[k] * prop_error[j]
                else:
                    for k in range(len(reverse[j])):
                        total[j][k] += temp[reverse[j][k]] * prop_error[j]
        for i in range(len(total)):
            for j in range(len(total[i])):
                total[i][j] /= len(train)
                total[i][j] *= 0.1
                layers[i][j] += total[i][j]
        st = ""
        for i in range(len(layers)):
            for j in layers[i]:
                st += str(j) + " "
            if i > 0:
                st += '\n'
        print("Epoch {}:\nLayer counts: {}\n{}".format(count, str(len(layers[0])) + " 2 1 1", st))
        if len(layers[0]) < 4 and time.time() - z > 15:
            for i in range(len(layers)):
                for j in range(len(layers[i])):
                    layers[i][j] = random.random()
            z = time.time()
            count = 1


if __name__ == '__main__':
    main()

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


def verify_inequality(x, y, compare, slope):
    distance = math.sqrt(x ** 2 + y ** 2)
    change = slope * distance
    if compare == 0:
        return 1 - change
    elif compare == 1:
        return change
    elif compare == 2:
        return 1 - change
    else:
        return change


def main():
    f = sys.argv[1]
    if '=' in f:
        if '<' in f:
            fix = f.split('<=')
            compare_type = 0
        else:
            fix = f.split('>=')
            compare_type = 1
    else:
        if '<' in f:
            fix = f.split('<')
            compare_type = 2
        else:
            fix = f.split('>')
            compare_type = 3

    compare_num = float(fix[-1])
    # test = verify_inequality(99, 99, compare_type, compare_num)
    keys = set()
    for i in range(-15, 15):
        for j in range(-15, 15):
            keys.add((i / 10.0, j / 10.0, 1))
    radius = math.sqrt(compare_num)

    for i in range(100):
        theta = random.uniform(0, 2 * math.pi)
        calc_radius = random.uniform(radius - .2, radius + .2)
        keys.add((calc_radius*math.cos(theta), calc_radius*math.sin(theta), 1))
    slope = 0.5 / radius

    start = time.time()
    train = {x: verify_inequality(x[0], x[1], compare_type, slope) for x in keys}
    major_list = list(keys)
    s = 3
    layer_count = [8, 2, 1, 1]
    layers = []
    prev = [-1]
    forward = {prev[0]: []}
    for i in layer_count:
        for j in range(i):
            temp = [random.random() for x in range(s)]
            layers.append(temp)
            for t in prev:
                forward[t].append(len(layers) - 1)
            forward[len(layers) - 1] = []
        prev = forward[prev[0]]
        s = i
    # layers = [[2, 1, 0], [1, 2, 3], [0.5, 0.75], [0.875]]
    # forward = {-1: [0, 1], 0: [2], 1: [2], 2: [3], 3: []}
    reverse = {}
    st = ""
    now = layer_count[0]
    t = 1
    for i in range(len(layers)):
        for j in layers[i]:
            st += str(j) + " "
        if i == now - 1:
            st += '\n'
            now += layer_count[t] if t < len(layer_count) else 0
            t += 1
    print("Layer counts: {}\n{}".format(
        str(len(layers[0])) + ' ' + str(layer_count).replace('[', '').replace(']', '').replace(',', ''), st))
    for i in forward:
        for j in forward[i]:
            if j not in reverse:
                reverse[j] = [i]
            else:
                reverse[j].append(i)
    total = [[0 for x in range(len(y))] for y in layers]
    count = 0
    archive = {x: [[0 for z in range(len(y))] for y in layers] for x in train}
    errors_total = 0
    init_error = {}
    while True:
        for i in train:
            temp = simulate(layers, forward, i)
            prop_error = [0 for x in temp]
            prop_error[-1] = train[i] - temp[len(temp) - 1]
            # if train[i] == 1:
            #     prop_error[-1] = train[i] - temp[len(temp) - 1] if temp[len(temp) - 1] <= 0.5 else 0
            # else:
            #     prop_error[-1] = train[i] - temp[len(temp) - 1] if temp[len(temp) - 1] >= 0.5 else 0
            errors_total += prop_error[-1]
            init_error[i] = prop_error[-1]
            for j in range(len(temp) - 2, -1, -1):
                mult_1 = [prop_error[x] for x in forward[j]]
                mult_2 = [layers[x][reverse[x].index(j)] for x in forward[j]]
                prop_error[j] = dot_product(mult_1, mult_2) * derivative(temp[j])
            for j in range(len(layers)):
                if reverse[j][0] == -1:
                    for k in range(len(layers[j])):
                        archive[i][j][k] = i[k] * prop_error[j]
                        total[j][k] += archive[i][j][k]
                        layers[j][k] += 0.1 * archive[i][j][k]

                else:
                    for k in range(len(reverse[j])):
                        archive[i][j][k] = temp[reverse[j][k]] * prop_error[j]
                        total[j][k] += archive[i][j][k]
                        layers[j][k] += 0.1 * archive[i][j][k]
        modified_count = 100
        # for i in range(len(total)):
        #     for j in range(len(total[i])):
        #         z = total[i][j]
        #         z /= 100
        #         z *= 0.0005
        #         layers[i][j] += z
        st = ""
        now = layer_count[0]
        t = 1
        for i in range(len(layers)):
            for j in layers[i]:
                st += str(j) + " "
            if i == now - 1:
                st += '\n'
                now += layer_count[t] if t < len(layer_count) else 0
                t += 1
        first_save = "Layer counts: {}\n{}".format(
            str(len(layers[0])) + ' ' + str(layer_count).replace('[', '').replace(']', '').replace(',', ''), st)
        print(first_save)
        if time.time() - start > 100:
            print(first_save)
            break
    # while True:
    #     for i in range(len(total)):
    #         for j in range(len(total[i])):
    #             total[i][j] -= archive[major_list[count]][i][j]
    #     errors_total -= init_error[major_list[count]]
    #     count += 1
    #     key = (random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5), 1)
    #
    #     major_list.append(key)
    #     train[key] = verify_inequality(key[0], key[1], compare_type, compare_num)
    #     archive[key] = [[0 for z in range(len(y))] for y in layers]
    #     temp = simulate(layers, forward, key)
    #     prop_error = [0 for x in temp]
    #     prop_error[-1] = train[key] - temp[len(temp) - 1]
    #     # if train[key] == 1:
    #     #     prop_error[-1] = train[key] - temp[len(temp) - 1] if temp[len(temp) - 1] <= 0.5 else 0
    #     # else:
    #     #     prop_error[-1] = train[key] - temp[len(temp) - 1] if temp[len(temp) - 1] >= 0.5 else 0
    #     errors_total += prop_error[-1]
    #     init_error[key] = prop_error[-1]
    #     for j in range(len(temp) - 2, -1, -1):
    #         mult_1 = [prop_error[x] for x in forward[j]]
    #         mult_2 = [layers[x][reverse[x].index(j)] for x in forward[j]]
    #         prop_error[j] = dot_product(mult_1, mult_2) * derivative(temp[j])
    #     for j in range(len(layers)):
    #         if reverse[j][0] == -1:
    #             for k in range(len(layers[j])):
    #                 archive[key][j][k] = key[k] * prop_error[j]
    #                 total[j][k] += archive[key][j][k]
    #         else:
    #             for k in range(len(reverse[j])):
    #                 archive[key][j][k] = temp[reverse[j][k]] * prop_error[j]
    #                 total[j][k] += archive[key][j][k]
    #     for i in range(len(total)):
    #         for j in range(len(total[i])):
    #             z = total[i][j]
    #             z /= 100
    #             z *= 0.0005
    #             layers[i][j] += z
    #     modified_count += 1
    #     st = ""
    #     now = layer_count[0]
    #     t = 1
    #     for i in range(len(layers)):
    #         for j in layers[i]:
    #             st += str(j) + " "
    #         if i == now - 1:
    #             st += '\n'
    #             now += layer_count[t] if t < len(layer_count) else 0
    #             t += 1
    #     print("Layer counts: {}\n{}".format(
    #         str(len(layers[0])) + ' ' + str(layer_count).replace('[', '').replace(']', '').replace(',', ''), st))
    #     if modified_count % 5000 == 0 or errors_total == 0:
    #         errors_total = 0
    #         total = [[0 for x in range(len(y))] for y in layers]
    #         for z in range(count, len(major_list)):
    #             temp = simulate(layers, forward, major_list[z])
    #             prop_error = [0 for x in temp]
    #             prop_error[-1] = train[major_list[z]] - temp[len(temp) - 1]
    #             # if train[major_list[z]] == 1:
    #             #     prop_error[-1] = train[major_list[z]] - temp[len(temp) - 1] if temp[len(temp) - 1] <= 0.5 else 0
    #             # else:
    #             #     prop_error[-1] = train[major_list[z]] - temp[len(temp) - 1] if temp[len(temp) - 1] >= 0.5 else 0
    #             errors_total += prop_error[-1]
    #             init_error[major_list[z]] = prop_error[-1]
    #             for j in range(len(temp) - 2, -1, -1):
    #                 mult_1 = [prop_error[x] for x in forward[j]]
    #                 mult_2 = [layers[x][reverse[x].index(j)] for x in forward[j]]
    #                 prop_error[j] = dot_product(mult_1, mult_2) * derivative(temp[j])
    #             for j in range(len(layers)):
    #                 if reverse[j][0] == -1:
    #                     for k in range(len(layers[j])):
    #                         archive[major_list[z]][j][k] = major_list[z][k] * prop_error[j]
    #                         total[j][k] += archive[major_list[z]][j][k]
    #                 else:
    #                     for k in range(len(reverse[j])):
    #                         archive[major_list[z]][j][k] = temp[reverse[j][k]] * prop_error[j]
    #                         total[j][k] += archive[major_list[z]][j][k]


if __name__ == '__main__':
    main()

import random


class Node:
    pairs = 0

    def __init__(self, word):
        self.degree = 0
        self.con = set()
        self.w = word

    def __str__(self):
        return self.w

    def addEdge(self, node):
        self.con.add(node)
        self.degree += 1

    def connect(self, other):
        self.addEdge(other)
        other.addEdge(self)
        Node.pairs += 1


def pick(add, nice, translate):
    while True:
        b = translate[random.choice(nice)]
        if b not in add.con:
            return b

def diameter(total):
    x = max(total, key=lambda b: b.degree)
    to_check = [(x, 0)]
    finished = {}
    count = 0
    while count < len(to_check):
        next = to_check[count][0].con
        for j in next:
            if j.__str__() in finished:
                continue
            if j.degree == 1:
                finished[j.__str__()] = to_check[count][1] + 1
            else:
                finished[j.__str__()] = to_check[count][1] + 1
                to_check.append((j, to_check[count][1] + 1))
        count += 1
    visited = list(finished.keys())
    d = sorted(visited, key=lambda f: finished[f])
    return finished[d[-1]] + finished[d[-2]]


total = [Node(str(x)) for x in range(5)]

total[0].connect(total[1])
total[1].connect(total[2])
total[1].connect(total[3])
total[2].connect(total[3])

total_degree = 0
average = 0
net = []
translate = {}
for i in total:
    total_degree += i.degree
    translate[i.__str__()] = i
    z = [i.__str__()] * (i.degree+1)
    for j in z:
        net.append(j)

count = 5
zero_count = 1
while len(total) < 100000:
    average = total_degree / len(total)
    if abs(average-4) == 0:
        target_degree = random.randint(3, 5)
    elif average > 4:
        target_degree = random.randint(0, 3)
    else:
        if len(total) - zero_count <= 5:
            target_degree = len(total) - zero_count
        else:
            target_degree = random.randint(5, min(len(total) - zero_count, 8))

    total.append(Node(str(count)))
    total_degree += 2 * target_degree
    temp = net
    for i in range(target_degree):
        m = pick(total[-1], temp, translate)
        m.connect(total[-1])
        net.append(m.__str__())
    translate[total[-1].__str__()] = total[-1]
    z = [total[-1].__str__()] * (total[-1].degree+1)
    if total[-1].degree == 0:
        zero_count += 1
    for j in z:
        net.append(j)
    count += 1

print()
print(diameter(total))
print()
temp = {}
for i in total:
    if i.degree not in temp:
        temp[i.degree] = 1
    else:
        temp[i.degree] += 1
nice = sorted(list(temp.keys()))
for i in nice:
    print(i)
print()
for i in nice:
    print('{}'.format(temp[i]))

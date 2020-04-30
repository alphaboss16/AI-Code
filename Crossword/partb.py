import random


class Node:
    pairs = 0

    def __init__(self, word):
        self.degree = 0
        self.con = set()
        self.w = word[0:-1]

    def __str__(self):
        return self.w

    def addEdge(self, node):
        self.con.add(node)
        self.degree += 1

    def connect(self, other):
        self.addEdge(other)
        other.addEdge(self)
        Node.pairs += 1


def pick(add, total):
    while True:
        for i in total:
            if i != add and add not in i.con:
                b = i.degree * 10
                z = random.randint(0, 100)
                if z < b:
                    return i


total = [Node(str(x)) for x in range(5)]

total[0].connect(total[1])
total[1].connect(total[2])
total[1].connect(total[3])
total[2].connect(total[3])

total_degree = 0
average = 0
for i in total:
    total_degree += i.degree

count = 5
while len(total) < 100000:
    average = total_degree // len(total)
    if average > 4:
        target_degree = random.randint(0, 4)
    else:
        target_degree = random.randint(4, 12)
    total.append(Node(count))
    total_degree += 2 * target_degree
    for i in range(target_degree):
        m = pick(total[-1], total)
        m.connect(total[-1])
    count += 1

temp = {}
for i in total:
    if i.degree not in temp:
        temp[i.degree] = 1
    else:
        temp[i.degree] += 1
nice = sorted(list(temp.keys()))
for i in nice:
    print(i)
for i in nice:
    print('{}'.format(temp[i]))

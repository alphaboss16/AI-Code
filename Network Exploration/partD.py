import random


class Node:
    pairs = 0

    def __init__(self, word, age):
        self.degree = 0
        self.con = set()
        self.w = word
        self.age = age
        self.sex = random.choice(['m', 'f'])
        self.kid = 0

    def __str__(self):
        return self.w

    def addEdge(self, node):
        self.con.add(node)
        self.degree += 1

    def connect(self, other):
        self.addEdge(other)
        other.addEdge(self)
        Node.pairs += 1

    def pass_year(self):
        self.age += 1

    def disconnect(self, other):
        self.con.remove(other)
        other.con.remove(self)

    def kids(self):
        self.kid += 1


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


def pick(add, nice, translate):
    while True:
        b = translate[random.choice(nice)]
        if b not in add.con:
            return b


total = [Node(str(x), x) for x in range(5)]

total[0].connect(total[1])
total[1].connect(total[2])
total[1].connect(total[3])
total[2].connect(total[3])
total[4].connect(total[0])

total_degree = 0
average = 0
net = []
translate = {}
for i in total:
    total_degree += i.degree
    translate[i.__str__()] = i
    z = [i.__str__()] * i.degree
    for j in z:
        net.append(j)

count = 5
time = 0
stored = {}
while time < 300 and len(total) < 105000:
    stored[time] = len(total)
    to_kill = set()
    for i in total:
        if i.age >= 75:
            if random.randint(1, 2) == 1:
                to_kill.add(i)
        elif i.age >= 60:
            if random.randint(1, 5) == 1:
                to_kill.add(i)
        elif i.age >= 50:
            if random.randint(1, 10) == 1:
                to_kill.add(i)
        else:
            if random.randint(1, 50) == 1:
                to_kill.add(i)
    for i in to_kill:
        total.remove(i)
        temp = {x for x in i.con}
        for j in temp:
            i.disconnect(j)
    net = [x for x in net if x not in to_kill]
    birth = []
    for i in total:
        i.pass_year()
    for i in total:
        if i.sex == 'f':
            if 20 < i.age <= 35 and random.randint(1, 100) <= 85 and i.kid < 2:
                average = total_degree / len(total)
                if abs(average - 2) == 0:
                    target_degree = random.randint(1, 3)
                elif average > 2:
                    target_degree = random.randint(1, 2)
                else:
                    target_degree = random.randint(2, 3)
                total_degree += 2 * target_degree
                total.append(Node(str(count), 0))
                for j in range(target_degree - 1):
                    m = pick(total[-1], net, translate)
                    m.connect(total[-1])
                    net.append(m.__str__())
                translate[total[-1].__str__()] = total[-1]
                z = [total[-1].__str__()] * total[-1].degree
                for j in z:
                    net.append(j)
                count += 1
    time += 1
print(stored)
for k in stored.keys():
    print(k)
for k in stored.keys():
    print(stored[k])
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
print()
print(diameter(total))
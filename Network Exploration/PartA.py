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
    z = sorted(visited, key=lambda m: finished[m])
    return finished[z[-1]] + finished[z[-2]]


total = [Node(str(x)) for x in range(100000)]

while Node.pairs < 250000:
    one = random.choice(total)
    two = random.choice(total)
    if one != two and one not in two.con:
        one.connect(two)
print(diameter(total))
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

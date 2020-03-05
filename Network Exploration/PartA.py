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


total = [Node(str(x)) for x in range(100000)]
while Node.pairs < 250000:
    one = random.choice(total)
    two = random.choice(total)
    if one != two and one not in two.con:
        one.connect(two)
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

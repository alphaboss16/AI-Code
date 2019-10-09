import sys
import time


class Node:
    pairs = 0

    def __init__(self, word):
        self.degree = 0
        self.con = set()
        self.w = word[0:-1]
        self.close = {word[0:i] + "_" + word[i + 1:-1] for i in range(len(word) - 1)}

    def __str__(self):
        return self.w

    def addEdge(self, node):
        self.con.add(node)
        self.degree += 1

    def connect(self, other):
        self.addEdge(other)
        other.addEdge(self)
        Node.pairs += 1


def getElem(el):
    return el[1]


def getDegree(node):
    return node.degree


def getFarthest(li, c):
    parseMe = {0: (li[c], 0)}
    b = 0
    m = 1
    k = [(li[c], 0)]
    ch = {li[c]}
    while b < len(parseMe):
        for it in parseMe[b][0].con:
            if it not in ch:
                k.append((it, parseMe[b][1] + 1))
                ch.add(it)
                parseMe[m] = (it, parseMe[b][1] + 1)
                m += 1
        b += 1
    z = sorted(k, key=getElem)
    return z[-1]


def fix(dict, l):
    curr = l
    to_ret = [curr]
    while dict[curr] != "":
        to_ret.append(dict[curr])
        curr = dict[curr]
    return to_ret[::-1]


def get_path(lis, curr, goal):
    parse_me = {0: lis[curr]}
    b = 0
    m = 1
    ch = {lis[curr]: ""}
    while b < len(parse_me):
        for it in parse_me[b].con:
            if it not in ch:
                if it == lis[goal]:
                    ch[it] = parse_me[b]
                    return fix(ch, lis[goal])
                ch[it] = parse_me[b]
                parse_me[m] = it
                m += 1
        b += 1


def checkK3(li):
    return li[1] in li[0].con and li[2] in li[0].con and li[1] in li[2].con


def checkK4(li):
    return li[1] in li[0].con and li[2] in li[0].con and li[3] in li[0].con and li[1] in li[2].con and li[2] in li[3].con and li[1] in li[3].con


def connectedComp(listTotal):
    t = set()
    toRet = []

    for i in range(len(listTotal)):
        if listTotal[i] not in t:
            parseMe = {0: listTotal[i]}
            b = 0
            m = 1
            k = {listTotal[i]}
            t.add(listTotal[i])
            while b < len(parseMe):
                for it in parseMe[b].con:
                    if it not in k:
                        t.add(it)
                        k.add(it)
                        parseMe[m] = it
                        m += 1
                b += 1

            toRet.append(k)
    return toRet


def creategraph():
    k = time.time()
    allNodes = []
    x = 0
    allClose = {}
    with open(sys.argv[1], 'r') as f:
        for line in f:
            temp = Node(line)
            for item in temp.close:
                if item in allClose:
                    for t in allClose[item]:
                        t.connect(temp)
                    allClose[item].add(temp)
                else:
                    allClose[item] = {temp}

            allNodes.append(temp)
    d = len(allNodes)
    b = sorted(allNodes, key=getDegree)
    dict = {}
    print("Word count: {}".format(d))
    print("Edge count: {}".format(Node.pairs))
    last = 0
    for i in range(len(b)):
        if b[i].degree not in dict:
            dict[b[i].degree] = 1
            last = i - 1
        else:
            dict[b[i].degree] += 1

    for i in range(b[-1].degree + 1):
        if i not in dict:
            dict[i] = 0

    print("Degree list: {}".format([dict[i] for i in range(b[-1].degree + 1)]))
    print("Construction time: {}s".format(round(time.time() - k, 2)))
    if len(sys.argv) > 2:
        print('Second degree word: {}'.format(b[last].w))
        z = connectedComp(allNodes)
        count = 0
        size = set()
        for i in z:
            if len(i) not in size:
                count += 1
                size.add(len(i))
        print("Connected component size count: {}".format(count))
        z = sorted(z, key=len)
        print("Largest component size: {}".format(len(z[-1])))
        count = 0
        for i in range(len(z)):
            if len(z[i]) == 2:
                count += 1
            elif count != 0:
                break
        print("K2 count: {}".format(count))
        count = 0
        for i in range(len(z)):
            if len(z[i]) == 3:
                if checkK3(list(z[i])):
                    count += 1
            elif count != 0:
                break
        print("K3 count: {}".format(count))
        count = 0
        for i in range(len(z)):
            if len(z[i]) == 4:
                if checkK4(list(z[i])):
                    count += 1
            elif count != 0:
                break
        print("K4 count: {}".format(count))
        curr = -1
        goal = -1
        for i in range(len(allNodes)):
            if allNodes[i].w == sys.argv[2]:
                curr = i
            elif allNodes[i].w == sys.argv[3]:
                goal = i
        s = ""
        for i in allNodes[curr].con:
            s += str(i) + ', '
        print("Neighbors: {}".format(s[0:-2]))
        st = getFarthest(allNodes, curr)
        print("Farthest: {}".format(st[0]))
        st = get_path(allNodes, curr, goal)
        for i in range(len(st)):
            st[i] = str(st[i])
        print("Path: {}".format(str(st)[1:-1].replace('\'', '')))


def main():
    creategraph()


if __name__ == "__main__":
    main()

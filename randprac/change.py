import sys
def recurse(i, choices):
    if i<0:
        return None
    if i == 0:
        return [[]]
    else:
        k = []
        for j in choices:
            b = recurse(i-j, choices)
            if b is list:
                for z in b:
                    temp = []
                    for m in z:
                        temp.append(m)
                    temp.append(j)
                    k.append(temp)
        return k
b = int(sys.argv[1])
ch = sys.argv[2:]
m = {int(z) for z in ch}
stor = recurse(b, m)
for i in stor:
    i.sort()
fin = []
for i in stor:
    if i not in fin:
        fin.append(i)
print(len(fin))



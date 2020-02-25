global done
to_fill = {}
def count_vowels(word):
    return word.count('E') + word.count('T') + word.count('A') + word.count('O') + word.count('I') + word.count('N')
def get_subs(word):
    global done
    if word in done:
        return {}
    if word.count('-') == len(word):
        return {word}
    b = {word}
    done.add(word)
    for i in range(len(word)):
        if word[i] != '-':
            b = b.union(get_subs(word[0:i] + '-' + word[i + 1:]))
    return b
f = open('dct20k.txt')
dims=(10, 10)

k = ''.join(f.readlines()).split('\n')[:-1]
for i in k:
    if (len(i) <= dims[0] or len(i) <= dims[1]) and len(i) > 2:
        i = i.upper()
        if len(i) <= 5:
            done = set()
            x = get_subs(i)
            m = (i, count_vowels(i))
            for j in x:
                if j in to_fill:
                    to_fill[j].append(m)
                else:
                    to_fill[j] = [m]
        else:
            m = (i, count_vowels(i))
            for j in range(len(i)):
                st = len(i[0:j]) * '-' + i[j] + '-' * len(i[j + 1:])
                if st in to_fill:
                    to_fill[st].append(m)
                else:
                    to_fill[st] = [m]
            st = '-' * len(i)
            m = (i, count_vowels(i))
            if st in to_fill:
                to_fill[st].append(m)
            else:
                to_fill[st] = [m]
for i in to_fill:
    to_fill[i].sort(key=lambda b: b[1], reverse=True)

temp = 'Q----B'
removed = []
for b in range(len(temp)):
    if temp[b] != '-':
        removed.append((temp[b], b))
        temp = temp[0:b] + '-' + temp[b + 1:]
    if temp.count('-') == len(temp) - 1:
        break
check = {*to_fill[temp]}
ensure = False
for rem in removed:
    combine=[]
    st = (rem[1])*'-'+rem[0]+'-'*(len(temp)-rem[1]-1)
    if st in to_fill:
        for u in to_fill[st]:
            if u in check:
                combine.append(u)
                ensure = True
    else:
        print(None)
    if not ensure:
        print(None)
    check = {*combine}
    ensure = False
print(combine)
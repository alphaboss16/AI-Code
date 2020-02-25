f = open('pcgabor_edax_formatted.txt')
k = f.readlines()
z = open('fixedo.txt', 'w+')
final = []
count = 0
fix = {}
for i in range(0, 10):
    for j in range(0, 10):
        b = i * 10 + j
        a = b // 10
        if a > 8 or a < 1:
            continue
        c = b % 10
        if c > 8 or c < 1:
            continue
        fix[count] = b
        count += 1
rev = {}
for i in fix:
    rev[fix[i]] = i

for i in range(1, len(k) - 1):
    b = k[i].split()
    if b[1] == 'o':
        board = (''.join([x for x in [*b[0]] if x != '?'])).replace('@', 'x')
        move = rev[int(k[i + 1].split()[-1])]
        final.append('\'{}\': {},\n'.format(board, move))
z.writelines(final)
z.close()
f.close()

f = open('dctLarge.txt', 'r+')
alphabet = [*'abcdefghijklmnopqrstuvwxyz']
freqs={x:0 for x in alphabet}
m = f.readlines()
for i in m:
    word = i.lower()
    for j in alphabet:
        freqs[j]+=word.count(j)
k = list(freqs.keys())
k.sort(key=lambda b: freqs[b], reverse=True)
print(k)
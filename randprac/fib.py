import sys
global cache 
cache = {1:1, 2:1}

for i in range(3, int(sys.argv[1])+1):
    cache[i]=cache[i-1]+cache[i-2]
def fib(i):
    global cache
    if i < 4:
        return i-(i>1)
    elif i in cache:
        return cache[i]
    else:
        cache[i]=fib(i-2)+fib(i-1)
        return cache[i]
print(fib(int(sys.argv[1])))

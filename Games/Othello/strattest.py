from Strategy import *

class k():
    def __init__(self):
        self.value=-1
m = k()
b = Strategy()
b.best_strategy('.' * 27 + "ox......xo" + '.' * 27, '@', m)
print(m.value)
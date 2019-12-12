import sys
brd, bL = sys.argv[1], len(sys.argv[1])
w=int(sys.argv[2]) if len(sys.argv)>2 else bL
xforms = {brd, ''.join([brd[r:r+2][::-1] for r in range(0, bL, w)])}
for b in [*xforms]: xforms.add(''.join(b[c::w] for c in range(w)))
for b in [*xforms]: xforms.add(b[::-1])
for b in [*xforms]: print(b)
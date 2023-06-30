from sys import *
import hashlib
from z3 import *

LEN = 37 
s = Solver()
a1 = [BitVec(i, 8) for i in range(LEN)]

# ========================================
for i in range(LEN):
    s.add(0x20 < a1[i])
    s.add(0x7f > a1[i])

# alphanumeric
for i in range(len(s)):
    solver.add(Or(And(s[i] >= '0', s[i] <= '9'), And(s[i] >= 'a', s[i] <= 'z'), And(s[i] >= 'A', s[i] <= 'Z')))

    
# comparison
s.add(a1[3] == a1[8])


# ========================================

while True:
    www = s.check()    
    model = s.model()
    manga = [0 for i in range(LEN)]
    for i in range(LEN):
        index = eval(str(model[i])[2:])
        manga[index] = eval(str(model[model[i]]))
    
    b = "".join([chr(manga[i]) for i in range(LEN)])
    print(b)

    # true conditions
    print(hashlib.md5(str.encode(b)).hexdigest(), "b7575a9d0a6bc912480b28ef3597c444")
    if hashlib.md5(str.encode(b)).hexdigest() == "b7575a9d0a6bc912480b28ef3597c444" :
        print(b)
        exit(1)
        break


    # add different candidate
    ev = "Or("
    for j in range(LEN):
        ev += "a1[{}] != {} , ".format(j, manga[j])
    ev = ev[:-2]
    ev += ")"
    exec("s.add({})".format(ev))
    

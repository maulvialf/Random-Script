from sys import *
import hashlib
from z3 import *

LEN = 37 
s = Solver()
a1 = [BitVec(i, 8) for i in range(LEN)]

# ========================================
for i in range(37):
    s.add(0x20 < a1[i])
    s.add(0x7f > a1[i])

# comparison
s.add(a1[3] == a1[8])


# ========================================

while True:
    www = s.check()    
    model = s.model()
    manga = [0 for i in range(37)]
    for i in range(37):
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
        ev += "a1[{}] != {} , ".format(i, manga[i])
    ev = ev[:-2]
    ev += ")"
    exec("s.add({})".format(ev))
    
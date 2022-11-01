from collections import defaultdict
from collections import deque
from pprint import pprint as pp
import sys

# helper function
def printnoline(string):
	sys.stdout.write(string)


"""
should modify this depends on the map
"""
def parsemap(peta):
	petaline = peta.split("\n")
	leny = len(petaline)
	lenx = len(list(petaline[0]))
	petab = [[0 for i in range(lenx)] for i in range(leny)]
	yy = 0
	for petax in petaline:
		xx = 0
		for p in petax:
			# allow
			if(p == "~"):
				petab[yy][xx] = 0
			# block
			elif(p == "*"):
				petab[yy][xx] = 1
			# player
			elif(p == "h"):
				petab[yy][xx] = 2
			# target
			elif(p == "u"):
				petab[yy][xx] = 3
			xx += 1
		yy += 1

	return petab, lenx, leny

def printmap(peta):
	for y in range(leny):
		for x in range(lenx):
			printnoline(str(peta[y][x]))
		print()

def convertmove(move):
	moveset = 0
	if(move == "a"):
		moveset = (-1, 0)
	elif(move == "s"):
		moveset = (0, 1)
	elif(move == "d"):
		moveset = (1, 0)
	elif(move == "w"):
		moveset = (0, -1)
	return moveset

def jalanpair(move, petax, koordinathero, deadend):

	x, y = koordinathero
	movex, movey = convertmove(move)
	if(x + movex < 0):
		return (petax, 0, koordinathero)

	elif(x + movex > lenx - 1):
		return (petax, 0, koordinathero)

	elif(y + movey < 0):
		return (petax, 0, koordinathero)

	elif(y + movey > leny - 1):
		return (petax, 0, koordinathero)

	elif(petax[y + movey][x + movex] == 3):
		return (petax, 2, koordinathero)

	elif(petax[y + movey][x + movex] == 0):
		newpeta = petax.copy()		
		newpeta[y][x] = 4
		newpeta[y+movey][x+movex] = 2
		return (newpeta, 1, (x + movex, y + movey))
	else:
		return (petax, 0, koordinathero)

def getplayer(peta):
	for y in range(leny):
		for x in range(lenx):
			if(peta[y][x] == 2):
				return (x, y)

	return -1

peta = """\
h*~~~*~*~*~~**~~~~*
~~~~~**~~~*~~*~~~*~
~~~**~~**~~*~~~~*~*
~~****~~*~~~~*~**~~
~~**~~~~~~~~~~~*~~*
~~~~~~~~***~~~*~~*~
~~***~~~~**~~~*~~~~
~~*~*~*~~~~*~~~*~~~
*~~*~*~~~~*~~~~~~*~
*~*~~~~~~~~~~*~~~*~
*~*~~~~~~**~/bin/su\
"""

petab, lenx, leny = parsemap(peta)
koordinathero = getplayer(petab)
assert koordinathero != -1

kotak = deque()
kotakx = ["a", "s", "w", "d"]

for x in kotakx:
	kotak.append(("", x, [koordinathero], petab, koordinathero))

while kotak:
	u = kotak.popleft()
	curr     = u[0]
	move     = u[1]
	deadend  = u[2]
	petabx   = u[3]
	koordinathero   = u[4]
	oldkoordinathero = koordinathero
	newpetab, status, koordinathero = jalanpair(move, petabx, oldkoordinathero, deadend)

	if(status == 2):
		print("gotflag")
		print(curr + move)
		break
	elif(status == 0):
		continue
	elif(koordinathero in deadend):
		continue
	else:	
		printmap(newpetab)
		print()		
		newdeadend = deadend.copy()
		newdeadend.append(koordinathero)
		for x in kotakx:
			kotak.append((curr + move, x, newdeadend, newpetab, koordinathero))

from collections import defaultdict
from collections import deque
from pprint import pprint as pp
import sys

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

move = ["a", "s", "d", "w"]

petaline = peta.split("\n")

leny = len(petaline)
lenx = len(list(petaline[0]))
petab = [[0 for i in range(lenx)] for i in range(leny)]

yy = 0
for petax in petaline:
	xx = 0
	for p in petax:
		petab[yy][xx] = p
		xx += 1
	yy += 1

def printnoline(string):
	sys.stdout.write(string)


def printmap(peta):
	for y in range(leny):
		for x in range(lenx):
			printnoline(peta[y][x])
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

	elif(petax[y + movey][x + movex] == "u"):
		return (petax, 2, koordinathero)

	elif(petax[y + movey][x + movex] == "~"):
		newpeta = petax.copy()		
		newpeta[y][x] = "."
		newpeta[y+movey][x+movex] = "h"
		return (newpeta, 1, (x + movex, y + movey))
	else:
		return (petax, 0, koordinathero)

def getplayer(peta):
	for y in range(leny):
		for x in range(lenx):
			if(peta[y][x] == 'h'):
				return (x, y)

	return -1

koordinathero = getplayer(petab)

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
		newdeadend = deadend.copy()
		newdeadend.append(koordinathero)
		for x in kotakx:
			kotak.append((curr + move, x, newdeadend, newpetab, koordinathero))

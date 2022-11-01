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
	peta2ds = peta.split("\n\n\n")
	lenz  = len(peta2ds) - 1
	leny  = len(peta2ds[0].split("\n"))
	lenx  = len(list(peta2ds[0].split("\n")))
	petab = [[[0 for i in range(lenx)] for i in range(leny)]  for i in range(lenz)]
	zz 	  = -1
	for peta2d in peta2ds:
		zz += 1
		petaline = peta2d.split("\n")
		yy = -1
		for petax in petaline:
			yy += 1
			xx = -1
			for p in petax:
				xx += 1
				# print(zz, yy, xx)				
				# allow
				if(p == "~"):
					petab[zz][yy][xx] = 0
				# block
				elif(p == "#"):
					petab[zz][yy][xx] = 1
				# player
				elif(p == "A"):
					petab[zz][yy][xx] = 2
				# target
				elif(p == "H"):
					petab[zz][yy][xx] = 3

	return petab, lenx, leny, lenz

def printmap(peta):
	for z in range(lenz):
		for y in range(leny):
			for x in range(lenx):
				printnoline(str(peta[z][y][x]))
			print()
		print()

def convertmove(move):
	moveset = 0
	if(move == "a"):
		moveset = (-1, 0, 0)
	elif(move == "s"):
		moveset = (0, 1, 0)
	elif(move == "d"):
		moveset = (1, 0, 0)
	elif(move == "w"):
		moveset = (0, -1, 0)
	elif(move == "r"):
		moveset = (0, 0, 1)
	elif(move == "f"):
		moveset = (0, 0, -1)
	return moveset

def jalanpair(move, petax, koordinathero, deadend):
	x, y, z = koordinathero
	movex, movey, movez = convertmove(move)
	if(x + movex < 0):
		return (petax, 0, koordinathero)

	elif(x + movex > lenx - 1):
		return (petax, 0, koordinathero)

	elif(y + movey < 0):
		return (petax, 0, koordinathero)

	elif(y + movey > leny - 1):
		return (petax, 0, koordinathero)

	elif(z + movez < 0):
		return (petax, 0, koordinathero)

	elif(z + movez > lenz - 1):
		return (petax, 0, koordinathero)


	elif(petax[z + movez][y + movey][x + movex] == 3):
		return (petax, 2, koordinathero)

	elif(petax[z + movez][y + movey][x + movex] == 0):
		newpeta = petax.copy()		
		newpeta[z][y][x] = 4
		newpeta[z+movez][y+movey][x+movex] = 2
		return (newpeta, 1, (x + movex, y + movey, z + movez))
	else:
		return (petax, 0, koordinathero)

def getplayer(peta):
	for z in range(lenz):
		for y in range(leny):
			for x in range(lenx):
				if(peta[z][y][x] == 2):
					return (x, y, z)

	return -1

peta = open("peta3d.map").read()

petab, lenx, leny, lenz = parsemap(peta)
# printmap(petab)
koordinathero = getplayer(petab)
assert koordinathero != -1

kotak = deque()
kotakx = ["a", "s", "w", "d", "f", "r"]

# newset
# f z + 1
# r z - 1

for x in kotakx:
	kotak.append(("", x, [koordinathero], petab, koordinathero, 0))

while kotak:
	u = kotak.popleft()
	curr     = u[0]
	move     = u[1]
	deadend  = u[2]
	petabx   = u[3]
	koordinathero   = u[4]
	distance   = u[5]
	oldkoordinathero = koordinathero
	newpetab, status, koordinathero = jalanpair(move, petabx, oldkoordinathero, deadend)
	if(status == 2):
		print(curr+move)
		print("gotflag")
		print("move", curr + move)
		print("distance", distance + 1)
		break
	elif(status == 0):
		continue
	elif(koordinathero in deadend):
		continue
	else:	
		newdeadend = deadend.copy()
		newdeadend.append(koordinathero)
		for x in kotakx:
			kotak.append((curr + move, x, newdeadend, newpetab, koordinathero, distance+1))

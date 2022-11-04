import gdb

def extract_mem(parammem):
	'''
	0x7fffffffda54:	0x0000000000010441
	0x010441
	'''
	raw = gdb.execute("x/gx {}".format(parammem), False, True)
	parammem = gdb.parse_and_eval("{}".format(parammem))
	print('raw', raw)
	print('parammem', parammem)
	extract = raw.split("{}:".format(parammem))[1].strip()
	extractval = eval(extract)
	print('extract', hex(extractval))
	return extractval

mem1 = extract_mem("$rbp")
mem2 = extract_mem("0x7fffffff00000")
reg1 = gdb.parse_and_eval("$eax")

# init file
gdb.execute('file a')

# run with arg
gdb.execute('r {}'.format("A" * 10))

# input with stdin
inp = "A" * 10
open('inp.temp', 'w').write(inp)
gdb.execute('r<inp.temp')

# execute cmd no return
gdb.execute("set $eax={}".format(hasil))


# execute cmd no return
output = gdb.execute("info reg", False, True)

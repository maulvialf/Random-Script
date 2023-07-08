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

# Function to extract memory using GDB
def extract_memory(address, num_bytes):
    # Run GDB in non-interactive mode
    # gdb.execute("set pagination off")
    # gdb.execute("set logging on")

    # Execute the x/16bx command to extract memory
    gdb_output = gdb.execute("x/{}bx {}".format(num_bytes, address), to_string=True)

    # Parse the GDB output to extract the bytes
    byte_array = []
    lines = gdb_output.strip().split("\n")
    for line in lines:
        byte_str = line.split(":")[1].strip()
        byte_str = byte_str.replace("0x", "")
        byte_str = byte_str.replace("\t", "")
        byte = int(byte_str, 16)
        byte_array.append(byte)

    # Save the output to a log file
    # gdb.execute("quit", to_string=True)

    return byte_array

data = extract_memory(0x555555559483, 1)

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

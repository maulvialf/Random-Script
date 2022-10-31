#!/usr/bin/python2
import sys
import os
import subprocess

program = sys.argv[1]
bit = os.popen('file {}'.format(program)).read()
ida = "/home/user/ida"
if '32-bit' in bit or 'PE32' in bit:
    cmd = "(wine {}/ida.exe {})> /dev/null 2>&1 &".format(ida, program)
else:
    cmd = "(wine {}/ida64.exe {})> /dev/null 2>&1 &".format(ida, program)


solver = '''#!/usr/bin/python2
from pwn import *
from sys import *

context.arch = "amd64"
# context.arch = "i386"
# context.log_level = 'DEBUG'

#libc = ELF('libc.so.6', checksec=False)
#libc = ELF('/usr/lib32/libc.so.6')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=False)       


e = ELF('{}')
elfROP = ROP(e)

if(len(argv) == 2):
    p = connect("localhost", 9090)
else:
    p = process('{}')
    # p = gdb.debug('{}', cmd)


cmd = """
"""
if(len(argv) == 3):
    gdb.attach(p, cmd)

p.interactive()

'''.format(program, program, program)

if(os.path.isfile("solve.py")):
    print "already exists"

else:
    open("solve.py", "wb").write(solver)
    os.system("chmod +x solve.py")
    os.system("subl "+"solve.py")

os.system(cmd)

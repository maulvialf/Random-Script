from sys import exit
shellcode = [0x80, 0x80]


# print   'asm("nop");\n' * 3000
# print len(shellcode)


data = open("a.out").read()

for i in range(len(data)):
  if(data[i:i+8] == "\x90" * 8):
    break
print i
data2 = list(data)
x = 0
for j in range(i, i+len(shellcode)):
  data2[j] = chr(shellcode[x])
  x += 1

simpan = "".join(data2)  

open("patched", "w").write(simpan)

# bac= open("b").read()
# kom = open("a").read()
def mux(asli, key):
	hasil = ""
	# print len(asli), len(key)
	pan = len(key)
	for i in range(len(asli)):

		ch = chr(ord(asli[i]) ^ ord(key[i]))
		# print ch,
		if ch not in "abcdefghijklmnopqrstuvwxyz ":
			# print ch
			return 0
		hasil += ch
		# print hasil
	return hasil

# bac = mux(bac, kom)
c1 = '38445d4e5311544249005351535f005d5d0c575b5e4f481155504e495740145f4c505c5c0e196044454817564d4e12515a5f4f12465c4a45431245430050154b4d4d415c560c4f54144440415f595845494c125953575513454e11525e484550424941595b5a4b'
c2 = '3343464b415550424b415551454b00405b4553135e5f00455f540c535750464954154a5852505a4b00455f5458004b5f430c575b58550c4e5444545e0056405d5f53101055404155145d5f0053565f59524c54574f46416c5854416e525e11506f485206554e51'
# for line in data:
# crypt = crypt.decode('hex')
#user@lithium:~/alexctf/cr2$ #used cribdrag.py 
c1 = c1.decode('hex')
c2 = c2.decode('hex')
key = 'e of plaintext used in codebreaking'
# key = "flag is easyctf{otp_ttp"
flag = "3, 244, 67, 182, 213, 111, 20, 224, "
# km = len(key)
# print mux(c1[68:68+len(key)], key)
# print mux(c1, flag)
mungkin = "1234567890, "
mungkin2 = "1234567890"

for l in mungkin2:
	for m in mungkin2:
		for x in mungkin2:
			for k in mungkin2:
				for i in mungkin2:
					# sem = flag + i+ k + x + "," + " " +  m
					sem = flag + i+ k  + ", " + x + m + ", " + l
					# sem = flag + i+ k  + ", " + x + m + l + ", "
					h = len("a")
					a = mux(c1[68+h:68+len(sem)], sem[h:])
					# print sem
					if a != 0:
						print sem, key+a
# for i in range(len(c1)):
	# print i, mux(c1[i:i+len(flag)], flag)
# for i in range(len(bac)):
	# print mux(bac[i:i+km], key)

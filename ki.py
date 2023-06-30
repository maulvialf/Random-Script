def reversecipher(setring):
    return setring[::-1]

def caesar_enhanced(setring, key):
    result = ""
    # transverse plain text
    for i in range(len(setring)):
        char = setring[i]
        # Encrypt digit (0-9)
        if(char.isdigit()):
            result += chr((ord(char) + key -  ord('0') ) % 10 + ord('0'))
        # Encrypt huruf kapital (A-Z)
        elif (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        # Encrypt huruf kecil (a-z)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

def break_caesar(setring):
    for i in range(26):
        cipher = caesar_enhanced(setring,i)
        print (i, cipher)

break_caesar("GIEWIVrGMTLIVrHIQS")

# transposition
def split_len(seq, length):
	return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
	order = {int(val): num for num, val in enumerate(key)}
	ciphertext = " "
	for index in sorted(order.keys()):
		for part in split_len(plaintext, len(key)):
			try:
				ciphertext += part[order[index]]
			except IndexError:
				continue
	return ciphertext

print(encode('3214', 'HELLOHELLO')) 

# des

import pyDes
data ="Impementasi Algoritma DES yang belum beres"
k = pyDes.des("IniKunci", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None,
padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)
print ("Encrypted: %r" % d)
print ("Decrypted: %r" % k.decrypt(d))
print (k.decrypt(d).decode('utf-8') == data) #memeriksa apakah dekripsi benar 




from Crypto.Cipher import Salsa20

def encrypt_message(key, nonce, message):
    cipher = Salsa20.new(key=key, nonce=nonce)
    encrypted_message = cipher.encrypt(message)
    return encrypted_message

def decrypt_message(key, nonce, encrypted_message):
    cipher = Salsa20.new(key=key, nonce=nonce)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message

# Example usage
key = b'This is a 32-byte key for Salsa2'
nonce = b'This isf'
message = b'Hello, World!'

encrypted = encrypt_message(key, nonce, message)
print("Encrypted:", encrypted)

decrypted = decrypt_message(key, nonce, encrypted)
print("Decrypted:", decrypted.decode())

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate AES key
key = get_random_bytes(16)  # AES requires 16, 24, or 32 bytes key
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt data
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(b"Sensitive Data")

# Decrypt data
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)
print(f"Decrypted Text: {plaintext.decode()}")

from cryptography.fernet import Fernet

# Generate key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt some text
text = "Sensitive Data"
encrypted_text = cipher_suite.encrypt(text.encode())
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the encrypted text
decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
print(f"Decrypted Text: {decrypted_text}")

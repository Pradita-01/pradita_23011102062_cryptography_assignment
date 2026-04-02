from cipher import encrypt, decrypt
from hash import polynomial_hash

# Example 1
text1 = "HELLO"
key1 = 7

cipher1 = encrypt(text1, key1)
hash1 = polynomial_hash(cipher1)
original1 = decrypt(cipher1, key1)

print("Example 1")
print("Plaintext:", text1)
print("Key:", key1)
print("Ciphertext:", cipher1)
print("Hash:", hash1)
print("Decrypted:", original1)

print("\n------------------\n")

# Example 2
text2 = "WORLD"
key2 = 7

cipher2 = encrypt(text2, key2)
hash2 = polynomial_hash(cipher2)
original2 = decrypt(cipher2, key2)

print("Example 2")
print("Plaintext:", text2)
print("Key:", key2)
print("Ciphertext:", cipher2)
print("Hash:", hash2)
print("Decrypted:", original2)

text3 = "car"
key3 = 7

cipher3 = encrypt(text3, key3)
hash3 = polynomial_hash(cipher3)
original3 = decrypt(cipher3, key3)

print("Example 3")
print("Plaintext:", text3)
print("Key:", key3)
print("Ciphertext:", cipher3)
print("Hash:", hash3)
print("Decrypted:", original3)
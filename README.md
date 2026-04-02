# pradita_23011102062_cryptography_assignment
cyrptography _assignment [Multiplicative cipher]
# Cryptography Assignment

## Overview

This project implements a Multiplicative Cipher for encryption and decryption, along with a custom Polynomial Rolling Hash function. It also demonstrates a complete workflow:

Encrypt → Hash → Decrypt

---

## 1. Multiplicative Cipher (Theory)

The Multiplicative Cipher is a substitution cipher in which each letter of the plaintext is mapped to a number and multiplied by a key modulo 26.

### Key Concepts

* Alphabet mapping:

  * A = 0, B = 1, ..., Z = 25
* The key must be coprime with 26 (i.e., gcd(key, 26) = 1)
* Valid keys include: 3, 5, 7, 11, 17, etc.

### Encryption Formula

C = (P × K) mod 26 [where p stands for plain text , k stands for key and c stands for cipher text]

Where:

* P = plaintext value
* K = key
* C = ciphertext value

### Decryption Formula

P = (C × K⁻¹) mod 26

Where:

* K⁻¹ is the modular multiplicative inverse of K such that:

  K × K⁻¹ ≡ 1 (mod 26)

---

## 2. Cipher Implementation (cipher.py)

The cipher is implemented using two main functions: `encrypt` and `decrypt`.

### encrypt(plain_text, key)

This function takes a plaintext string and a key as input and returns the encrypted ciphertext.

#### Steps:

1. Initialize an empty string for the ciphertext.
2. Iterate through each character in the plaintext.
3. If the character is alphabetic:

   * Convert it to uppercase.

   * Convert the character to its numeric value using:

     ord(char) - ord('A') [ the ASCII value of the character -  ASCII value of the letter A]

   * Apply the multiplicative cipher formula:

     (value × key) mod 26

   * Convert the result back to a character using:

     chr(result + ord('A')) [ ASCII  value of the resultant character + The ASCII value of character A]
4. If the character is not alphabetic, it is left unchanged.
5. Return the final ciphertext.

---

### decrypt(cipher_text, key)

This function takes ciphertext and a key as input and returns the original plaintext.

#### Steps:

1. Compute the modular multiplicative inverse of the key using:

   pow(key, -1, 26)

2. Initialize an empty string for the plaintext.

3. Iterate through each character in the ciphertext.

4. If the character is alphabetic:

   * Convert it to uppercase.

   * Convert it to its numeric value.

   * Apply the decryption formula:

     (value × key_inverse) mod 26

   * Convert the result back to a character.

5. Non-alphabetic characters are left unchanged.

6. Return the decrypted plaintext.

---

## 3. Hash Function (hash.py)

A Polynomial Rolling Hash function is used to generate a numeric hash for a given string.

### Formula

hash = (hash × base + ASCII value) mod m

Where:

* base = 31
* m = 1,000,000,007 (a large prime number)

### Implementation Logic

1. Initialize `hash_value = 0`.
2. For each character in the input string:

   * Multiply the current hash by 31.
   * Add the ASCII value of the character using `ord(char)`.
   * Take modulo 1,000,000,007 to keep the value within limits.
3. Return the final hash value.

### Reason for Choosing This Hash

* Simple to implement from scratch
* Efficient for string processing
* Produces good distribution of values
* Reduces collisions compared to basic hashing methods

---

## 4. Test Script (test.py)

The test script demonstrates the complete workflow:

Encrypt → Hash → Decrypt

### Steps Performed

1. Define plaintext and key.
2. Encrypt the plaintext using the multiplicative cipher.
3. Compute the hash of the ciphertext.
4. Decrypt the ciphertext back to the original plaintext.
5. Print all values:

   * Plaintext
   * Key
   * Ciphertext
   * Hash
   * Decrypted text

---

## 5. Example Outputs

### Example 1

Plaintext: HELLO
Key: 7
Ciphertext: XCZZU
Hash: 83355210
Decrypted: HELLO

---

### Example 2

Plaintext: WORLD
Key: 7
Ciphertext: YUPZV
Hash: 84805360
Decrypted: WORLD

---

### Example 3

Plaintext: CAR
Key: 7
Ciphertext: OAP
Hash: 78014
Decrypted: CAR

---

## 6. How to Run the Project

1. Ensure Python (version 3.8 or above) is installed.
2. Place all files in the same directory:

   * cipher.py
   * hash.py
   * test.py
3. Open a terminal in that directory.
4. Run the following command:

python test.py

5. The output will display encryption, hash, and decryption results.

---

## 7. Notes

* The key must be coprime with 26 for decryption to work correctly.
* The modular inverse is calculated using Python’s built-in `pow()` function.
* All alphabetic characters are converted to uppercase for consistency.
* Valid keys : 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
* Invalid keys: 2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24
* When we say that the key is not valid it means there is no modular inverse for the key and hence decryption will fail
*  Non-alphabetic characters are preserved during encryption and decryption.

---

## Conclusion

This project demonstrates the implementation of a classical encryption technique along with a custom hashing function. It showcases how mathematical concepts such as modular arithmetic and hashing can be applied to ensure data transformation and integrity.


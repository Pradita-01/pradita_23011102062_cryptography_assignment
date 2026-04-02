def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            char = char.upper()
            encrypted_char = chr(((ord(char) - ord('A')) * key) % 26 + ord('A'))
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    
    # Modular inverse using Python built-in
    key_inverse = pow(key, -1, 26)

    for char in cipher_text:
        if char.isalpha():
            char = char.upper()
            decrypted_char = chr(((ord(char) - ord('A')) * key_inverse) % 26 + ord('A'))
            plain_text += decrypted_char
        else:
            plain_text += char
    return plain_text
def polynomial_hash(text):
    base = 31
    mod = 1000000007
    hash_value = 0

    for char in text:
        value = ord(char)
        hash_value = (hash_value * base + value) % mod

    return hash_value
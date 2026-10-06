# Hill Cipher - 2x2 Matrix

import numpy as np


def encrypt(text, key):
    text = text.upper().replace(" ", "")

    # Add X if length is odd
    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        pair = [
            ord(text[i]) - ord('A'),
            ord(text[i + 1]) - ord('A')
        ]

        encrypted = np.dot(key, pair) % 26

        result += chr(encrypted[0] + ord('A'))
        result += chr(encrypted[1] + ord('A'))

    return result


plaintext = input("Enter plaintext: ")

# Key matrix
key = np.array([
    [3, 3],
    [2, 5]
])

ciphertext = encrypt(plaintext, key)

print("Key Matrix:")
print(key)

print("Encrypted text:", ciphertext)
# Monoalphabetic Cipher

import string

# Plain alphabet
alphabet = string.ascii_uppercase

# Substitution key
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def encrypt(text):
    result = ""

    for char in text.upper():
        if char in alphabet:
            index = alphabet.index(char)
            result += key[index]
        else:
            result += char

    return result


def decrypt(text):
    result = ""

    for char in text.upper():
        if char in key:
            index = key.index(char)
            result += alphabet[index]
        else:
            result += char

    return result


# Input
plaintext = input("Enter plaintext: ")

# Encryption
ciphertext = encrypt(plaintext)
print("Encrypted text:", ciphertext)

# Decryption
decrypted_text = decrypt(ciphertext)
print("Decrypted text:", decrypted_text)
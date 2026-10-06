# Polyalphabetic Cipher - Vigenere Cipher

def encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += char

    return result


plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = encrypt(plaintext, key)
print("Encrypted text:", ciphertext)

print("Decrypted text:", decrypt(ciphertext, key))
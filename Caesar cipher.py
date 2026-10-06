# Caesar Cipher

def encrypt(text, shift):
    result = ""

    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char

    return result


plaintext = input("Enter plaintext: ")
shift = int(input("Enter shift value: "))

ciphertext = encrypt(plaintext, shift)
print("Encrypted text:", ciphertext)

print("Decrypted text:", decrypt(ciphertext, shift))
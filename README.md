# Basic Cryptography Techniques

This project contains simple Python implementations of several classical encryption algorithms used for learning and demonstration purposes.

## Included Ciphers

- Caesar Cipher
- Monoalphabetic Cipher
- Playfair Cipher
- Hill Cipher (2x2 matrix)
- Polyalphabetic Cipher (Vigenere Cipher)

## Project Files

- `Caesar cipher.py` — Implements the Caesar shift cipher for encryption and decryption.
- `Monoalphabetic Cipher.py` — Uses a fixed substitution alphabet for encryption and decryption.
- `Playfair cipher.py` — Implements the Playfair cipher with key matrix creation and text preparation.
- `Hill Cipher.py` — Performs a 2x2 Hill cipher encryption using a matrix key.
- `Polyalphabetic Cipher.py` — Implements the Vigenere cipher using a repeating keyword.

## Requirements

- Python 3.x
- NumPy (required for the Hill cipher implementation)

Install NumPy using:

```bash
pip install numpy
```

## How to Run

Open a terminal in the project folder and run any script directly with Python:

```bash
python "Caesar cipher.py"
python "Monoalphabetic Cipher.py"
python "Playfair cipher.py"
python "Hill Cipher.py"
python "Polyalphabetic Cipher.py"
```

## Example Usage

### Caesar Cipher
- Enter the plaintext.
- Enter the shift value.
- The script prints the encrypted and decrypted text.

### Monoalphabetic Cipher
- Enter the plaintext.
- The script uses a predefined substitution key.

### Playfair Cipher
- Enter a keyword.
- Enter the plaintext.
- The program creates a 5x5 matrix and encrypts/decrypts the text.

### Hill Cipher
- Enter the plaintext.
- The script uses a fixed 2x2 key matrix.
- The plaintext is processed in pairs of letters.

### Polyalphabetic Cipher (Vigenere)
- Enter the plaintext.
- Enter the encryption key.
- The key is repeated across the text to shift each letter.

## Notes

This repository is intended for educational purposes to understand how classical ciphers work conceptually and programmatically. These implementations are not intended for production-grade security.

## License

This project is provided for learning and academic use.

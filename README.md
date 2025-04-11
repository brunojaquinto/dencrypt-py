# Dencrypt
Dencrypt is a simple file encryption/decryption tool built in Python, using the `cryptography` library Fernet.
(for personal learning and practice purposes)


# Features
- Generate a secure encryption key
- Encrypt files locally
- Decrypt previously encrypted files


# How to Use
1. Generate a Key

```bash
python3 generate_key.py
```
A file named key.key will be created.

```bash
python3 dencrypt.py
```
- Choose option
- Specify the file
- The file will be saved with _e or _d suffix

# Requirements
- Python 3.6+
- cryptography library

# Secure Vault Password Manager

A simple, local password manager written in Python for educational purposes. It allows you to generate, store, and manage your credentials using a Vigenere-based encryption with a master password.

## Features
- **Secure Login**: Access your vault using a Master Password.
- **Key Derivation**: Uses `SHA-256` hashing to generate a strong encryption key from your master password.
- **Generate & Save**: Automatically generates random passwords with letters, digits, and special characters.
- **Encryption**: Encrypts stored passwords using a Vigenere cipher (Unicode-safe).
- **Manage Entries**: View all saved credentials or delete specific ones by index.

## Project Structure
- `main.py`: The entry point of the application.
- `vigenere.py`: Contains the logic for encryption and decryption.
- `generate_key.py`: Handles key derivation using `hashlib`.
- `show_menu.py`: Handles UI/Menu display.


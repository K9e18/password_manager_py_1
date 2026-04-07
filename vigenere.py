def encrypt(plain_text, key):
    final_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = key[i % len(key)]

        encrypted_char = chr((ord(char) + ord(key_char)) % 256)
        final_text += encrypted_char

    return final_text

def decrypt(cipher_text, key):
    final_text = ""
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        key_char = key[i % len(key)]

        decrypted_char = chr((ord(char) - ord(key_char)) % 256)
        final_text += decrypted_char

    return final_text
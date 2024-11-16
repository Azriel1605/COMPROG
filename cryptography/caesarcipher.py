def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

text = "Hello, World!"
shift = 1

# Encrypt the text
encrypted_text = encrypt(text, shift)
print("Encrypted:", encrypted_text)

# Decrypt the text
decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted:", decrypted_text)

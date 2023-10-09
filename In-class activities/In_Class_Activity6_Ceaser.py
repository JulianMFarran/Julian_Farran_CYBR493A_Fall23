# Store the alphabet in a variable named alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Store the encryption key as 4
encryption_key = 4

# Store a message to encrypt
message = "radar"

# Initialize an empty string for the encrypted message
encrypted_message = ""


# Function to encrypt a character using Caesar Cipher
def encrypt_char(char, key):
    if char.isalpha():
        is_upper = char.isupper()
        char = char.lower()
        encrypted_index = (alphabet.index(char) + key) % 26
        encrypted_char = alphabet[encrypted_index]
        return encrypted_char.upper() if is_upper else encrypted_char
    return char


# Encrypt the message character by character
for char in message:
    encrypted_message += encrypt_char(char, encryption_key)

# Print the original message and the encrypted message
print("Original Message:", message, "Encrypted Message:", encrypted_message)

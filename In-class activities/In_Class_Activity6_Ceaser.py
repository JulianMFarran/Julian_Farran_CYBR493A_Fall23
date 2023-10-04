# Store the alphabet in a variable named alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Store the encryption key 4 as of right now.
encryption_key = 4

# Store a message to encrypt (You can put anything here even Zebra -> Difve, it works)
message = "Julian Farran"

# Initialize an empty string for the encrypted message.
encrypted_message = ""

# Create a dictionary to map characters to their indices
#Instead of repeatedly searching for the index of a character in the alphabet string,
# We should simply create a dictionary that maps each letter to its index.
# This will improve the lookup efficiency.
# (This will allow quick lookup of a character's index when needed in the encryption process.)
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Time to Encrypt the message, and handle the wrap around for encryption and handle uppercase and lowercase letters.
for char in message:
    if char.isalpha():  # Check if the character is a letter or not
        char_index = char_to_index[char.lower()]  # Find the position of the character in the alphabet
        encrypted_index = (char_index + encryption_key) % 26  # Apply the Caesar Cipher logic with the wraparound
        encrypted_char = alphabet[encrypted_index]  # Get the encrypted character
        # Preserve the original case of the character so that it reads back correct.
        if char.isupper():
            encrypted_char = encrypted_char.upper()
        encrypted_message += encrypted_char  # Append it to the result
    else:
        encrypted_message += char  # If it's not a letter, keep it unchanged

# Print the original message and then print the encrypted message below
print("Original Message:", message)
print("Encrypted Message:", encrypted_message)

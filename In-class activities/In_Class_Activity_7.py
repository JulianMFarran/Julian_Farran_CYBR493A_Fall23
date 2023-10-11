# Caesar cipher encryption function / Key is provided by the USER.
# The last time I did In_Class_Activity6_Ceaser I hardcoded the key.
# This new and improved version allows the user to pick what the key is at runtime.
def caesar_cipher(text, key):
    # Initialize an empty string to store the encrypted result
    encrypted_text = ""

    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an alphabetic character
        if char.isalpha():
            # Remember the case (uppercase or lowercase)
            is_upper = char.isupper()

            # Convert the character to lowercase to perform the encryption
            char = char.lower()

            # Calculate the new character position in the alphabet
            shifted = (ord(char) - ord('a') + key) % 26

            # Convert the shifted character back to its ASCII representation and then to a character
            encrypted_char = chr(shifted + ord('a'))

            # If the original character was uppercase, convert the shifted character to uppercase
            if is_upper:
                encrypted_char = encrypted_char.upper()

            # Append the shifted character to the encrypted_text
            encrypted_text += encrypted_char
        else:
            # If the character is not alphabetic, append it unchanged to the encrypted_text
            encrypted_text += char

    # Return the encrypted text
    return encrypted_text

# Main function
def main():
    # Prompt the user to enter the text to be encrypted
    user_text = input("Enter the text you want to encrypt: ")

    # Prompt the user to enter the encryption key (an integer)
    key = int(input("Enter the key (an integer): "))

    # Call the caesar_cipher function to encrypt the user's input
    encrypted_text = caesar_cipher(user_text, key)

    # Print the encrypted text to the console
    print("Encrypted text: " + encrypted_text)

if __name__ == "__main__":
    main()

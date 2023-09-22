# Julian Farran
# HW #2
# 9/22/2023
# CYBR 493A

# Method to check if the password is at least 8 characters long
def ValidLength(password):
    return len(password) >= 8

# Method to check if the password contains at least one digit
def HasNumber(password):
    for char in password:
        if char.isdigit():
            return True
    return False

# Method to check if the password contains at least one of the specified symbols
def HasSymbol(password):
    symbols = set(['%', '!', '@', '#', '$', '%', '&', '*'])
    for char in password:
        if char in symbols:
            return True
    return False




# Importing the methods from HW2.py
from HW2 import ValidLength, HasNumber, HasSymbol

def main():
    password = input("Give me a password to check: ")

    if ValidLength(password) and HasNumber(password) and HasSymbol(password):
        print("Valid Password")
    else:
        print("Invalid Password")

if __name__ == "__main__":
    main()

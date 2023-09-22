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



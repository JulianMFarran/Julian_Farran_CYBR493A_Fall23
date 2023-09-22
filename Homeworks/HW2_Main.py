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

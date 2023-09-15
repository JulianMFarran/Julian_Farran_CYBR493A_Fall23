def WordsChecker():
    """
    This method prints whether a user input matches a pre-defined password or not
    :return:
    """
    secretWord = "Fluffkinz"
    userInput = input("Guess the password: ")
    if secretWord == userInput:
        print("You guessed it")
    else:
        print("You did not guess the password")

def CoolWordsChecker():
    """
    This method tells whether a user input matches a pre-defined password or not
    :return: True if passwords match. False if not.
    """
    secretWord = "Fluffkinz"
    userInput = input("Guess the password: ")
    if secretWord == userInput:
      return True
    else:
        return False

def main():
    print()
    if CoolWordsChecker() == True:
        print("Moving to next functionality")
    else:
        print("You are stuck here")


if __name__ == "__main__":
    main()

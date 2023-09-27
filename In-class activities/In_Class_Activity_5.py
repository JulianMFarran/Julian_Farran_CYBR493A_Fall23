# Name: Julian Farran
# Date: 2023-09-27
# In Class Activity 5
# Description: This program allows the user to choose between different activities,
# including checking a password, and pinging IP addresses.
# THE CORRECT PASSWORD IS *"Fluffkinz"*
# // Any other input other than "Fluffkinz" will be incorrect.
import subprocess
from In_Class_3 import WordsChecker
from Activity_4 import ping_ip_addresses_and_save
from In_Class_3 import CoolWordsChecker

def main():
    print("Select an activity:")
    print("1. Check Password")
    print("2. Ping IP Addresses")
    print("3. Use WordsChecker")
    choice = input("Enter the number of the activity you want to execute: ")

    if choice == "1":
        if CoolWordsChecker():
            print("Password is correct. Moving to the next functionality.")
        else:
            print("Incorrect password. You are stuck here.")
    elif choice == "2":
        ip_addresses_to_ping = ["127.0.0.1", "8.0.0.1", "192.168.0.10", "192.168.10.10"]
        output_file_path = "pinger.txt"
        ping_ip_addresses_and_save(ip_addresses_to_ping, output_file_path)
    elif choice == "3":
        WordsChecker()  # Call the WordsChecker function
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

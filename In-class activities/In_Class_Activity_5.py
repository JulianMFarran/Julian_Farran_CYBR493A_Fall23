# Name: Julian Farran
# Date: 2023-09-27
# In Class Activity 5
# Description: This program allows the user to choose between different activities,
# including checking a password, and pinging IP addresses.
# THE CORRECT PASSWORD IS *"Fluffkinz"*
# // Any other input other than "Fluffkinz" will be incorrect.

import subprocess
from In_Class_3 import WordsChecker
import Activity_4
from Activity_4 import ping_ip_addresses_and_save  # Import the function we created

def main():
    print("Select an activity:")
    print("1. Check Password")
    print("2. Ping IP Addresses")
    choice = input("Enter the number of the activity you want to execute: ")

    if choice == "1":
        WordsChecker() # Call the WordsChecker function from In_Class_3
    elif choice == "2":
        # List of IP addresses to ping
        ip_addresses_to_ping = ["127.0.0.1", "8.0.0.1", "192.168.0.10", "192.168.10.10"]

        # Specify the path for the output file
        output_file_path = "pinger.txt"

        # Call the ping_ip_addresses_and_save function from Activity_4
        ping_ip_addresses_and_save(ip_addresses_to_ping, output_file_path)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

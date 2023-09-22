import subprocess

# List of IP addresses to ping
ip_addresses = ["127.0.0.1", "8.0.0.1", "192.168.0.10", "192.168.10.10"]

# Create a file to store the ping results
output_file = open("pinger.txt", "w")

# Iterate through the list of IP addresses and ping each one
for ip_address in ip_addresses:
    try:
        # Run the ping command with specified parameters
        ping_result = subprocess.check_output(["ping", "-c", "1", "-w", "2", ip_address], universal_newlines=True)
        output_file.write(f"Ping result for {ip_address}:\n")
        output_file.write(ping_result)
        output_file.write("\n")
    except subprocess.CalledProcessError as e:
        output_file.write(f"Error pinging {ip_address}: {e}\n")
    except Exception as e:
        output_file.write(f"An error occurred while pinging {ip_address}: {str(e)}\n")

# Close the output file
output_file.close()

print("Ping results have been saved to 'pinger.txt'")

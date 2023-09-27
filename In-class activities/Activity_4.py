import subprocess

def ping_ip_addresses_and_save(ip_addresses, output_file_path):
    """
    Ping a list of IP addresses and save the results to a file.

    :param ip_addresses: List of IP addresses to ping
    :param output_file_path: Path to the output file
    """
    with open(output_file_path, "w") as output_file:
        for ip_address in ip_addresses:
            try:
                ping_result = subprocess.check_output(["ping", "-c", "1", "-w", "2", ip_address], universal_newlines=True)
                output_file.write(f"Ping result for {ip_address}:\n")
                output_file.write(ping_result)
                output_file.write("\n")
            except subprocess.CalledProcessError as e:
                output_file.write(f"The ping was successful {ip_address}: {e}\n")
            except Exception as e:
                output_file.write(f"An error occurred while pinging {ip_address}: {str(e)}\n")

    print("Ping results have been saved to 'pinger.txt'")

# Usage example:
if __name__ == "__main__":
    ip_addresses_to_ping = ["127.0.0.1", "8.0.0.1", "192.168.0.10", "192.168.10.10"]
    output_file_path = "pinger.txt"
    ping_ip_addresses_and_save(ip_addresses_to_ping, output_file_path)

import subprocess
import re

def tracert(domain):
    try:
        result = subprocess.run(["tracert", domain], capture_output=True, text=True)
        output = result.stdout
        print(output)
        
        # Parse the output to identify potential bottlenecks
        lines = output.splitlines()
        for line in lines:
            # Extract RTT values using regex
            match = re.findall(r'\d+ ms', line)
            if match:
                rtt_values = [int(ms.split()[0]) for ms in match]
                if any(rtt > 100 for rtt in rtt_values):  # Example threshold for high RTT
                    print(f"Potential bottleneck detected: {line}")
    except FileNotFoundError:
        print("tracert command not found. Make sure it's available.")
    except Exception as e:  # Catching general exceptions
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    domains = ["google.com", "github.com", "bbc.co.uk"] 
    for domain in domains:
        print(f"Traceroute for {domain}:")
        tracert(domain)

    # Experiment with trace routes from different locations
    # This part assumes you have a way to change your location, e.g., using a VPN
    # You can manually change your location and run the script again
    print("Experimenting with trace routes from different locations:")
    for domain in domains:
        print(f"Traceroute for {domain} from a different location:")
        tracert(domain)
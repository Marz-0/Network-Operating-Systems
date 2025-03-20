import socket
import ipaddress

def get_ip_info(domain):
    ip = socket.gethostbyname(domain)
    ip_obj = ipaddress.ip_address(ip)

    print(f"Website: {domain}")
    print(f"IP Address: {ip}")
    print(f"Is private: {ip_obj.is_private}")
    print(f"Is global: {ip_obj.is_global}")

# Example usage with a university domain (change as needed)
get_ip_info('gold.ac.uk')

import ipaddress

def analyse_ip(ip_str):
    ip = ipaddress.ip_interface(ip_str)

    print(f"Address: {ip.ip}")
    print(f"Network: {ip.network}")
    print(f"Netmask: {ip.netmask}")
    print(f"Broadcast Address: {ip.network.broadcast_address}")
    print(f"First Usable Host: {list(ip.network.hosts())[0]}")
    print(f"Last Usable Host: {list(ip.network.hosts())[-1]}")
    print(f"Number of Usable Hosts: {ip.network.num_addresses - 2}")
    print(f"Is private: {ip.ip.is_private}")
    print(f"Is global: {ip.ip.is_global}")

# Example usage
analyse_ip('192.168.1.1/24')

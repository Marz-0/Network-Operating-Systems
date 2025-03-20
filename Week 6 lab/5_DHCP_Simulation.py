server = {
    "ip_pool": ["192.168.1.100", "192.168.1.101", "192.168.1.102"],
    "leases": {}
}

client = {
    "mac": "AA:BB:CC:DD:EE:FF",
    "ip": None
}

def send_discover():
    print("\n[CLIENT] Step 1: Sending DHCP DISCOVER")
    return {"type": "DISCOVER", "mac": client["mac"]}

def make_offer(discover):
    print("\n[SERVER] Step 2: Making DHCP OFFER")
    if not server["ip_pool"]:
        print("No IPs available!")
        return None
    offered_ip = server["ip_pool"].pop(0)
    return {"type": "OFFER", "mac": discover["mac"], "ip": offered_ip}

def send_request(offer):
    print("\n[CLIENT] Step 3: Sending DHCP REQUEST")
    return {"type": "REQUEST", "mac": offer["mac"], "ip": offer["ip"]}

def send_ack(request):
    print("\n[SERVER] Step 4: Sending DHCP ACK")
    server["leases"][request["mac"]] = request["ip"]
    return {"type": "ACK", "mac": request["mac"], "ip": request["ip"]}

def main():
    print("=== Simple DHCP Simulation ===")

    discover = send_discover()
    offer = make_offer(discover)
    if not offer:
        return

    request = send_request(offer)
    ack = send_ack(request)

    client["ip"] = ack["ip"]

    print("\n=== Result ===")
    print(f"Client {client['mac']} got IP: {client['ip']}")
    print("Server leases:", server["leases"])

if __name__ == "__main__":
    main()

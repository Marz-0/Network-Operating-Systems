import socket
from encryption import encrypt, decrypt

def authenticate_client(message, client_address, users, authenticated_clients, ip_addresses):
    parts = message[5:].split(":")
    if len(parts) == 2:
        username, password = parts
        if username in users and users[username] == password:
            authenticated_clients[client_address] = username
            ip, port = client_address
            if ip not in ip_addresses:
                ip_addresses[ip] = []
            ip_addresses[ip].append((port, username))
            return encrypt("Authentication successful!"), username
        else:
            return encrypt("Authentication failed!"), None
    else:
        return encrypt("Invalid authentication format!"), None

def handle_client_message(message, client_address, authenticated_clients):
    username = authenticated_clients[client_address]
    print(f"Encrypted message from {username}: {message}")
    decrypted_message = decrypt(message)
    print(f"Decrypted message: {decrypted_message}")
    return encrypt(f"{username}: {decrypted_message}")

def main():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 65433))
    print("UDP Secure Chat Server is running...")

    # Users database {username: password}
    users = {
        "admin": "password123",
        "alice": "secure456",
        "bob": "qwerty789"
    }

    authenticated_clients = {}
    ip_addresses = {}

    while True:
        data, client_address = server_socket.recvfrom(2048)
        encrypted_message = data.decode()
        message = decrypt(encrypted_message)

        if client_address not in authenticated_clients:
            if message.startswith("AUTH:"):
                response, username = authenticate_client(message, client_address, users, authenticated_clients, ip_addresses)
                server_socket.sendto(response.encode(), client_address)
                if username:
                    print(f"User {username} authenticated from {client_address[0]}:{client_address[1]}")
            else:
                response = encrypt("Authentication required! Use AUTH:username:password")
                server_socket.sendto(response.encode(), client_address)
        else:
            formatted_message = handle_client_message(encrypted_message, client_address, authenticated_clients)
            for client in authenticated_clients:
                if client != client_address:
                    server_socket.sendto(formatted_message.encode(), client)

if __name__ == "__main__":
    main()
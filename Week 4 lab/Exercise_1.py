import socket
import threading

print_lock = threading.Lock()

# Server code
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 65433))  # Bind to all interfaces on port 65433

    print("UDP Chat Server is running...")

    clients = set()  # Store client addresses

    while True:
        data, client_address = server_socket.recvfrom(2048)
        
        if client_address not in clients:
            clients.add(client_address)
        
        message = data.decode()
        with print_lock:
            print(f"Received from {client_address}: {message}")
        
        # Broadcast message to all clients
        for client in clients:
            if client != client_address:  # Don't send message to sender
                server_socket.sendto(data, client)

# Client code
def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('localhost', 0))  # Bind to an available port on localhost
    server_address = ('localhost', 65433)

    def receive_messages():
        while True:
            data, _ = client_socket.recvfrom(2048)
            with print_lock:
                print("\nReceived:", data.decode())

    # Start a thread to receive messages
    threading.Thread(target=receive_messages, daemon=True).start()

    while True:
        message = input("Enter message: ")
        client_socket.sendto(message.encode(), server_address)

# Run server and client in separate threads
threading.Thread(target=run_server, daemon=True).start()
threading.Thread(target=run_client, daemon=True).start()

# Keep the main thread alive
while True:
    pass
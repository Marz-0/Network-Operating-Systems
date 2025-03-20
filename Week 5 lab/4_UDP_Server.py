import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65432))

print("UDP Server is listening...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received: {data.decode()} from {client_address}")
    server_socket.sendto(b"ACK: " + data, client_address)

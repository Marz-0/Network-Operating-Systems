import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('www.example.com', 80)

# Connect to the server
client_socket.connect(server_address)

# Send an HTTP GET request
request = "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
client_socket.send(request.encode())

# Receive the response
response = client_socket.recv(4096)
print(response.decode())

# Close the socket
client_socket.close()

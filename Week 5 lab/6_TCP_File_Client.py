import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))

with open('file_to_send.txt', 'rb') as f:
    client_socket.sendfile(f)

client_socket.close()

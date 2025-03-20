import socket
import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter message: ")
start_time = datetime.datetime.now()
client_socket.sendto(message.encode(), ('localhost', 65432))

response, _ = client_socket.recvfrom(1024)
end_time = datetime.datetime.now()

print(f"Server response: {response.decode()}")
print(f"Time taken: {(end_time - start_time).total_seconds()} seconds")

client_socket.close()

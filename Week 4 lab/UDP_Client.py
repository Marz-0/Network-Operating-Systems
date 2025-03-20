import socket
import threading
from encryption import encrypt, decrypt

class UDPClient:
    def __init__(self, server_address):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = server_address

    def receive_messages(self):
        while True:
            try:
                data, _ = self.client_socket.recvfrom(2048)
                decrypted_message = decrypt(data.decode())
                print(decrypted_message)
            except Exception as e:
                print(f"Error: {e}")
                break

    def authenticate(self, username, password):
        auth_message = f"AUTH:{username}:{password}"
        encrypted_auth = encrypt(auth_message)
        self.client_socket.sendto(encrypted_auth.encode(), self.server_address)

    def send_message(self, message):
        encrypted_message = encrypt(message)
        self.client_socket.sendto(encrypted_message.encode(), self.server_address)

    def close(self):
        self.client_socket.close()

def main():
    server_address = ('localhost', 65433)
    client = UDPClient(server_address)

    username = input("Enter username: ")
    password = input("Enter password: ")
    client.authenticate(username, password)

    receive_thread = threading.Thread(target=client.receive_messages)
    receive_thread.daemon = True
    receive_thread.start()

    print("Type 'exit' to quit the chat")
    while True:
        message = input("")
        if message.lower() == 'exit':
            break
        client.send_message(message)

    client.close()

if __name__ == "__main__":
    main()
import socket

# Define server address and port
server_address = ("127.0.0.1", 12345)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and start listening
server_socket.bind(server_address)
server_socket.listen(1)

print("TCP Server is waiting for connections...")

# Accept client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    # Receive message from client
    message = client_socket.recv(1024).decode()

    if not message or message.lower() == "exit":
        print("Client disconnected.")
        break

    # Count characters and convert to uppercase
    char_count = len(message)
    response_message = f"{char_count} - {message.upper()}"

    # Send response back to client
    client_socket.send(response_message.encode())
    print(f"Received from client: {message} (Characters: {char_count})")

# Close sockets
client_socket.close()
server_socket.close()

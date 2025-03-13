import socket

# Define server address and port
server_address = ("127.0.0.1", 12345)

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(server_address)
print("Connected to the server. Type 'exit' to quit.")

while True:
    # Get user input
    message = input("Enter message: ")

    # Send message to server
    client_socket.send(message.encode())

    if message.lower() == "exit":
        break

    # Receive response from server
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")

# Close socket
client_socket.close()

import socket

SERVER_HOST = '0.0.0.0'  # Replace with the server's IP or hostname
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

while True:
    question = client_socket.recv(1024).decode()
    if not question:
        break
    print(f"Quiz Question: {question}")
    
    options = []
    for _ in range(4):
        option = client_socket.recv(1024).decode()
        options.append(option)
    
    print("\n".join(options))
    
    answer = input("Your answer (e.g., 'a', 'b', 'c', 'd', or 'exit' to finish the quiz): ")
    client_socket.send(answer.encode())
    
    if answer.lower() == 'exit':
        break

client_socket.close()

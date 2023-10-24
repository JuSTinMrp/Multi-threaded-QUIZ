import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 7878

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))


while True:
    question = client_socket.recv(1024).decode()
    if not question:
        break
    print(f'Question: {question}', end=' ')
    
    
    for _ in range(4):
        option = client_socket.recv(1024).decode()
        print(option, end=' ')
    
    
    answer = input("\nAnswer: ")
    client_socket.send(answer.encode())

client_socket.close()

# modules
import socket
import threading
import os

# IP and port number
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 7878

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)


clients = []


def handle_client(client_socket):
    
    # Username and file creation
    client_socket.send("Enter your Name: ".encode())
    username = client_socket.recv(1024).decode()
    
    print(f'{username} connected')
    print (clients)

    user_file = f'{username}.txt'
    
    # PUT QUESTIONS HERE...!!!
    question = "Testing Question 1?"
    client_socket.send(question.encode())


    answer = client_socket.recv(1024).decode()
    print(f'{username} answered: {answer}')
    # print(f'Client answered: {answer}')
    
    with open(user_file, 'a') as file:
        file.write(f'Question: {question}\nAnswer: {answer}\n\n')
    
    client_socket.close()
    clients.remove(client_socket)
    del clients[username]


while True:
    client, addr = server_socket.accept()
    print(f'Accepted connection from {addr[0]}:{addr[1]}')
    clients.append(client)

    # To join next client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()




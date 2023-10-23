# modules
import socket
import threading

# IP and port number
SERVER_HOST = '192.168.184.210'
SERVER_PORT = 7878

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

# no.of clients
clients = []

# client codes
def handle_client(client_socket):
    
    # PUT QUESTIONS HERE...!!!
    question = "Testing Question 1?"
    client_socket.send(question.encode())


    answer = client_socket.recv(1024).decode()
    print(f'Client answered: {answer}')
    
    
    client_socket.close()
    clients.remove(client_socket)


while True:
    client, addr = server_socket.accept()
    print(f'Accepted connection from {addr[0]}:{addr[1]} & USERNAME: {}')
    clients.append(client)

    # To join next client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()




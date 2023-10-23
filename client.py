import socket

SERVER_HOST = '192.168.184.210'
SERVER_PORT = 7878

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))


question = client_socket.recv(1024).decode()

# need to add question number 



print(f'Question: {question}')


answer = input("Your answer: ")
client_socket.send(answer.encode())

client_socket.close()

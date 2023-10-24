#! /usr/bin/env python

# modules
import socket
import threading
import os

# IP and port number
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 7979

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)


clients = []

# QUESTIONS
data = [
    {
        'question': 'Testing Question 1?',
        'options': ['a) a', 'b) b', 'c) c', 'd) d'],
        'correct_answer': 'c'
    },
    {
        'question': 'Testing Question 2?',
        'options': ['a) a', 'b) b', 'c) c', 'd) d'],
        'correct_answer': 'b'
    },
    
]

def handle_client(client_socket):
    
    # Username and file creation
    client_socket.send("Enter your Name: ".encode())
    username = client_socket.recv(1024).decode()
    
    print(f'{username} connected')
    print (clients)

    user_file = f'{username}.txt'
    ans_file = f'{username}_ans.txt'
    
    
    for question_data in data:
        
        question_with_options = f"{question_data['question']} [{', '.join(question_data['options'])}]"
        client_socket.send(question_with_options.encode())

        
        answer = client_socket.recv(1024).decode()
        print(f'{username} answered: {answer}')

        
        with open(user_file, 'a') as file:
            file.write(f'Question: {question_data["question"]}\nAnswer: {answer}\nCorrect Answer: {question_data["correct_answer"]}\n\n')

        with open(ans_file, 'a') as file:
            file.write(f'{answer}\n')


    client_socket.close()
    clients.remove(client_socket)
    del clients[username]
    file.close()

while True:
    client, addr = server_socket.accept()
    print(f'Accepted connection from {addr[0]}:{addr[1]}')
    clients.append(client)
    # clients['client'].append(client)

    # To join next client
    client_handler = threading.Thread(target=handle_client(client))
    client_handler.start()




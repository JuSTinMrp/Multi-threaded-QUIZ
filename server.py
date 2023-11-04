#!/usr/bin/env python

# modules
import socket
import threading
import os


def handle_client(client_socket):
    
    # Username and file creation
    user_question="Enter your Name: "
    client_socket.send(user_question.encode())
    username = client_socket.recv(1024).decode()
    
    print(f'{username} connected')
    # print (clients)

    # user_file = f'{username}.txt'
    # # ans_file = f'{username}_ans.txt'
    
    
    # for question_data in data:
        
    #     question_with_options = f"{question_data['question']} [{', '.join(question_data['options'])}]"
    #     client_socket.send(question_with_options.encode())

        
    #     answer = client_socket.recv(1024).decode()
    #     print(f'{username} answered: {answer}')

        
    #     with open(user_file, 'a') as file:
    #         file.write(f'Question: {question_data["question"]}\nAnswer: {answer}\nCorrect Answer: {question_data["correct_answer"]}\n\n')

    #     # with open(ans_file, 'a') as file:
    #     #     file.write(f'{answer}\n')

    client_socket.close()
    client_threads.remove(threading.current_thread())
    
    
# IP and port number
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1111

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)


client_threads = []

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

while True:
    # print("Waiting for a client to connect...")
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    
    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_threads.append(client_thread)
    client_thread.start()



    # clients.remove(client_socket)
    # del clients[username]
    # file.close()
    







#!/usr/bin/env python

# modules
import socket
import threading
import random
import json
import os #for path -> file creation


def convertQtobQ(questions):
    bquestion = {}
    for i,j in questions.items():
        bquestion.setdefault(i,json.dumps(j).encode())
    return bquestion

def handle_client(client_socket,client_addr):
    
    # Username and file creation
    user_question="Enter your Name: "
    client_socket.send(user_question.encode())
    username = client_socket.recv(1024).decode()

    # hostname = socket.gethostname()
    filepath = os.path.join('ans_sheets')
        
    if not os.path.exists(filepath):
        os.makedirs(filepath, exist_ok=True)
        
    user_file = os.path.join(filepath, f'{username}.txt')
    
    print(f'{username} connected')

    client_socket.send(str(NO_OF_QUES).encode())
    t_q_IDs = q_IDs.copy()
    random.shuffle(t_q_IDs)

    for q_ID in random.sample(t_q_IDs,NO_OF_QUES):
        # json_str = json.dumps(questions[q_ID])
        # bytes_representation = json_str.encode()

        client_socket.send(bquestion[q_ID])
        c = int(client_socket.recv(1024).decode())
        for i, (question, answer, correct_answer) in enumerate(questions, start=1):
            print(f'{username} answered {answer} for question {questions[q_ID]}.')
 
            correct_answer = questions[q_ID]['correct_answer']
            
            with open(user_file, 'a') as file:
                file.write(f'Question: {questions[q_ID]["question"]}\nAnswer: {answer}\nCorrect Answer: {correct_answer}\n\n')


        
    client_socket.close()
    print(f'\n\n{username} Exited...\n\n')




# IP and port number
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1111

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

# tot.connections
Connection_count=0

# Total questions
NO_OF_QUES = 2
# MOdify the question 
questions = {
    1: {
        'question': 'How are you',
        'choices': ['fine', 'not bad', 'good', 'can\'t disclose'],
        'correct_answer': 'fine'
    },
    2: {
        'question': 'What is your name',
        'choices': ['Alice', 'Bob', 'Charlie', 'David'],
        'correct_answer': 'Charlie'
    },
    3: {
        'question': 'Where are you from',
        'choices': ['USA', 'Canada', 'UK', 'Australia'],
        'correct_answer': 'usa'
    },
    4: {
        'question': 'Favorite color',
        'choices': ['Red', 'Blue', 'Green', 'Yellow'],
        'correct_answer': 'blue'
    },
    5: {
        'question': 'What is your favorite food',
        'choices': ['Pizza', 'Burger', 'Sushi', 'Pasta'],
        'correct_answer': 'pizza'
    },
    6: {
        'question': 'How do you like to spend your weekends',
        'choices': ['Reading', 'Hiking', 'Netflix', 'Gaming'],
        'correct_answer': 'hiking'
    },
    7: {
        'question': 'Favorite animal',
        'choices': ['Dog', 'Cat', 'Dolphin', 'Elephant'],
        'correct_answer': 'cat'
    },
    8: {
        'question': 'Favorite movie genre',
        'choices': ['Action', 'Comedy', 'Drama', 'Science Fiction'],
        'correct_answer': 'action'
    },
    9: {
        'question': 'What\'s your dream travel destination',
        'choices': ['Paris', 'Tokyo', 'Hawaii', 'New York'],
        'correct_answer': 'paris'
    },
    10: {
        'question': 'What\'s your preferred way of transportation',
        'choices': ['Car', 'Bicycle', 'Public Transit', 'Walking'],
        'correct_answer': 'car'
    },
}


bquestion = convertQtobQ(questions)
q_IDs = list(questions.keys())

while True:
    # print("Waiting for a client to connect...")
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    
    #Total connection so far
    Connection_count+=1
    print(f"Total Connection: {Connection_count}")
    
    # Creating new threads for upcoming clients
    client_thread = threading.Thread(target=handle_client, args=(client_socket,client_address,))
    
    # new thread starting
    client_thread.start()


    
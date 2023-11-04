import socket
import threading

# Define the server address and port
SERVER_ADDRESS = ('0.0.0.0', 12345)

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(5)

# List to store client threads and their scores
client_threads = []
client_scores = {}

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            if data == 'REQUEST_QUESTION':
                send_question(client_socket)
            else:
                handle_answer(client_socket, data)
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()

def send_question(client_socket):
    if len(quiz_questions) > 0:
        question = quiz_questions.pop(0)  # Get the next question
        client_socket.send(f"QUESTION:{question['question']}".encode('utf-8'))
        for option in question['options']:
            client_socket.send(option.encode('utf-8'))
        client_socket.send(''.encode('utf-8'))  # Signal the end of options
    else:
        client_socket.send('QUIZ_OVER'.encode('utf-8'))

def handle_answer(client_socket, answer):
    # Check if the answer is correct
    question = quiz_questions[0]
    if answer == question['correct_answer']:
        client_scores[client_socket] = client_scores.get(client_socket, 0) + 1

# Question database (replace with your actual data)
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['A) Paris', 'B) London', 'C) Berlin', 'D) Madrid'],
        'correct_answer': 'A',
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['A) Mars', 'B) Venus', 'C) Earth', 'D) Jupiter'],
        'correct_answer': 'A',
    },
    # Add more questions here
]

# Start the server
while True:
    print("Waiting for a client to connect...")
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    
    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_threads.append(client_thread)
    client_thread.start()

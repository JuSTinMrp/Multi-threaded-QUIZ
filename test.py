import socket

SERVER_HOST = '0.0.0.0'  # Listen on all available network interfaces
SERVER_PORT = 12345

questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['a) London', 'b) Berlin', 'c) Paris', 'd) Madrid'],
        'correct_answer': 'c'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['a) Venus', 'b) Mars', 'c) Jupiter', 'd) Saturn'],
        'correct_answer': 'b'
    },
    # Add more questions here
]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f"Server is listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    for question_data in questions:
        # Send the question to the client
        client_socket.send(question_data['question'].encode())
        # Send the answer options to the client
        for option in question_data['options']:
            client_socket.send(option.encode())
        
        # Receive the client's answer
        answer = client_socket.recv(1024).decode()
        print(f"Client answered: {answer}")
        # Check the answer and send feedback (you can add your logic here)

    client_socket.close()
